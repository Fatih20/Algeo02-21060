import cv2
import numpy as np
import os
# import matplotlib.pyplot as pyplot


def path_generator(folder_name):
    path_list = []
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            if file.endswith('.jpg'):
                path_list.append(root + "/" + file)
    return path_list


def image_f_matrix_generator(folder_name):
    matrix_list = []
    path_list = path_generator(folder_name)
    for path in path_list:
        original_matrix = (cv2.imread(path, 0))
        flatten_matrix = original_matrix.flatten()
        matrix_list.append(flatten_matrix)
    return matrix_list


def average_flatten_generator(matrix_list):
    n = len(matrix_list)
    sum_matrix = matrix_list[0]
    for i in range(1, n):
        sum_matrix = np.add(sum_matrix, matrix_list[i])
    sum_matrix = sum_matrix * (1/n)
    return sum_matrix


def transposed_training_matrix_generator(flat_matrix_list, average_matrix):
    flat_difference_list = []
    # print(flat_difference_list.shape)
    n = len(flat_matrix_list)
    for i in range(0, n):
        added_matrix = np.subtract(flat_matrix_list[i], average_matrix)
        flat_difference_list.append(added_matrix)
    return (np.array(flat_difference_list))


def eigen_generator(covariant_acc, training_matrix):
    eigenval_list, eigenvec_acc_list = np.linalg.eig(covariant_acc)
    eigenvec_list = np.array([]).reshape(65536, 0)
    for eigenvec_acc in eigenvec_acc_list:
        new_eigenvec = (np.matmul(
            training_matrix, (np.array(eigenvec_acc)[np.newaxis].T)))
        new_eigenvec = new_eigenvec / np.sqrt((new_eigenvec**2).sum())
        eigenvec_list = np.append(eigenvec_list, new_eigenvec, axis=1)
    return eigenval_list, eigenvec_list


def y_generator(covariant_acc, training_matrix):
    eigenval_list, eigenvec_matrix = eigen_generator(
        covariant_acc, training_matrix)
    eigenvec_matrix_t = eigenvec_matrix.T
    return np.matmul(eigenvec_matrix_t, training_matrix)


flat_matrix_list = image_f_matrix_generator(
    "/media/fatih/Mass Storage/Tugas-Tugas Kuliah/Algeom/Tubes 2/Algeo02-13521060/pepsiman/test_image")
average_matrix = average_flatten_generator(flat_matrix_list)
transposed_training_matrix = transposed_training_matrix_generator(
    flat_matrix_list, average_matrix)
training_matrix = np.transpose(transposed_training_matrix)
covariant_acc = np.matmul(transposed_training_matrix, training_matrix)

y = y_generator(covariant_acc, training_matrix)


np.savetxt("matrix.txt", y, fmt='%.18e')

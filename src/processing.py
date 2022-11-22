import cv2
import numpy as np
import os
import eigen_function as eigfunc

USE_NP_LINALG_EIG = False

def path_generator(folder_name):
    name_list = []
    path_list = []
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            if file.endswith('.jpg'):
                name_list.append(int(file[:len(file)-4]))
        name_list.sort()
        for name in name_list:
            path_list.append(f"{root}/{name}.jpg")
    return path_list


def image_f_matrix_generator(folder_name):
    path_list = path_generator(folder_name)
    sizeOfFlatMatrix = np.prod((cv2.imread(path_list[0], 0)).shape)
    flat_matrix_list = np.array([]).reshape(sizeOfFlatMatrix, 0)
    for path in path_list:
        original_matrix = (cv2.imread(path, 0))
        flatten_matrix = np.array(original_matrix.flatten())[np.newaxis].T
        flat_matrix_list = np.append(flat_matrix_list, flatten_matrix, axis=1)
    return flat_matrix_list


def average_flatten_generator(matrix_list):
    n = len((matrix_list[0]))
    sum_matrix = matrix_list[:, 0]
    for i in range(1, n):
        sum_matrix = np.add(sum_matrix, matrix_list[:, i])
    sum_matrix = np.array(sum_matrix)[np.newaxis].T
    average_matrix = sum_matrix * (1/n)
    return average_matrix


def training_matrix_generator(flat_matrix_list, average_matrix):
    n = len(flat_matrix_list[0])
    flat_difference_list = np.array([]).reshape(len(flat_matrix_list), 0)
    for i in range(0, n):
        added_matrix = np.subtract(np.array(flat_matrix_list[:, i])[
                                   np.newaxis].T, average_matrix)
        flat_difference_list = np.append(
            flat_difference_list, added_matrix, axis=1)
    return ((flat_difference_list))


def eigen_generator(covariant_acc, training_matrix):
    if (USE_NP_LINALG_EIG is True):
        eigenval_list, eigenvec_acc_list = np.linalg.eig(covariant_acc)
    else:
        eigenval_list, eigenvec_acc_list = eigfunc.QR_eig(covariant_acc)

    row, column = training_matrix.shape
    eigenvec_list = np.array([]).reshape(row, 0)
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


def omega_of_target(filename, average_matrix, eigenvec_matrix):
    original_target_matrix = (cv2.imread(f"{filename}", 0))
    flatten_target = np.array(original_target_matrix.flatten())[np.newaxis].T
    omega = np.matmul(eigenvec_matrix.T, np.subtract(
        flatten_target, average_matrix))
    return omega


def euclidean_distance(matrix_a, matrix_b):
    subtract = matrix_a - matrix_b
    return np.sqrt(np.dot(subtract.T, subtract))


def bestface(average_matrix, eigenvec_matrix, y, path_list, testedImage):
    omega_in_array = omega_of_target(testedImage,
                                     average_matrix, eigenvec_matrix).flatten()
    min_column_r = y[:, 0]
    min_dist = euclidean_distance(omega_in_array, min_column_r)
    min_column = 0
    n = len(y[0])
    for i in range(1, n):
        observed_column = y[:, i]
        dist = euclidean_distance(omega_in_array, observed_column)
        if dist < min_dist:
            min_dist = dist
            min_column = i
            min_column_r = observed_column
    if (min_dist < 10**6):
        return path_list[min_column]
    else:
        return ""


def process_images(folder_name):
    path_list = path_generator(folder_name)
    flat_matrix_list = image_f_matrix_generator(folder_name)
    average_matrix = average_flatten_generator(flat_matrix_list)
    training_matrix = training_matrix_generator(
        flat_matrix_list, average_matrix)
    training_matrix_t = np.transpose(training_matrix)
    covariant_acc = np.matmul(training_matrix_t, training_matrix)
    ev, e = eigen_generator(covariant_acc, training_matrix)
    y = y_generator(covariant_acc, training_matrix)
    return path_list, e, y, average_matrix, int((len(flat_matrix_list))**(1/2))
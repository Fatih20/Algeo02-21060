import cv2
import numpy as np
import os
# import matplotlib.pyplot as pyplot


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
    flat_matrix_list = np.array([]).reshape(65536, 0)
    path_list = path_generator(folder_name)
    for path in path_list:
        original_matrix = (cv2.imread(path, 0))
        flatten_matrix = np.array(original_matrix.flatten())[np.newaxis].T
        flat_matrix_list = np.append(flat_matrix_list, flatten_matrix, axis=1)
    # flat_matrix_list is X
    return flat_matrix_list


def average_flatten_generator(matrix_list):
    n = len((matrix_list[0]))
    sum_matrix = matrix_list[:, 0]
    for i in range(1, n):
        sum_matrix = np.add(sum_matrix, matrix_list[:, i])
    sum_matrix = np.array(sum_matrix)[np.newaxis].T
    average_matrix = sum_matrix * (1/n)
    # This is the mean matrix
    return average_matrix


def training_matrix_generator(flat_matrix_list, average_matrix):
    n = len(flat_matrix_list[0])
    flat_difference_list = np.array([]).reshape(65536, 0)
    for i in range(0, n):
        added_matrix = np.subtract(np.array(flat_matrix_list[:, i])[
                                   np.newaxis].T, average_matrix)
        # flat_difference_list.append(added_matrix)
        flat_difference_list = np.append(
            flat_difference_list, added_matrix, axis=1)
    # This is A
    return ((flat_difference_list))


def eigen_generator(covariant_acc, training_matrix):
    eigenval_list, eigenvec_acc_list = np.linalg.eig(covariant_acc)
    eigenvec_list = np.array([]).reshape(65536, 0)
    for eigenvec_acc in eigenvec_acc_list:
        new_eigenvec = (np.matmul(
            training_matrix, (np.array(eigenvec_acc)[np.newaxis].T)))
        new_eigenvec = new_eigenvec / np.sqrt((new_eigenvec**2).sum())
        eigenvec_list = np.append(eigenvec_list, new_eigenvec, axis=1)
    # Eigenvec_list is E
    return eigenval_list, eigenvec_list


def y_generator(covariant_acc, training_matrix):
    eigenval_list, eigenvec_matrix = eigen_generator(
        covariant_acc, training_matrix)
    eigenvec_matrix_t = eigenvec_matrix.T
    # This is Y
    return np.matmul(eigenvec_matrix_t, training_matrix)


def omega_of_target(filename, average_matrix, eigenvec_matrix):
    original_target_matrix = (cv2.imread(f"{filename}", 0))
    flatten_target = np.array(original_target_matrix.flatten())[np.newaxis].T
    omega = np.matmul(eigenvec_matrix.T, np.subtract(
        flatten_target, average_matrix))
    return omega


def bestface(average_matrix, eigenvec_matrix, y, path_list):
    omega_in_array = omega_of_target("70",
                                     average_matrix, eigenvec_matrix).flatten()
    min_column_r = y[:, 0]
    min_dist = np.linalg.norm(omega_in_array - min_column_r)
    min_column = 0
    n = len(y[0])
    for i in range(1, n):
        observed_column = y[:, i]
        dist = np.linalg.norm(omega_in_array - observed_column)
        if dist < min_dist:
            min_dist = dist
            min_column = i
            min_column_r = observed_column
    return path_list[min_column]


# path_list = path_generator(
#     "/media/fatih/Mass Storage/Tugas-Tugas Kuliah/Algeom/Tubes 2/Algeo02-13521060/pepsiman/test_image")
# flat_matrix_list = image_f_matrix_generator(
#     "/media/fatih/Mass Storage/Tugas-Tugas Kuliah/Algeom/Tubes 2/Algeo02-13521060/pepsiman/test_image")

# average_matrix = average_flatten_generator(flat_matrix_list)

# training_matrix = training_matrix_generator(
#     flat_matrix_list, average_matrix)
# training_matrix_t = np.transpose(training_matrix)
# covariant_acc = np.matmul(training_matrix_t, training_matrix)
# ev, e = eigen_generator(covariant_acc, training_matrix)

# omega = omega_of_target("70", average_matrix, e)

# y = y_generator(covariant_acc, training_matrix)
# file_of_bestface = bestface(average_matrix, e, y, path_list)
# print(file_of_bestface)

# np.savetxt("matrix.txt", y, fmt='%.18e')
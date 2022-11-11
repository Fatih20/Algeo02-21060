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


def training_matrix_generator(flat_matrix_list, average_matrix):
    flat_difference_list = []
    # print(flat_difference_list.shape)
    n = len(flat_matrix_list)
    for i in range(0, n):
        added_matrix = np.subtract(flat_matrix_list[i], average_matrix)
        flat_difference_list.append(added_matrix)
    return np.array(flat_difference_list)


flat_matrix_list = image_f_matrix_generator(
    "/media/fatih/Mass Storage/Tugas-Tugas Kuliah/Algeom/Tubes 2/Algeo02-13521060/pepsiman/test_image")
average_matrix = average_flatten_generator(flat_matrix_list)
training_matrix = training_matrix_generator(flat_matrix_list, average_matrix)
np.savetxt("matrix.txt", training_matrix, fmt='%.6g')

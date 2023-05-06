import numpy as np
import math


#rotate shape 90 deg clockwise
def rotate_shape(shape: np.array):
    rotation_matrix = np.array([[0, -1], [1, 0]])
    rotated_matrix = []
    for i in shape:
        rotated_matrix.append(np.dot(i, rotation_matrix))
    return rotated_matrix


shape = np.array([[ 0, 0], [ 1,  0], [ 0, -1], [ 2,  0]])
print(rotate_shape(shape))
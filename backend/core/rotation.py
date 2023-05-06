import numpy as np
import math


#rotate shape
def rotate_shape(shape: np.array):
    rotation_matrix = np.array([[0 -1], [1, 0]])
    for i in shape:
        print(i)


shape = np.array([[ 0, 0], [ 1,  0], [ 0, -1], [ 2,  0]])
rotate_shape(shape)
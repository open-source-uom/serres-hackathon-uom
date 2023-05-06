import numpy as np

class manipullator:
    #a matrix that contains the rotation matrixes, 1:flip vertically, 2:flip horizontaly
    rotation_matrixes = np.array([
        [
            [0, -1], #0:90 clockwise rotation
            [1, 0]
        ],
        [
            [1, 0], #1:flip vertically
            [0, -1]
        ],
        [
            [-1, 0], #2:flip horizontaly
            [0, 1]
        ]
    ]
    )
    def rotate_shape(self, shape: np.array, rotation: int):
        rotated_matrix = []
        for i in shape:
            rotated_matrix.append(np.dot(i, self.rotation_matrixes[rotation]))

        return rotated_matrix

shape = np.array([[ 0, 0], [ 1,  0], [ 0, -1], [ 2,  0]])
man = manipullator()
print(man.rotate_shape(shape, 2))
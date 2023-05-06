import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable, Any
#from canvas import Canvas

class Shape():

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

    shape_to_coords_dict = {"F": np.array([[0, 0],[0, -1],[1, -1],[0, 1],[-1, 0]]),
        "I": np.array([[0, 0], [0, -1], [0, -2], [0, 1], [0, 2]]),
        "N": np.array([[0, 0],[-1, 0],[-1, 1],[0, -1],[0, -2]]),
        "P": np.array([[0, 0],[0, -1],[1, -1],[1, 0],[0, 1]]),
        "T": np.array([[0, 0],[1, 0],[-1, 0],[0, 1],[0, 2]]),
        "U": np.array([[0, 0],[-1, 0],[1, 0],[1, -1],[-1, -1]]),
        "V": np.array([[0, 0],[0, -1],[0, -2],[-1, 0],[-2, 0]]),
        "W": np.array([[0, 0],[-1, 0],[-1, -1],[0, 1],[1, 1]]),
        "X": np.array([[0, 0],[1, 0],[-1, 0],[0, 1],[0, -1]]),
        "Y": np.array([[0, 0],[-1, 0],[0, -1],[0, 1],[0, 2]]),
        "Z": np.array([[0, 0],[0, -1],[-1, -1],[0, 1],[1, 1]])
    }
    def __init__(self,letter:str):
        if letter not in self.shape_to_coords_dict: raise ValueError
        self.value = letter.upper()
        self.coords = self.shape_to_coords_dict[letter]
        self.origin: Tuple[int, int] = 0, 0
        self.rotation_state:int = 0
        pass
    def get_coords_list(self) -> List:
        return list(self.coords.tolist())
    # mporei na einai kai degrees tha doume
    def rotate_basic_shape(self, cords, rotation:int):
        rotated_matrix = []
        for i in cords:
            rotated_matrix.append(np.dot(i, self.rotation_matrixes[rotation]))
        return rotated_matrix
    def rotate_shape(self,r:int):
        rotated_matrix = []
        if r==0:
            self.coords = self.shape_to_coords_dict[self.value]
        elif r==1:
            self.coords = self.rotate_basic_shape(self.shape_to_coords_dict[self.value], 0)
        elif r==2:
            self.coords = self.rotate_basic_shape(self.shape_to_coords_dict[self.value], 0)
            self.coords = self.rotate_basic_shape(self.coords, 0)
        elif r==3:
            self.coords = self.rotate_basic_shape(self.shape_to_coords_dict[self.value], 0)
            self.coords = self.rotate_basic_shape(self.coords, 0)
            self.coords = self.rotate_basic_shape(self.coords, 0)
        elif r==4:
            self.coords = self.rotate_basic_shape(self.shape_to_coords_dict[self.value], 1)
        elif r==5:
            self.coords = self.rotate_basic_shape(self.shape_to_coords_dict[self.value], 2)
        self.rotation_state = r
        self.coords = np.array(self.coords)
        self.change_cords_by_a_position(self.origin)


    def change_cords_by_a_position(self,position:Tuple[int,int]):
        self.coords = self.coords + position
        self.origin = position
    def set_coords_list(self,coords:List):
        self.coords = np.array(coords)

    def get_symbol_to_show(self):
        return self.value+self.rotation_state

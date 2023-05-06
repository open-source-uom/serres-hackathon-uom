import collections
from functools import reduce

import numpy as np
from typing import List, Tuple


# shape_to_coords_dict = {"L":np.array(np.array()),"F":np.array(np.array()),
#                         "I":np.array(np.array()),"N":np.array(np.array()),
#                         "P":np.array(np.array()),"T":np.array(np.array()),
#                         "U":np.array(np.array()),"V":np.array(np.array()),
#                         "W":np.array(np.array()),"X":np.array(np.array()),
#                         "Y":np.array(np.array()),"Z":np.array(np.array()),}



# Q2
def generate_all_shapes():
    available_tiles:List[str] = ["F","I","L","N","P","T","U","V","W","X","Y","Z"]
    all_available_shapes:List[Shape] = list(map(lambda letter: Shape(letter),available_tiles))


class Shape():
    shape_to_coords_dict = {"L": np.array(np.array(0)), "F": np.array(np.array(0)),
                            "I": np.array(np.array(0)), "N": np.array(np.array(0)),
                            "P": np.array(np.array(0)), "T": np.array(np.array(0)),
                            "U": np.array(np.array(0)), "V": np.array(np.array(0)),
                            "W": np.array(np.array(0)), "X": np.array(np.array(0)),
                            "Y": np.array(np.array(0)), "Z": np.array(np.array(0)), }
    def __init__(self,letter:str):
        if(letter not in self.shape_to_coords_dict):raise ValueError
        self.coords = self.shape_to_coords_dict[letter]
        self.origin:Tuple[int,int] = 0,0
        pass

    # mporei na einai kai degrees tha doume
    def rotate_shape(self,radians:float):
        # calculate sinΘ cosΘ
        # this will change the coords (while maintaining the same origin ig)
        pass



def run_fn_and_count_time():
    pass

#mporei na mhn xreiastei
class CongruentGroup:
    pass


def main():
    my_canvas = Canvas(5,6)
    result1 = my_canvas.count_filled_cells()
    print("Filled Cells" ,result1)
    result2 = my_canvas.count_empty_cells()
    print("Empty Cells",result2)
    result3 = my_canvas.count_holes()
    print("Hole Cells",result3)

class Canvas():

    empty_cell_char = 'E'
    hole_cell_char = 'H'

    # to megethos den mas apasxolei sto backend
    def __init__(self,lines:int,rows:int):
        self.shapes_placed:List[Shape] = []
        enough_empty_cells = [self.empty_cell_char for i in range(lines*rows)]
        # den einai swsto auto
        # self.matrix = np.arange(lines * rows).reshape(lines,rows)
        self.matrix = np.full((lines,rows),'E')
        print("MATRIX OF:",self.matrix)


        pass

    def __str__(self):
        my_string:str = ""
        for elem in self.matrix:
            pass



    def count_empty_cells(self) -> int:
        the_sum = 0
        for row in self.matrix:
            for elem in row:
                if elem == self.empty_cell_char:
                    print(elem)
                    the_sum += 1

        return the_sum
    def count_filled_cells(self) -> int:
        the_sum = 0
        for row in self.matrix:
            for elem in row:
                if elem != self.empty_cell_char and elem != self.hole_cell_char:
                    print(elem)
                    the_sum += 1

        return the_sum
    def count_holes(self) -> int:
        the_sum = 0
        for row in self.matrix:
            for elem in row:
                if elem == self.hole_cell_char:
                    print(elem)
                    the_sum += 1

        return the_sum
        pass
    def get_holes(self) -> List[Tuple[int,int]]:
        pass
    def calculate_parameter_of_shape(self,s1:Shape) -> int:
        pass

    def get_empty_cells(self)->List[Tuple[int,int]]:
        pass

    def place_hole_in(self,x,y):
        pass

    def shapes_touch(self,s1:Shape,s2:Shape) -> bool:
        pass
    def merge_shapes(self,s1:Shape,s2:Shape):
        # this will return a shape that has the coordinates of both
        # shapes should touch --> be a Congruent Group/Group
        # !!! there will be a problem with defining its origin
        # we might just make it a different Class
        pass

main()
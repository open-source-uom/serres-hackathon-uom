import collections
from functools import reduce
import time
import numpy as np
from typing import List, Tuple, Callable, Any

# 9] Create a function that calculates (in milliseconds, ms) the execution time of any other function.
def measure_time(func: Callable[..., Any], *args: Tuple[Any], **kwargs: Any) -> Any:
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    running_time = end_time - start_time
    print(f"Function {func.__name__} took {running_time:.6f} seconds to run.")
    return result

# 10] Create a program that finds each and every (unique) way to fill a Canvas (with or without black cells)
# with the maximum number of Shapes given (with or without rotation and flipping allowed).
def find_ways_to_fill_canvas():
    pass

# Q2
def generate_all_shapes():
    available_tiles:List[str] = ["F","I","L","N","P","T","U","V","W","X","Y","Z"]
    all_available_shapes:List[Shape] = list(map(lambda letter: Shape(letter),available_tiles))


class Shape():
    # shapes = {
    #     "F": np.array([0, 0],[0, -1],[1, -1],[0, 1],[-1, 0]),
    #     "I": np.array([0, 0],[0, -1],[0, -2],[0, 1],[0, 2],),
    #     "N": [
    #         [0, 0],
    #         [-1, 0],
    #         [-1, 1],
    #         [0, -1],
    #         [0, -2],
    #     ],
    #     "P": [
    #         [0, 0],
    #         [0, -1],
    #         [1, -1],
    #         [1, 0],
    #         [0, 1],
    #     ],
    #     "T": [
    #         [0, 0],
    #         [1, 0],
    #         [-1, 0],
    #         [0, 1],
    #         [0, 2],
    #     ],
    #     "U": [
    #         [0, 0],
    #         [-1, 0],
    #         [1, 0],
    #         [1, -1],
    #         [-1, -1],
    #     ],
    #     "V": [
    #         [0, 0],
    #         [0, -1],
    #         [0, -2],
    #         [-1, 0],
    #         [-2, 0],
    #     ],
    #     "W": [
    #         [0, 0],
    #         [-1, 0],
    #         [-1, -1],
    #         [0, 1],
    #         [1, 1],
    #     ],
    #     "X": [
    #         [0, 0],
    #         [1, 0],
    #         [-1, 0],
    #         [0, 1],
    #         [0, -1],
    #     ],
    #     "Y": [
    #         [0, 0],
    #         [-1, 0],
    #         [0, -1],
    #         [0, 1],
    #         [0, 2],
    #     ],
    #     "Z": [
    #         [0, 0],
    #         [0, -1],
    #         [-1, -1],
    #         [0, 1],
    #         [1, 1],
    #     ]
    # }
    shape_to_coords_dict = {"F": np.array([0, 0],[0, -1],[1, -1],[0, 1],[-1, 0]),
        "I": np.array([0, 0], [0, -1], [0, -2], [0, 1], [0, 2]),
        "N": np.array([0, 0],[-1, 0],[-1, 1],[0, -1],[0, -2]),
        "P": np.array([0, 0],[0, -1],[1, -1],[1, 0],[0, 1]),
        "T": np.array([0, 0],[1, 0],[-1, 0],[0, 1],[0, 2]),
        "U": np.array([0, 0],[-1, 0],[1, 0],[1, -1],[-1, -1]),
        "V": np.array([0, 0],[0, -1],[0, -2],[-1, 0],[-2, 0]),
        "W": np.array([0, 0],[-1, 0],[-1, -1],[0, 1],[1, 1]),
        "X": np.array([0, 0],[1, 0],[-1, 0],[0, 1],[0, -1]),
        "Y": np.array([0, 0],[-1, 0],[0, -1],[0, 1],[0, 2]),
        "Z": np.array([0, 0],[0, -1],[-1, -1],[0, 1],[1, 1])
    }
    def __init__(self,letter:str):
        if letter not in self.shape_to_coords_dict: raise ValueError
        self.value = letter.upper()
        self.coords = self.shape_to_coords_dict[letter]
        self.origin: Tuple[int, int] = 0, 0
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
        holes = []
        rows,cols = self.matrix.shape
        for row_index in range(rows):
            for col_index in range(cols):
                elem = self.matrix[row_index][col_index]
                if elem == self.hole_cell_char:
                    print(elem)
                    holes.append((row_index,col_index))


        return holes

    # Calculate Parameter of shape
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
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
    #print(f"Function {func.__name__} took {running_time:.6f} seconds to run.")
    return result

# 10] Create a program that finds each and every (unique) way to fill a Canvas (with or without black cells)
# with the maximum number of Shapes given (with or without rotation and flipping allowed).
def find_ways_to_fill_canvas():
    pass

# Q2
def generate_all_shapes():
    available_tiles:List[str] = ["F","I","N","P","T","U","V","W","X","Y","Z"]
    all_available_shapes:List[Shape] = list(map(lambda letter: Shape(letter),available_tiles))


class Shape():

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
        pass
    def get_coords_list(self) -> List:
        return list(self.coords.tolist())
    # mporei na einai kai degrees tha doume
    def rotate_shape(self,radians:float):
        # calculate sinΘ cosΘ
        # this will change the coords (while maintaining the same origin ig)
        pass
    def change_cords_by_a_position(self,position:Tuple[int,int]):
        self.coords = self.coords + position



def run_fn_and_count_time():
    pass

#mporei na mhn xreiastei
class CongruentGroup:
    pass


def main():
                    #  Y X
    my_canvas = Canvas(6,5, [])
    result1 = my_canvas.count_filled_cells()
    #print("Filled Cells" ,result1)
    result2 = my_canvas.count_empty_cells()
    #print("Empty Cells",result2)
    result3 = my_canvas.count_holes()
    #print("Hole Cells",result3)
    s1 = Shape('F')
    # s2 = Shape('L')
    # s3 = Shape('T')

    pos = (1,1)
    Shape.change_cords_by_a_position(s1,pos)
    #print(s1.get_coords_list())

    #print(my_canvas.check_for_out_of_bounds_when_placed_in(s1,pos))                                    # Y X
    #my_canvas.place_shape_checked(s1,pos)


class Canvas():

    empty_cell_char = '-'
    hole_cell_char = 'B'

    # to megethos den mas apasxolei sto backend
    def __init__(self,lines:int,rows:int, holes:List[Tuple[int, int]]):#y:lines,x:rows

        self.shapes_placed:List[Shape] = []
        self.holes: List[Tuple[int, int]] = holes
        enough_empty_cells = [self.empty_cell_char for i in range(lines*rows)]
        # den einai swsto auto
        # self.matrix = np.arange(lines * rows).reshape(lines,rows)
        self.matrix = np.full((lines,rows),self.empty_cell_char)
        #print("MATRIX OF:",self.matrix)

    def check_for_stepping_in_hole_when_placed_in(self,s:Shape,position:Tuple[int,int]):
        position_x, position_y = position
        pass
    def check_for_out_of_bounds_when_placed_in(self,s:Shape,position:Tuple[int,int])->bool:
        position_x,position_y = position
        coords = s.get_coords_list()
        all_x = list(map(lambda coord: coord[0], coords))
        all_x_sorted = sorted(all_x)
        #print(all_x_sorted)
        all_y = list(map(lambda coord: coord[1], coords))
        all_y_sorted = sorted(all_y)

        min_x = all_x_sorted[0]
        min_y = all_y_sorted[0]

        max_x = all_y_sorted[len(all_x_sorted)-1]
        max_y = all_y_sorted[len(all_y_sorted)-1]

        # everything is signed so just add it
        max_position_x = position_x + max_x
        max_position_y = position_y + max_y

        min_position_x = position_x + min_x
        min_position_y = position_y + min_y

        if min_position_y< 0 or min_position_x < 0 or max_position_x > self.matrix.shape[0] -1 or max_position_y > self.matrix.shape[1] - 1:
            return False
        return True

    def place_shape_unchecked(self,s:Shape,position:Tuple[int,int]):
        pass
    def place_shape(self,s:Shape,position:Tuple[int,int]):
        position_x,position_y = position
        coords = s.get_coords_list()
        self.shaps_placed.append(s)
        s.change_cords_by_a_position(position)

        #draw the board appropriately
        for coord_tuple in coords:
            # position_y,position_x to origin kai thelw na efarmosw ta transforms
        #    print(coord_tuple)
            x,y = coord_tuple

            place_in_x = position_x + x
            place_in_y = position_y + y
            #print("Placement",place_in_x,place_in_y)
            self.matrix[place_in_x][place_in_y] = s.value
        print(self.matrix)
    def draw_shape_in(self,s:Shape,position:Tuple[int,int]):
        position_x,position_y = position


    def __str__(self):
        my_string:str = ""
        for elem in self.matrix:
            pass



    def count_empty_cells(self) -> int:
        the_sum = 0
        for row in self.matrix:
            for elem in row:
                if elem == self.empty_cell_char:
                #    print(elem)
                    the_sum += 1

        return the_sum
    def count_filled_cells(self) -> int:
        the_sum = 0
        for row in self.matrix:
            for elem in row:
                if elem != self.empty_cell_char and elem != self.hole_cell_char:
                    #print(elem)
                    the_sum += 1

        return the_sum
    def count_holes(self) -> int:
        the_sum = 0
        for row in self.matrix:
            for elem in row:
                if elem == self.hole_cell_char:
                    #print(elem)
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
                    #print(elem)
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

class manipullator():
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
    def rotate_shape(self, shape: Shape, rotation: int):
        rotated_matrix = []
        for i in shape.get_coords_list():
            rotated_matrix.append(np.dot(i, self.rotation_matrixes[rotation]))

        return rotated_matrix


main()
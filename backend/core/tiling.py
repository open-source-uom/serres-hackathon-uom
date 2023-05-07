import collections
from functools import reduce
import time
import numpy as np
from typing import List, Tuple, Callable, Any
from shape import Shape
from canvas import Canvas
import networkx as nx

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


def run_fn_and_count_time():
    pass

#mporei na mhn xreiastei
class CongruentGroup:
    pass


def main():
                    #  Y X
    my_canvas = Canvas(10,11, [(3,4)])
    # man = manipullator()
    # result1 = my_canvas.count_filled_cells()
    # #print("Filled Cells" ,result1)
    # result2 = my_canvas.count_empty_cells()
    # #print("Empty Cells",result2)
    # result3 = my_canvas.count_holes()
    # #print("Hole Cells",result3)
    s1 = Shape('F')
    s2 = Shape('N')
    # s3 = Shape('T')


    #rotate s1 with manipulator
    #man.rotate_shape(s1,0)
    #print cords of s1
    #print(s1.get_coords_list())
    pos1 = (6,6)
    pos2 = (2,2)
    #Shape.change_cords_by_a_position(s1,pos)
    #print(s1.get_coords_list())

    print(my_canvas.check_for_out_of_bounds_when_placed_in(s1,pos1))                                    # Y X
    my_canvas.place_shape(s1,pos1)
    my_canvas.place_shape(s2, pos2)
    print(my_canvas.get_matrix())





main()
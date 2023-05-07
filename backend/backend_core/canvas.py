import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable, Any
from backend_core.shape import Shape



class Canvas():

    empty_cell_char = '-'
    hole_cell_char = 'B'

    def __init__(self,lines:int,rows:int, holes:List[Tuple[int, int]]):#y:lines,x:rows
        self.dimensions: Tuple[int, int] = (lines, rows)
        self.shapes_placed:List[Shape] = []
        self.holes: List[Tuple[int, int]] = holes
        enough_empty_cells = [self.empty_cell_char for i in range(lines*rows)]
        # den einai swsto auto
        # self.matrix = np.arange(lines * rows).reshape(lines,rows) NOT WORKING
        #self.matrix = np.full((lines,rows),self.empty_cell_char)
        #print("MATRIX OF:",self.matrix)

    # def check_for_stepping_in_hole_when_placed_in(self,s:Shape,position:Tuple[int,int]):
    def check_for_stepping_in_hole_when_placed_in(self, s: Shape, position: Tuple[int, int]):
        position_x, position_y = position
        s.change_cords_by_a_position(position)
        for coords in s.get_coords_list():
            x,y = coords
            if(x, y) in self.holes:
                return False
        # return check
        return True

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

        if min_position_y< 0 or min_position_x < 0 or max_position_x > self.dimensions[0] -1 or max_position_y > self.dimensions[1] - 1:
            return False
        return True

    def place_shape_unchecked(self,s:Shape,position:Tuple[int,int]):
        s.change_cords_by_a_position(position)
        print("Warning unchecked placement")



    def place_shape(self,s:Shape,position:Tuple[int,int]):
        position_x,position_y = position
        coords = s.get_coords_list()
        self.shapes_placed.append(s)
        s.change_cords_by_a_position(position)
    def get_matrix(self):
        matrix = np.full((self.dimensions[0], self.dimensions[1]), self.empty_cell_char)
        for shape in self.shapes_placed:
            coords = shape.get_coords_list()
            for coord_tuple in coords:
                x, y = coord_tuple
                matrix[x][y] = shape.value

        #place the holes in the matrix
        for hole in self.holes:
            hole_x,hole_y = hole
            matrix[hole_x][hole_y] = self.hole_cell_char
        return np.rot90(matrix)

    def __str__(self):
        my_string:str = ""
        matrix = self.get_matrix()
        for rows in matrix:
            for elems in rows:
                my_string += elems
            my_string += " "
        return my_string

    def get_positions_it_will_be_on_pos(self,s:Shape, pos:Tuple[int,int])->List[Tuple[int,int]]:
        potitions:List[Tuple[int, int]] = []
        for i in s.get_coords_list():
            x,y = i
            potitions.append((pos[0]-x,pos[1]-y))
        return potitions

    def count_filled_cells(self) -> int: #not hole or shape
        the_sum = 0
        for i in self.shapes_placed:
            the_sum += len(i.get_coords_list())

        return (the_sum + len(self.holes))

    def count_empty_cells(self) -> int:
        return (self.dimensions[0] * self.dimensions[1]) - self.count_filled_cells()
    def get_all_available_positions(self,s:Shape)->List[Tuple[int,int]]:
        matrix_set = set()
        for row in range(self.dimensions[0]):
            for col in range(self.dimensions[1]):
                matrix_set.add((row, col))
        return matrix_set.difference(set(self.get_all_non_available_positions(s)))

    def get_all_non_available_positions(self,s:Shape)->List[Tuple[int,int]]:
        positions_filled:List[Tuple[int,int]] = []
        for shape in self.shapes_placed:
            for i in shape.get_coords_list():
                positions_filled.append(i)
        for hole in self.holes:
            positions_filled.append(hole)
        positions_filled = list(set(positions_filled))

        positions:List[Tuple[int,int]] = []
        for pos in positions_filled:
            positions += self.get_positions_it_will_be_on_pos(s,pos)

        coords = s.get_coords_list()
        all_x = list(map(lambda coord: coord[0], coords))
        all_x_sorted = sorted(all_x)
        # print(all_x_sorted)
        all_y = list(map(lambda coord: coord[1], coords))
        all_y_sorted = sorted(all_y)
        #print("all_x_sorted",all_x_sorted)
        min_x = all_x_sorted[0]
        min_y = all_y_sorted[0]

        max_x = all_x_sorted[len(all_x_sorted) - 1]
        max_y = all_y_sorted[len(all_y_sorted) - 1]

        for i in range(self.dimensions[0]):
            for j in range(max_y):
                positions.append((i,self.dimensions[1]-j-1))
            for j in range(-min_y):
                positions.append((i,j))

        for i in range(self.dimensions[1]):
            for j in range(max_x):
                #print(self.dimensions[0]-j-1,i)
                positions.append((self.dimensions[0]-j-1,i))
            for j in range(-min_x):
                positions.append((j,i))


        return list(set(positions))

    def get_string_of_matrix(self):
        matrix = self.get_matrix()
        my_string = ""
        for i in matrix:
            for j in i:
                my_string += j
            my_string += " "
        return my_string

    def count_holes(self) -> int:
        return len(self.holes)
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


    def get_all_shapes_coords(self):
        return list(map(lambda shape: shape.get_coords_list(),self.shapes_placed))
    # Calculate Parameter of shape
    def get_placed_shapes(self):
        return self.shapes_placed
    def calculate_parimeter_of_shapes(self,shapes: List[Shape]) -> int:

        # Create a 3x3 cube shape
        shape = []
        for i in shapes:
            shape += i.get_coords_list()

        # Create a graph
        G = nx.Graph()

        # add each poit of the shape to the graph
        for i in shape:
            G.add_node(i)
        # add edges between tow points if they are neighbors
        for i in shape:
            for j in shape:
                if (i[0] == j[0] and abs(i[1] - j[1]) == 1) or (i[1] == j[1] and abs(i[0] - j[0]) == 1):
                    G.add_edge(i, j)

        # show the graph
        # print the number neighbors of each point
        s = 0
        for i in shape:
            s += 4 - len(list(G.neighbors(i)))
        return s
    def get_empty_cells(self)->List[Tuple[int,int]]:
        pass

    def place_hole_in(self,x,y):
        self.holes.append((x,y))
        pass

    def shapes_touch(self,s1:Shape,s2:Shape) -> bool:
        others_coords = s2.get_coords_list()
        for node in s1.nodes:
            x,y = node.get_coords()
            if others_coords == (x - 1, y):
                return True
            if others_coords == (x + 1, y):
                return True
            if others_coords == (x, y - 1):
                return True
            if others_coords == (x, y + 1):
                return True
    def merge_shapes(self,s1:Shape,s2:Shape,new_label:str):
        # this will return a shape that has the coordinates of both
        combined_coords = s1.get_coords_list() + s2.get_coords_list()
        return Shape(new_label,combined_coords)
        # the positions of the nodes are on the canvas so we just create a new shape that has as Nodes both the nodes of s1 and s2

        pass

def main():
    my_canvas = Canvas(12,12,[(0,0),(0,1),(0,2),(0,3),(0,4)])
    # True-> passes the check, False
    checking = my_canvas.check_for_stepping_in_hole_when_placed_in(Shape("F"),(3,3))
    res = my_canvas.count_empty_cells()
    res2 = my_canvas.count_filled_cells()
    print(checking)
    print(res,res2)
#main();
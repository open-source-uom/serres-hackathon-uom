from typing import List, Tuple, Callable, Any
import copy
from shape import Shape
from canvas import Canvas
import networkx as nx
class Dfs():
    def __init__(self, shapes: List[Shape], holes: List[Tuple[int, int]], dimensions: Tuple[int, int]):
        self.shapes: List[Shape] = shapes
        self.holes: List[Tuple[int, int]] = holes
        self.dimensions: Tuple[int, int] = dimensions
        self.tree: nx.Graph = nx.Graph()

class NodeT():

    rotations_dict = {
        "F": [0, 1, 2, 3, 4, 5],
        "I": [0, 1, 0, 1, 0, 0],
        "N": [0, 1, 2, 3, 4, 5],
        "P": [0, 1, 2, 3, 4, 5],
        "T": [0, 1, 2, 3, 0, 5],
        "U": [0, 1, 2, 3, 0, 5],
        "V": [0, 1, 2, 3, 5, 5],
        "W": [0, 1, 2, 3, 4, 5],
        "X": [0, 0, 0, 0, 0, 0],
        "Y": [0, 1, 2, 3, 4, 5],
        "Z": [0, 1, 0, 3, 4, 5],
        "L": [0, 1, 2, 3, 4, 5],
    }

    def __init__(self, shapes_remain: List[ Shape], canvas, rotation_allows: bool = True):
        # List[Node]
        self.shapes_remain = shapes_remain
        self.canvas = canvas
        self.rotation_allows = rotation_allows
        self.children = []

    def get_canvas(self):
        return self.canvas

    def generate_children(self) -> Tuple[Shape, Tuple[int, int]]:
        children: List[NodeT] = []
        childres_placed_shapes = []
        for shape_symbol in self.shapes_remain:
            symbols_remain_instanse = copy.deepcopy(self.shapes_remain)
            symbols_remain_instanse.remove(shape_symbol)
            rotations = copy.deepcopy(self.rotations_dict[shape_symbol])
            rot_made = []
            for rotation in range(6):
                if rotations[rotation] in rot_made:
                    continue
                rot_made.append(rotation)
                shape = Shape(shape_symbol)
                shape.rotate_shape(rotation)
                #print(self.canvas.get_all_available_positions(shape))
                for position in self.canvas.get_all_available_positions(shape):
                    shape = Shape(shape_symbol)
                    shape.rotate_shape(rotation)
                    newCanvas = copy.deepcopy(self.get_canvas())
                    newCanvas.place_shape(shape, position)
                    node_instance = NodeT(symbols_remain_instanse, newCanvas, self.rotation_allows)
                    children.append(node_instance)
                    childres_placed_shapes.append(node_instance.get_canvas().get_placed_shapes())
        return children





def is_solution(current):
    pass

def dfs(symbols: List[str], canvas: Canvas, rotation_allows: bool = True):
    frontier = [NodeT(symbols, canvas, rotation_allows)]
    leafs = []
    while len(frontier) > 0:
        current = frontier.pop()
        children = current.generate_children()
        if len(children) == 0:
            leafs.append(current)
        else:
            for i in children:
                frontier.append(i)
    return leafs

def run():
    # x, y = 15, 15
    #letters = [("F", 3), ("I", 5), ("L", 4), ("N", 4), ("P", 3), ("T", 3), ("U", 2), ("V", 3), ("W", 3), ("X", 3), ("Y", 4), ("Z", 3)]
    # root = NodeT(["T", "F", "I", "Y", "L"], Canvas(5, 5, []))
    # frontier = [root]
    # leafs = []
    # while len(frontier) > 0:
    #     current = frontier.pop()
    #
    #     children = current.generate_children()
    #     if len(children) == 0:
    #         leafs.append(current)
    #     else:
    #         for i in children:
    #             frontier.append(i)
    leafs = dfs(["T", "F", "I", "Y", "L"], Canvas(5, 5, []))
    for i in leafs:
        if i.shapes_remain == []:
            print(i.canvas.get_matrix(), "\n")


run()
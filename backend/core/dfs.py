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
    shapes_that_must_be_used = ["W", "T", "Y", "U", "P", "F", "L", "Z", "X", "V", "N"]

    def __init__(self, shapes_remain: List[ Shape], canvas, rotation_allows: bool = True):
        # List[Node]
        self.shapes_remain = shapes_remain
        self.canvas = canvas
        self.rotation_allows = rotation_allows
        self.children = []

    def generate_children(self) -> Tuple[Shape, Tuple[int, int]]:
        children: List[NodeT] = []
        for shape_symbol in self.shapes_remain:
            symbols_remain_instanse = copy.deepcopy(self.shapes_remain)
            symbols_remain_instanse.remove(shape_symbol)
            for rotation in range(6):
                shape = Shape(shape_symbol)
                shape.rotate_shape(rotation)
                #print(self.canvas.get_all_available_positions(shape))
                for position in self.canvas.get_all_available_positions(shape):
                    shape = Shape(shape_symbol)
                    shape.rotate_shape(rotation)
                    newCanvas = copy.deepcopy(self.canvas)
                    newCanvas.place_shape(shape, position)
                    children.append(NodeT(symbols_remain_instanse, newCanvas, self.rotation_allows))
        return children





def is_solution(current):
    pass

def run():
    x, y = 15, 15
    root = NodeT(["T", "F", "I", "Y", "L"], Canvas(5, 5, []))
    frontier = [root]
    leafs = []
    while len(frontier) > 0:
        current = frontier.pop()

        children = current.generate_children()
        if len(children) == 0:
            leafs.append(current)
        else:
            for i in children:
                frontier.append(i)

    for i in leafs:
        if i.shapes_remain == []:
            print(i.canvas.get_matrix(), "\n")

run()
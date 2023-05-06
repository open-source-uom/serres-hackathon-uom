from typing import Tuple, List, Callable, Any
class Node():
    cords: Tuple[int, int]
    def __init__(self, cords: Tuple[int, int], symbol: str):
        self.cords = cords

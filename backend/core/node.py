from typing import Tuple, List, Callable, Any
class Node():
    def __init__(self, cords: Tuple[int, int], symbol: str):
        self.coords: Tuple[int, int] = cords
        self.symbol: str = symbol
    def get_coords(self) -> Tuple[int, int]:
        return self.coords
    def set_coords(self, coords):
        self.coords = coords
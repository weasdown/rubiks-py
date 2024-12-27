# Simulator for a 3x3 Rubik's Cube

import numpy as np
from enum import Enum

class Direction(Enum):
    """Defines the two possible ways to rotate a side."""
    ANTICLOCKWISE = 0
    CLOCKWISE = 1
    DOUBLE = 2

class ColumnOrRowIndex(Enum):
    """Makes checks of column or row indices more rigorous."""
    FIRST = 0
    SECOND = 1
    THIRD = 2

class CubeOperations(Enum):
    F = 0
    R = 1
    U = 2
    L = 3
    B = 4
    D = 5

class Colour(Enum):
    GREEN = 0
    RED = 1
    WHITE = 2
    ORANGE = 3
    BLUE = 4
    YELLOW = 5

class Cube:
    pass

class Side:
    def __init__(self, colour: Colour, colour_anticlockwise_from_column_1: Colour,
                 colour_clockwise_from_column_1: Colour, colour_left_from_column_1: Colour):
        self.colour: Colour = colour

        self.colour_anticlockwise_from_column_1: Colour = colour_anticlockwise_from_column_1
        self.colour_clockwise_from_column_1: Colour = colour_clockwise_from_column_1
        self.colour_left_from_column_1: Colour = colour_left_from_column_1

        self.matrix: np.ndarray = np.full((3,3), self.colour)

    def rotate(self, direction: Direction):
        pass

    def set_column(self, column_index: ColumnOrRowIndex, new_values_from_side: Direction):
        pass

    def set_row(self, row_index: ColumnOrRowIndex, new_values_from_side: Direction):
        pass

# Simulator for a 3x3 Rubik's Cube

import numpy as np
from enum import Enum

class Direction(Enum):
    """Defines the two possible ways to rotate a side."""
    ANTICLOCKWISE = 0
    CLOCKWISE = 1
    DOUBLE = 2

class RowDirection(Enum):
    LEFT = 0
    RIGHT = 1

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
    ORANGE = 5
    BLUE = 6
    YELLOW = 4

class Cube:
    pass

class Side:
    def __init__(self, colour: Colour, colour_anticlockwise_from_column_1: Colour,
                 colour_clockwise_from_column_1: Colour, colour_left_from_column_1: Colour):
        self.colour: Colour = colour

        self.colour_anticlockwise_from_column_1: Colour = colour_anticlockwise_from_column_1
        self.colour_clockwise_from_column_1: Colour = colour_clockwise_from_column_1
        self.colour_left_from_column_1: Colour = colour_left_from_column_1

        self.matrix: np.ndarray = np.full((3,3), self.colour.value, dtype=int)

    def rotate(self, direction: Direction):
        # Note: np.rot90 rotates anti-clockwise by default.
        rotations: int = -1  # clockwise rotation by default
        match direction:
           case Direction.ANTICLOCKWISE:
               rotations = 1
           case Direction.CLOCKWISE:
               rotations = -1
           case Direction.ANTICLOCKWISE:
               rotations = 2

        self.matrix = np.rot90(self.matrix, rotations)

    def set_column(self, column_index: ColumnOrRowIndex, new_values_from_side: Direction):
        # TODO test this
        self.matrix[:, column_index.value] =  self.colour_clockwise_from_column_1 if \
                new_values_from_side == Direction.CLOCKWISE else self.colour_anticlockwise_from_column_1

    def set_row(self, row_index: ColumnOrRowIndex, new_values_from_side: RowDirection):
        if new_values_from_side == RowDirection.LEFT:
            self.matrix[row_index.value, :] = self.colour_left_from_column_1.value
        else:
            # Use that Colour values have been defined so opposite sides on the Cube add to 6.
            self.matrix[row_index.value, :] = 6 - self.colour_left_from_column_1.value

green = Side(Colour.GREEN, Colour.WHITE, Colour.YELLOW, Colour.ORANGE)
print(green.matrix)

green.set_row(ColumnOrRowIndex.FIRST, RowDirection.LEFT)
print(green.matrix)

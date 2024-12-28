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
    # TODO add functions to return adjacent colours (like with Dart enums)
    GREEN = 0
    RED = 1
    WHITE = 2
    ORANGE = 5
    BLUE = 6
    YELLOW = 4

class Cube:
    def __init__(self):
        self.green: Side = Side(Colour.GREEN, Colour.WHITE, Colour.ORANGE)
        self.red: Side = Side(Colour.RED, Colour.WHITE, Colour.GREEN)
        self.white: Side = Side(Colour.WHITE, Colour.BLUE, Colour.ORANGE)
        self.orange: Side = Side(Colour.ORANGE, Colour.WHITE, Colour.BLUE)
        self.blue: Side = Side(Colour.BLUE, Colour.WHITE, Colour.RED)
        self.yellow: Side = Side(Colour.YELLOW, Colour.GREEN, Colour.ORANGE)

        self.sides: list[Side] = [self.green, self.red, self.white, self.orange, self.blue, self.yellow]

class Side:
    def __init__(self, colour: Colour, colour_above_column_1: Colour, colour_left_from_column_1: Colour):
        self.colour: Colour = colour

        self.colour_above_column_1: Colour = colour_above_column_1
        self.colour_below_column_1: Colour = Colour(6 - self.colour_above_column_1.value)
        self.colour_left_from_column_1: Colour = colour_left_from_column_1
        self.colour_right_from_column_1: Colour = Colour(6 - self.colour_left_from_column_1.value)

        self.matrix: np.ndarray = np.full((3,3), self.colour.value, dtype=int)

    def __str__(self):
        return self.matrix_string

    @property
    def matrix_string(self):
        """Gets a neater version of self.matrix that shows the name of the Colour in each cell."""
        matrix = np.full((3,3), '', dtype=np.dtype('U6'))
        for row_index, row in enumerate(self.matrix):
            for column_index, value in enumerate(row):
                matrix[row_index, column_index] = Colour(value).name

        matrix = str(matrix)[1:-1]  # convert to string, remove the extra leading and trailing square brackets
        return matrix

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
        self.matrix[:, column_index.value] =  self.colour_below_column_1 if \
                new_values_from_side == Direction.CLOCKWISE else self.colour_above_column_1

    def set_row(self, row_index: ColumnOrRowIndex, new_values_from_side: RowDirection):
        if new_values_from_side == RowDirection.LEFT:
            self.matrix[row_index.value, :] = self.colour_left_from_column_1.value
        else:
            # Use that Colour values have been defined so opposite sides on the Cube add to 6.
            self.matrix[row_index.value, :] = 6 - self.colour_left_from_column_1.value

cube = Cube()
# green = Side(Colour.GREEN, Colour.WHITE, Colour.YELLOW, Colour.ORANGE)
print(cube.green)

cube.green.set_row(ColumnOrRowIndex.FIRST, RowDirection.LEFT)
print(cube.green.matrix_string)

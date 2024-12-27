# Rubik's Cube simulator

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


class Cube:
    pass

class Side:
    def __init__(self):
        pass

    def rotate(self, direction: Direction):
        pass

    def set_column(self, column_index: ColumnOrRowIndex, new_values_from_side: Direction):
        pass

    def set_row(self, row_index: ColumnOrRowIndex, new_values_from_side: Direction):
        pass

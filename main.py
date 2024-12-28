# Simulator for a 3x3 Rubik's Cube

import numpy as np
from enum import Enum

class Direction(Enum):
    """Defines the two possible ways to rotate a side."""
    ANTICLOCKWISE = 0
    CLOCKWISE = 1
    OPPOSITE = 2

class VerticalDirection(Enum):
    TOP = 0
    BOTTOM = 1
    OPPOSITE = 2

class HorizontalDirection(Enum):
    LEFT = 0
    RIGHT = 1
    OPPOSITE = 2

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
        """
        Default cube orientation has:

        - Yellow on U face
        - Blue on F face
        - Orange on L face

        The Blue side is therefore the centre of the net that defines which cells are rows or columns on each side.
        """
        self.green: _Side = _Side(Colour.GREEN, Colour.WHITE, Colour.ORANGE)
        self.red: _Side = _Side(Colour.RED, Colour.YELLOW, Colour.BLUE)
        self.white: _Side = _Side(Colour.WHITE, Colour.BLUE, Colour.ORANGE)
        self.orange: _Side = _Side(Colour.ORANGE, Colour.YELLOW, Colour.GREEN)
        self.blue: _Side = _Side(Colour.BLUE, Colour.YELLOW, Colour.ORANGE)
        self.yellow: _Side = _Side(Colour.YELLOW, Colour.GREEN, Colour.ORANGE)

        self.sides: list[_Side] = [self.green, self.red, self.white, self.orange, self.blue, self.yellow]

    def F(self, quarter_turns: int = 1):
        """Rotate the Blue side.

        Unaffected side: Green.
        """
        # raise NotImplementedError  # TODO remove error once tested
        match quarter_turns:
            case 1:
                self.blue.rotate(Direction.CLOCKWISE)
                self.yellow.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.LEFT)
                self.white.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.RIGHT)
                self.red.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.TOP)
                self.orange.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.BOTTOM)

            case -1:
                self.blue.rotate(Direction.ANTICLOCKWISE)
                self.yellow.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.RIGHT)
                self.white.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.LEFT)
                self.red.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.BOTTOM)
                self.orange.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.TOP)

            case 2:
                self.blue.rotate(Direction.OPPOSITE)
                self.yellow.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.OPPOSITE)
                self.white.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.OPPOSITE)
                self.red.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.OPPOSITE)
                self.orange.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.OPPOSITE)

    def R(self, quarter_turns: int = 1):
        """Rotate the Red side.

        Unaffected side: Orange.
        """
        # raise NotImplementedError  # TODO remove error once tested
        match quarter_turns:
            case 1:
                self.red.rotate(Direction.CLOCKWISE)
                self.blue.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.BOTTOM)
                self.yellow.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.BOTTOM)
                self.white.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.BOTTOM)
                self.green.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.BOTTOM)

            case -1:
                self.red.rotate(Direction.ANTICLOCKWISE)
                self.blue.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.TOP)
                self.yellow.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.TOP)
                self.white.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.TOP)
                self.green.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.TOP)

            case 2:
                self.red.rotate(Direction.OPPOSITE)
                self.blue.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.OPPOSITE)
                self.yellow.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.OPPOSITE)
                self.white.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.OPPOSITE)
                self.green.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.OPPOSITE)

    def U(self, quarter_turns: int = 1):
        """Rotate the Yellow side.

        Unaffected side: White.
        """
        # raise NotImplementedError  # TODO remove error once tested
        match quarter_turns:
            case 1:
                self.yellow.rotate(Direction.CLOCKWISE)
                self.blue.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.RIGHT)
                self.orange.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.RIGHT)
                self.red.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.RIGHT)
                self.green.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.LEFT)

            case -1:
                self.yellow.rotate(Direction.ANTICLOCKWISE)
                self.blue.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.LEFT)
                self.orange.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.LEFT)
                self.red.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.LEFT)
                self.green.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.RIGHT)

            case 2:
                self.yellow.rotate(Direction.OPPOSITE)
                self.blue.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.OPPOSITE)
                self.orange.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.OPPOSITE)
                self.red.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.OPPOSITE)
                self.green.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.OPPOSITE)

    def L(self, quarter_turns: int = 1):
        """Rotate the Orange side.

        Unaffected side: Red.
        """
        # raise NotImplementedError  # TODO remove error once tested
        match quarter_turns:
            case 1:
                self.orange.rotate(Direction.CLOCKWISE)
                self.blue.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.TOP)
                self.yellow.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.TOP)
                self.white.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.TOP)
                self.green.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.TOP)

            case -1:
                self.orange.rotate(Direction.ANTICLOCKWISE)
                self.blue.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.BOTTOM)
                self.yellow.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.BOTTOM)
                self.white.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.BOTTOM)
                self.green.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.BOTTOM)

            case 2:
                self.orange.rotate(Direction.OPPOSITE)
                self.blue.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.OPPOSITE)
                self.yellow.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.OPPOSITE)
                self.white.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.OPPOSITE)
                self.green.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.OPPOSITE)

    def B(self, quarter_turns: int = 1):
        """Rotate the Green side.

        Unaffected side: Blue.
        """
        # TODO update to new UFL
        # raise NotImplementedError  # TODO remove error once tested
        match quarter_turns:
            case 1:
                self.green.rotate(Direction.CLOCKWISE)
                self.yellow.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.RIGHT)
                self.white.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.LEFT)
                self.red.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.BOTTOM)
                self.orange.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.TOP)

            case -1:
                self.green.rotate(Direction.ANTICLOCKWISE)
                self.yellow.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.LEFT)
                self.white.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.RIGHT)
                self.red.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.TOP)
                self.orange.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.BOTTOM)

            case 2:
                self.green.rotate(Direction.OPPOSITE)
                self.yellow.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.OPPOSITE)
                self.white.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.OPPOSITE)
                self.red.set_column(ColumnOrRowIndex.THIRD, VerticalDirection.OPPOSITE)
                self.orange.set_column(ColumnOrRowIndex.FIRST, VerticalDirection.OPPOSITE)

    def D(self, quarter_turns: int = 1):
        """Rotate the White side.

        Unaffected side: Yellow.
        """
        # raise NotImplementedError  # TODO remove error once tested
        match quarter_turns:
            case 1:
                self.white.rotate(Direction.CLOCKWISE)
                self.blue.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.LEFT)
                self.orange.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.LEFT)
                self.red.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.LEFT)
                self.green.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.RIGHT)

            case -1:
                self.white.rotate(Direction.ANTICLOCKWISE)
                self.blue.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.RIGHT)
                self.orange.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.RIGHT)
                self.red.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.RIGHT)
                self.green.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.LEFT)

            case 2:
                self.white.rotate(Direction.OPPOSITE)
                self.blue.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.OPPOSITE)
                self.orange.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.OPPOSITE)
                self.red.set_row(ColumnOrRowIndex.THIRD, HorizontalDirection.OPPOSITE)
                self.green.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.OPPOSITE)

class _Side:
    def __init__(self, colour: Colour, colour_above_column_1: Colour, colour_left_from_column_1: Colour):
        self.colour: Colour = colour

        self.colour_above: Colour = colour_above_column_1
        self.colour_below: Colour = Colour(6 - self.colour_above.value)
        self.colour_left: Colour = colour_left_from_column_1
        self.colour_right: Colour = Colour(6 - self.colour_left.value)
        self.colour_opposite: Colour = Colour(6 - self.colour.value)

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

    def set_column(self, column_index: ColumnOrRowIndex, new_values_from_side: VerticalDirection):
        # TODO test set_column
        new_value: int = self.colour.value
        match new_values_from_side:
            case VerticalDirection.TOP:
                new_value = self.colour_above.value
            case VerticalDirection.BOTTOM:
                new_value = self.colour_below.value
            case VerticalDirection.OPPOSITE:
                new_value = new_value = self.colour_opposite.value

        self.matrix[:, column_index.value] =  new_value

    def set_row(self, row_index: ColumnOrRowIndex, new_values_from_side: HorizontalDirection):
        # TODO remove old implementation
        # if new_values_from_side == HorizontalDirection.LEFT:
        #     self.matrix[row_index.value, :] = self.colour_left_from_column_1.value
        # else:
        #     # Use that Colour values have been defined so opposite sides on the Cube add to 6.
        #     self.matrix[row_index.value, :] = 6 - self.colour_left_from_column_1.value

        # TODO test set_row
        new_value: int = self.colour.value
        match new_values_from_side:
            case HorizontalDirection.LEFT:
                new_value = self.colour_left.value
            case HorizontalDirection.RIGHT:
                new_value = self.colour_right.value
            case HorizontalDirection.OPPOSITE:
                new_value = self.colour_opposite.value
        self.matrix[row_index.value, :] = new_value

cube = Cube()
# print(cube.green)
#
cube.F()
# cube.green.set_row(ColumnOrRowIndex.FIRST, HorizontalDirection.LEFT)
# print(cube.green.matrix_string)
print(cube.red.matrix_string)

# Core classes for the Rubik's Cube simulator.

from enum import Enum
import numpy as np

class Colour(Enum):
    # TODO add functions to return adjacent colours (like with Dart enums)
    GREEN = 0
    RED = 1
    WHITE = 2
    ORANGE = 5
    BLUE = 6
    YELLOW = 4

class _Side:
    def __init__(self, colour: Colour):
        self.colour: Colour = colour
        self.name: str = colour.name.title()

        self.matrix: np.ndarray = np.full((3, 3), self.colour.value, dtype=int)

    def __repr__(self):
        return f'{self.name} Side'

class RotationDirection(Enum):
    """Defines the two possible ways to rotate a side."""
    ANTICLOCKWISE = 0
    CLOCKWISE = 1

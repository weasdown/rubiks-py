# Core classes for the Rubik's Cube simulator.

from __future__ import annotations

from enum import Enum
from dataclasses import dataclass
import numpy as np

# from rubik_nx import Cube

# class Slide:
#     def __init__(self, name: str, value: int):
#         self.name: str = name
#         self.value: int = value

@dataclass
class _Colour:
    name: str
    value: int
    hex: int

class Colour(Enum):
    # TODO add functions to return adjacent colours (like with Dart enums)
    GREEN = _Colour('Green', 0, int('0x00FF00', 0))
    RED = _Colour('Red', 1, int('0xFF0000', 0))
    WHITE = _Colour('White', 2, int('0xFFFFFF', 0))
    ORANGE = _Colour('Orange', 3, int('0xFFA500', 0))
    BLUE = _Colour('Blue', 4, int('0x0000FF', 0))
    YELLOW = _Colour('Yellow', 5, int('0xFFFF00', 0))

    # def __init__(self, name: str, value: int):
    #     self.name: str = name
    #     self.value: int = value

class RotationDirection(Enum):
    """Defines the two possible ways to rotate a side."""
    ANTICLOCKWISE = 0
    CLOCKWISE = 1

# Core classes for the Rubik's Cube simulator.

from __future__ import annotations

from enum import Enum
from dataclasses import dataclass

@dataclass
class _Colour:
    name: str
    value: int
    hex: int

class Colour(Enum):
    GREEN = _Colour('Green', 1, int('0x00FF00', 0))
    RED = _Colour('Red', 2, int('0xFF0000', 0))
    WHITE = _Colour('White', 4, int('0xFFFFFF', 0))
    ORANGE = _Colour('Orange', 8, int('0xFFA500', 0))
    BLUE = _Colour('Blue', 16, int('0x0000FF', 0))
    YELLOW = _Colour('Yellow', 32, int('0xFFFF00', 0))

    @staticmethod
    def name_from_value(value: int):
        return [colour_item.value.name for colour_item in Colour if colour_item.value.value == value][0]

class RotationDirection(Enum):
    """Defines the two possible ways to rotate a side."""
    ANTICLOCKWISE = 0
    CLOCKWISE = 1

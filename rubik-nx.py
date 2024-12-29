# A 3x3 Rubik's Cube simulator that represents the Cube as a set of networkx graphs.

from core import _Side, Colour, RotationDirection
import networkx as nx
import numpy as np

class Ring:
    def __init__(self, cut_sides: list[_Side]):
        self.cut_sides: list[_Side] = cut_sides

class InnerRing(Ring):
    def __init__(self, cut_sides: list[_Side]):
        super().__init__(cut_sides)

class OuterRing(Ring):
    def __init__(self, planar_side: _Side, edge_sides: list[_Side]):
        self.planar_side: _Side = planar_side
        self.edge_sides: list[_Side] = edge_sides
        super().__init__(self.edge_sides)

class Cube:
    blue: _Side = _Side(Colour.BLUE)
    yellow: _Side = _Side(Colour.YELLOW)
    white: _Side = _Side(Colour.WHITE)
    orange: _Side = _Side(Colour.ORANGE)
    red: _Side = _Side(Colour.RED)
    green: _Side = _Side(Colour.GREEN)

    sides: list[_Side] = [blue, yellow, white, orange, red, green]

    def __init__(self):
        pass


G = nx.Graph()
G.add_nodes_from(Cube.sides)

print(list(G.nodes))

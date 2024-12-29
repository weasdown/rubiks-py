# A 3x3 Rubik's Cube simulator that represents the Cube as a set of networkx graphs.

from __future__ import annotations

from core import Colour, RotationDirection

import networkx as nx
import numpy as np

# class Ring:
#     def __init__(self, cut_sides: list[_Side]):
#         self.cut_sides: list[_Side] = cut_sides
#
# class InnerRing(Ring):
#     def __init__(self, cut_sides: list[_Side]):
#         super().__init__(cut_sides)
#
# class OuterRing(Ring):
#     def __init__(self, planar_side: _Side, edge_sides: list[_Side]):
#         self.planar_side: _Side = planar_side
#         self.edge_sides: list[_Side] = edge_sides
#         super().__init__(self.edge_sides)

class Cube:
    def __init__(self):
        self.blue: _Side = _Side(Colour.BLUE.value, self)
        self.yellow: _Side = _Side(Colour.YELLOW.value, self)
        self.white: _Side = _Side(Colour.WHITE.value, self)
        self.orange: _Side = _Side(Colour.ORANGE.value, self)
        self.red: _Side = _Side(Colour.RED.value, self)
        self.green: _Side = _Side(Colour.GREEN.value, self)

        self.sides: list[_Side] = [self.blue, self.yellow, self.white, self.orange, self.red, self.green]

        self.graph: nx.Graph = self.build_graph()

        self.ring_yellow_red: list[np.ndarray] = [self.yellow.matrix, np.rot90(self.red.matrix, -1), np.rot90(self.white.matrix, -2), np.rot90(self.orange.matrix, 1),]

    def build_graph(self) -> nx.Graph:
        g = nx.Graph()
        g.add_nodes_from(self.sides)

        # Blue side connections
        g.add_edges_from(
            [(self.blue, self.orange), (self.blue, self.yellow), (self.blue, self.red), (self.blue, self.white), ])

        # Yellow side connections
        g.add_edges_from([(self.yellow, self.orange), (self.yellow, self.green), (self.yellow, self.red), ])

        # Orange side connections
        g.add_edges_from([(self.orange, self.green), (self.orange, self.white), ])

        # Red side connections
        g.add_edges_from([(self.red, self.green), (self.red, self.white), ])

        # Green side connections
        g.add_edges_from([(self.green, self.white), ])

        return g

    def F(self):
        # print(self.blue.neighbours_text)

        neighbours: list[_Side] = self.blue.neighbours.copy()
        for index, neighbour in enumerate(neighbours):
            if index != 0:
                new_matrix = neighbours[index - 1].matrix[0, :]
                neighbour.matrix[:, 0] = new_matrix
            else:
                new_matrix = neighbours[len(neighbours) - 1].matrix[0, :]
                neighbour.matrix[:, 2] = new_matrix

            print(f'New matrix for {neighbour}:\n'
                  f'{neighbour.matrix_string}\n')

class _Side:
    def __init__(self, colour: Colour, parent_cube: Cube):
        self.colour: Colour = colour
        self.name: str = colour.name.title()

        self.cube: Cube = parent_cube

        self.matrix: np.ndarray = np.full((3, 3), self.colour.value, dtype=int)

    def __repr__(self):
        return f'{self.name} Side'

    @property
    def matrix_string(self):
        """Gets a neater version of self.matrix that shows the name of the Colour in each cell."""
        matrix = np.full((3, 3), '', dtype=np.dtype('U6'))
        for row_index, row in enumerate(self.matrix):
            for column_index, value in enumerate(row):
                colour_name = Colour.name_from_value(value)
                matrix[row_index, column_index] = colour_name

        matrix = str(matrix)[1:-1]  # convert to string, remove the extra leading and trailing square brackets
        return matrix

    @property
    def neighbours(self) -> list[_Side]:
         return [neighbour for neighbour in self.cube.graph.adj[
            list(self.cube.graph.nodes)[self.cube.sides.index(self)]]]

    @property
    def neighbours_text(self) -> str:
        text = f'Neighbours for {self}:'
        for neighbour in self.neighbours:
            text += f'\n\t- {neighbour}'

        text += '\n'
        return text

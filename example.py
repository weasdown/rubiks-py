# Example of simulating a 3x3 Rubik's Cube.

from rubik_nx import Cube

# import matplotlib.pyplot as plt

cube = Cube()

cube.F()

# G = cube.graph
# print(f'Nodes: {list(G.nodes)}')
# print(f'Edges: {list(G.edges)}')
#
# options = {
#     # 'node_color': 'black',
#     # 'node_color': [hex(node.colour.hex) for node in list(G.nodes)],
#     'node_size': 100,
#     'with_labels': True
#     # 'width': 3,
# }
# # nx.draw_circular(G, **options)
# # nx.draw_spectral(G, **options)
# nx.draw_spring(G, **options)
#
# # plt.show()
#
# print(f'{list(G.nodes)[1]}: {G.adj[list(G.nodes)[1]]}')
#
# # print(G.adjacency())

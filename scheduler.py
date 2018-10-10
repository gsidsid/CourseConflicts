from graph import Graph
from registrar import Registrar

import networkx as nx

R = Registrar()
G = Graph()
node_colors = []

def color_graph_builtin(g):
    nxGraph = g.G
    d = nx.greedy_color(nxGraph, strategy='independent_set')
    print(d)
    used = []
    color_map = R.slotMappings.values()
    color_idx = -1
    for class_item in d:
        node_colors.append(color_map[d[class_item]])
    return node_colors


def color_graph(g):
    # TODO: Define course book further, implement graph coloring algorithm
    pass


G.build_graph(R.course_book)
G.color_map = color_graph_builtin(G)
G.visualize()
G.export_graph()
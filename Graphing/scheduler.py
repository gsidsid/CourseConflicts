from graph import Graph
from registrar import Registrar

import networkx as nx

R = Registrar()
G = Graph()

def color_graph_test(g):
    d = nx.greedy_color(g.G, strategy='independent_set')
    print(d)
    for course in R.course_book:
        g.color_vertex(course,R.slotMappings[str(d[course])])

def color_graph(g):
    # TODO: Define course book further, implement graph coloring algorithm
    pass


G.build_graph(R.course_book)
color_graph_test(G)
G.visualize()
G.export_graph()
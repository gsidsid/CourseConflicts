from graph import Graph
from registrar import Registrar

import networkx as nx

R = Registrar()
G = Graph()
node_colors = []

def slot_overlap(s,l):
    len_s = len(s)
    return any(s == l[i:len_s+i] for i in xrange(len(l) - len_s+1))

def color_graph_builtin(g):
	nxGraph = g.G
	d = nx.greedy_color(nxGraph,strategy='independent_set')
	print(d)
	used = []
	color_map = R.slotMappings.values()
	color_idx = -1
	for class_item in d:
		node_colors.append(color_map[d[class_item]])
	print(node_colors)

def build_offering_graph(G,course_book):
	for course in course_book:
		G.add_node(course)
		_node_labels = list(G.get_nodes())
		slots = course_book[course]
		for label in _node_labels:
			if slot_overlap(slots,course_book[label]):
				G.add_edge(course,label)

build_offering_graph(G,R.course_book)
color_graph_builtin(G)
G.visualize(node_colors)


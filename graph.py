import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Graph(object):
	G = nx.Graph()
	maxClassCap = 6
	semester_idx = 1

	def __init__(self,semester=1):
		self.semester = semester

	def visualize(self,colors):
		pos = nx.circular_layout(self.G)
		nx.draw(self.G, pos, font_size=16, node_color=colors, with_labels=False)
		for p in pos:  # raise text positions
		    pos[p][1] += 0.07
		nx.draw_networkx_labels(self.G, pos)
		plt.show()

	def add_node(self,offering):
		self.G.add_node(offering)

	def get_nodes(self):
		return (self.G.nodes)

	def add_edge(self,offering1,offering2):
		self.G.add_edge(offering1, offering2)

	def get_edges(self):
		return list(self.G.edges)

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class Graph(object):
    G = nx.Graph()
    maxClassCap = 6
    semester_idx = 1

    def __init__(self, semester=1):
        self.semester = semester

    def visualize(self, colors):
        pos = nx.circular_layout(self.G)
        nx.draw(
            self.G,
            pos,
            font_size=16,
            node_color=colors,
            with_labels=False)
        for p in pos:  # raise text positions
            pos[p][1] += 0.07
        nx.draw_networkx_labels(self.G, pos)
        plt.show()

    def add_node(self, offering):
        self.G.add_node(offering)

    def get_nodes(self):
        return (self.G.nodes)

    def add_edge(self, offering1, offering2):
        self.G.add_edge(offering1, offering2)

    def get_edges(self):
        return list(self.G.edges)

    def slot_overlap(self, s, l):
        len_s = len(s)
        return any(s == l[i:len_s + i] for i in xrange(len(l) - len_s + 1))

    def build_graph(self, course_book):
        for course in course_book:
            self.add_node(course)
            _node_labels = list(self.get_nodes())
            slots = course_book[course]
            for label in _node_labels:
                if self.slot_overlap(slots, course_book[label]):
                    self.add_edge(course, label)

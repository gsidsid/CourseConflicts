from Graphing.graph import Graph
from Graphing.registrar import Registrar
from Coloring.color_backtrack import color_graph

R = Registrar()
G = Graph()

G.build_graph(R.course_book)
color_graph(G)
G.visualize()
G.export_graph()
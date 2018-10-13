import json

import flask
import networkx as nx
from networkx.readwrite import json_graph

app = flask.Flask(__name__)

with open('static/graph.json') as f:
    graph = json.load(f)

nodes = graph["nodes"]
print(nodes)
links = graph["links"]
print(links)

@app.route('/')
def serve():
    return flask.render_template("index.html", nodes=nodes, links=links)

print('\n http://localhost:3029/ \n')
app.run(debug=True,port=3029)
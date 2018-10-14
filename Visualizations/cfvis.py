from networkx.readwrite import json_graph

import json
import flask
import networkx as nx
import os

with open('Visualizations/static/graph.json') as f:
    graph = json.load(f)
nodes = graph["nodes"]
links = graph["links"]

port = int(os.environ.get('PORT', 5000))
app = flask.Flask(__name__)

@app.route('/')
def serve():
    return flask.render_template("index.html", nodes=nodes, links=links)

@app.route('/index.html')
def returnHome():
    return flask.render_template("index.html", nodes=nodes, links=links)

@app.route('/how.html')
def how():
    return flask.render_template("how.html")

@app.route('/about.html')
def about():
    return flask.render_template("about.html")

if __name__ == '__main__':
    print('\n When2Discrete deployment complete. \n')
    app.run(host='0.0.0.0',port=port)

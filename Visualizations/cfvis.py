import json

import flask
import networkx as nx
from networkx.readwrite import json_graph

app = flask.Flask(__name__, static_folder="Web")

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

print('\n http://localhost:2019/index.html \n')
app.run(debug=True,port=2019)
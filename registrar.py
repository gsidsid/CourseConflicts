import json

class Registrar(object):

    course_book = json.loads(open('course_book.json').read())

    slotMappings = {
        "MT900": "red",
        "MT1050": "blue",
        "MT1330": "green",
        "MT1520": "yellow",
        "TF900": "purple",
        "TF1050": "pink",
        "TF1330": "brown",
        "TF1520": "orange"
    }

    def __init__(self):
        pass

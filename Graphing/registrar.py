import json

class Registrar(object):

    course_book = json.loads(open('Courses/course_book.json').read())

    slotMappings = {
        "0": "#0074D9",
        "1": "#001f3f",
        "2": "#85144b",
        "3": "#F012BE",
        "4": "#FF851B",
        "5": "#3D9970",
        "6": "#2ECC40"
    }

    def __init__(self):
        pass

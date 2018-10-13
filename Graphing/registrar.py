import json

class Registrar(object):

    course_book = json.loads(open('../Courses/course_book.json').read())

    slotMappings = {
        "0": "red",
        "1": "blue",
        "2": "green",
        "3": "purple",
        "4": "pink",
        "5": "brown",
        "6": "orange"
    }

    def __init__(self):
        pass

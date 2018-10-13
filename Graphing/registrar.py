import json

class Registrar(object):

    course_book = json.loads(open('../Courses/course_book.json').read())

    slotMappings = {
        "0": "PowderBlue",
        "1": "DarkSeaGreen",
        "2": "LightSeaGreen",
        "3": "DarkCyan",
        "4": "CadetBlue",
        "5": "SteelBlue",
        "6": "DodgerBlue"
    }

    def __init__(self):
        pass

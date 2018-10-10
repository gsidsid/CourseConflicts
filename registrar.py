
class Registrar(object):

    course_book = {
        "Discrete": ["MT900", "MT1040"],
        "Bayesian": ["TF900", "TF1040"],
        "CompArch": ["TF1300"],
        "CompBayes": ["TF1300"],
        "LinII": ["TF1300"],
        "QEAII": ["MT1300"],
        "PoE": ["TF900", "TF1040"]
    }

    slotMappings = {
        "MT900": "red",
        "MT1040": "blue",
        "MT1300": "green",
        "MT1510": "yellow",
        "TF900": "purple",
        "TF1040": "pink",
        "TF1300": "brown",
        "TF1510": "orange"
    }

    def __init__(self):
        pass

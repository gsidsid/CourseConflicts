
class Registrar(object):

    course_book = {
    	"DesNat":["MT900"],
    	"ISIM":["TF900","TF1050","TF1330"],
        "Discrete": ["MT900", "MT1050"],
        "Bayesian": ["TF900", "TF1050"],
        "CompArch": ["TF1050"],
        "CompBayes": ["TF1330"],
        "CompRobo": ["TF1330"],
        "LinII": ["TF1330"],
        "QEAII": ["MT1330"],
        "PoE": ["TF900", "TF1050"],
        "Dynamics": ["TF900"],
        "SoftDes": ["MT1050"],
        "UoCD": ["MT900"],
        "Transport": ["MT1050"]
    }

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

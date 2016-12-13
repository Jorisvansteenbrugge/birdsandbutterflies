class Species():
    def __init__(self, name):
        if type(name) == str:
            self.name = name
            self.observations = []
        elif type(name) == dict:
            self.load(name)

    def load(self, obj):
        self.name = obj["name"]
        self.observations = []

        for obs in obj["observations"]:
            o = Observarion(obs)
            self.observations.append(o)

    def addObservation(self, observ):
        self.observations.append(observ)
    
   
    def toDic(self):
        obsv = [x.toDic() for x in self.observations]
        return {"name": self.name,
                "observations": obsv
               }

class Observation():
    def __init__(self,coords):
        if type(coords) == tuple:
            self.longti = coords[0]
            self.lati   = coords[1]
        elif type(coords) == dict: 
            self.load(coords)

    def load(self, obj):
        self.longti = obj["longti"]
        self.lati   = obj["lati"]

    def toDic(self):
        return {"longti": self.longti,
                "lati": self.lati
                }

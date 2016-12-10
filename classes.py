class Species():
    def __init__(self, name):
        self.name = name
        self.observations = []
        
    def addObservation(self, observ):
        self.observations.append(observ)
    
    
class Observation():
    def __init__(self, activity,longti, lati):
        self.activity = activity
        self.longti = longti
        self.lati = lati
    
    def __str__(self):
        return "observatio"
    
    def __repr__(self):
        return "observation"
    

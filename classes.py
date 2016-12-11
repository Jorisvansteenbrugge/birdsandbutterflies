from pyspark.mllib.linalg import SparseVector

class Species():
    def __init__(self, name):
        self.name = name
        self.observations = []
        
    def addObservation(self, observ):
        self.observations.append(observ)
    
    def getVectorRDD(self):
	return [x.toSparseVector() for x in self.observations]
   
class Observation():
    def __init__(self,longti, lati):
        self.longti = longti
        self.lati = lati
    
    def __str__(self):
        return "observatio"
    
    def __repr__(self):
        return "observation"

    def toSparseVector(self):
        return SparseVector(2, [[0, self.longti], [1, self.lati]])    

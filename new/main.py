from mongo import MongoHandler
from species import Species
import sys

dbController = MongoHandler(True)#true means birds


def parseFile(fileName):
    with open(fileName) as in_file:
        for line in in_file:
            line = line.strip().split(',')
            spec = Species(line[0])
            insertSpecies(spec)
            

def insertSpecies(species):
    dbController.addSpecies(species.toDic())

def testInsert():
    dbController.addSpecies(Species("Joriss").toDic())    

def testReplace():
    dbController.collection.replace_one({"name": "Joriss"},
                                    {"name":"Sjaak"})

if __name__ == "__main__":
    #testInsert()
    testReplace()
    parseFile(sys.argv[1])    

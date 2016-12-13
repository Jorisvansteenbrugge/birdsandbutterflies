#!/usr/bin/env python

from pymongo import MongoClient
from pymongo.son_manipulator import SONManipulator
from species import Species
from bson.binary import Binary


class MongoHandler():
    def __init__(self, birds):
        """Establish a connection with the database server
            and switch to the right database and collection.
        """
        self.client = MongoClient()
        if birds:
            self.db = self.client.birds
        else:
            self.db = self.client.butterflies
        self.collection = self.db.species

    def addSpecies(self, specie):
        self.collection.insert(specie)

    def bulkInsert(self, species):
        self.collection.insert_many(species)


    def addObs(self, species_name_observation)
        self.collection.rep

    def close(self):
        self.client.close()


dbController = MongoHandler(True) 

#spec = Species("Joriss")
#dbController.addSpecies(spec.toDic())

result =  dbController.collection.find_one({"name":"Joriss"})
print(result)

dbController.collection.replace_one({"name": "Joriss"},
                                    {"name":"Sjaak"})

print dbController.collection.find_one()

dbController.close()

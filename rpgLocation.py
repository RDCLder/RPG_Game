# Module:  Location class definitions.

#-------------------------------------------------------------------------------------#

# Initialize

from random import randint
from random import choice
from rpgCharacter import *

adventurer = Character("Hero", "warrior", "player", 1, 1, 1, 1)

#-------------------------------------------------------------------------------------#

# Location Class

class Location:

    def __init__(self, name, enemies, travelLocations):

        self.name = name
    
    def __str__(self):
        return self.name
# Main File.  Run this file to play the RPG.

#-------------------------------------------------------------------------------------#

# Initialize

from random import randint
from random import choice
from rpgCharacter import *
from rpgGameplay import *

#-------------------------------------------------------------------------------------#

# Character creation

yourName = input("What is your name, adventurer?\n")
print(f"Welcome, {yourName}, what is your class?\n" + "-" * 20)
print("1. Warrior: Gifted with overwhelming strength and steadfast endurance.")
print("2. Assassin: Gifted with blinding speed and deadly skill.")
print("3. Mage: Gifted with arcane knowledge and mystical powers.")
print("-" * 20)
chooseClass = 0

while chooseClass == 0:
    yourClass = input("Choose an option (1-3):\n")
    if yourClass not in ("1", "2", "3"):
        print("Please make a valid selection")
    else:
        if yourClass == "1":
            adventurer = Character(yourName, "warrior", "player", 5, 5, 3, 3)
        elif yourClass == "2":
            adventurer = Character(yourName, "assassin", "player", 2, 3, 6, 4)
        else:
            adventurer = Character(yourName, "mage", "player", 1, 2, 3, 8)
        
        chooseClass = 1

#-------------------------------------------------------------------------------------#

# Main program

idle("Town")

#-------------------------------------------------------------------------------------#
# Module:  Gameplay mechanics definitions.

#-------------------------------------------------------------------------------------#

# Initialize

from random import randint
from random import choice
from rpgCharacter import *

adventurer = Character("Hero", "warrior", "player", 1, 1, 1, 1)

#-------------------------------------------------------------------------------------#

# World Map

worldMap = {
    "Town": (("Forest", "S"), ("Graveyard", "SW")),
    "Forest": (("Town", "N"), ("Graveyard", "W"), ("Cave", "E"), (("Abandoned Village", "S")), 
        ("Ancient Forest", "special")),
    "Graveyard": (("Town", "NE"), ("Forest", "E"), ("Abandoned Village", "SE")),
    "Cave": (("Forest", "W"), ("Abandoned Village", "SW"), ("Caverns 1", "S")),
    "Caverns 1": (("Cave", "N"), ("Caverns 2", "S")),
    "Caverns 2": (("Caverns 1", "N"), ("Caverns 3", "S")),
    "Caverns 3": (("Caverns 2", "N"), ("Caverns 4", "S")),
    "Caverns 4": (("Caverns 3", "N"), ("Deep Caverns", "S")),
    "Abandoned Village": (("Graveyard", "NW"), ("Forest", "N"), ("Cave", "NE"), 
        ("Ancient Forest", "S")),
    "Ancient Forest": (("Forest", "special"), ("Abandoned Village", "N"), 
        ("Deep Caverns", "special"), ("Ancient Ruins", "E")),
    "Deep Caverns": (("Caverns 4", "N"), ("Ancient Ruins", "S"), ("Dragon's Den", "E")),
    "Ancient Ruins": (("Ancient Forest", "W"), ("Corridor Between Worlds", "special")),
    "Corridor Between Worlds": (("Forest", "special"), ("Graveyard", "special"), 
        ("Cave", "special"), ("Abandoned Village", "special"), ("Ancient Forest", "special"), 
        ("Deep Caverns", "special"), ("Ancient Ruins", "special"), ("Dragon's Den", "special"), 
        ("Steppe of Sheol", "special")),
    "Steppe of Sheol": (("Ancient Ruins", "special")),
    "Dragon's Den": (("Deep Caverns", "W"))
}

#-------------------------------------------------------------------------------------#

# Generate Enemies

goblin1 = Character("Goblin", "goblin", "common", 1, 1, 2, 1)
bandit1 = Character("Bandit", "bandit", "common", 2, 2, 3, 2)
wolf1 = Character("Wolf", "wolf", "common", 2, 1, 4, 1)
zombie1 = Character("Zombie", "zombie", "uncommon", 1, 1, 0, 10),
troll1 = Character("Troll", "troll", "rare", 8, 8, 2, 1)
shadow1 = Character("Shadow Elemental", "shadow", "uncommon", 4, 0.1, 4, 10)
greaterShadow1 = Character("Greater Shadow Elemental", "greaterShadow", "rare", 8, 2, 5, 20)
deathShadow1 = Character("Shadow of Death", "deathShadow", "mythic", 15, 5, 6, 30)
vampire1 = Character("Vampire Fledgling", "babyVampire", "uncommon", 3, 3, 3, 2)
vampire2 = Character("Adult Vampire", "adultVampire", "rare", 5, 5, 5, 5)
vampire3 = Character("Elder Vampire", "elderVampire", "mythic", 10, 20, 8, 10)
dragon = Character("Dragon", "dragon", "unique", 50, 100, 15, 100)

enemies = {
    "common": (goblin1, bandit1, wolf1),
    "uncommon": (zombie1, shadow1, vampire1),
    "rare": (troll1, greaterShadow1, vampire2),
    "mythic": (vampire3, deathShadow1),
    "unique": (dragon)
}

# In the future, enemies will become location dependent.
# e.g. dragon will only appear in Dragon's Den, zombie will only appear in Graveyard, etc.

#-------------------------------------------------------------------------------------#

# Gameplay definitions.

def idle(location):

    while True:
        
        print("Actions:\n" + "-" * 20)
        print("1. Travel")
        print("2. Explore")
        print("3. Rest")
        print("4. Quit")
        print("-" * 20, end = "")
        raw_input = input("Choose an action (1-4): ")

        if raw_input == "1":
            travel(location)
        elif raw_input == "2":
            explore(location)
        elif raw_input == "3":
            rest(location)
        elif raw_input == "4":
            print("Thank you for playing.")
            break
        else:
            print("Please make a valid choice.")

def travel(location):
    directions = [loc[1] for loc in worldMap[location]]
    
    while True:
    
        print("You can travel:\n" + "-" * 20)
        for i in range(len(worldMap[location])):
            print(f"{i + 1}. {directions[i]}")
        print("-" * 20)
        directionsIndex = input(f"Choose a direction (1-{len(directions)}): ")

        if directionsIndex not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "special"]:
            print("\nPlease select a valid choice.")
        elif int(directionsIndex) < 1 or int(directionsIndex) > len(directions):
            print("\nPlease select a valid choice.")
        else:
            if directionsIndex == "special":
                print("Work in progress.")
            else:
                goDirection = worldMap[location][int(directionsIndex) - 1]
            break

    leaveEncounter = randint(0, 1)

    if leaveEncounter == 0:
        print(f"{adventurer.name} is now in {goDirection[0]}.")
        idle(goDirection[0])
    else:
        encounter(1, location)
        idle(goDirection[0])

def townLocations(location):

    if location == "1":
        print(f"{adventurer.name} arrives at the Adventurer's Guild.")

        while True:

            print("Quests:\n" + "-" * 20)
            # These are empty, placeholder quests.  
            # The full game will have randomized daily quests and a main quest chain.
            # Quests will have their own data structure to draw upon.
            print("1. Easy: Slay 10 Goblins.")
            print("2. Medium: Retrieve Hunting Bow from Forest.")
            print("3. Hard: Search for missing people in Cave.")
            print("4. Return")
            print("-" * 20)
            raw_input = input("Choose an option: (1-4)")

            if raw_input in ["1", "2", "3"]:
                print("You have accepted the quest:")
                print()
            elif raw_input == "4":
                break
            else:
                print("Please select a valid choice.")

    elif location == "2":
        print()
    elif location == "3":
        print()
    elif location == "4":
        print()

def explore(location):
    
    if location == "Town":
        while True:

            print("Places of interest:\n" + "-" * 20)
            print("1. Adventurer's Guild")
            print("2. Blacksmith's Forge")
            print("3. Alchemist's Apothecary")
            print("4. Chapel")
            print("5. Return")
            print("-" * 20)
            print("Choose a place to visit (1-5): ")
            raw_input = input()

            if raw_input not in ["1, 2, 3, 4, 5"]:
                print("Please select a valid choice.")
            elif raw_input == "1":
                townLocations(1)
                break
            elif raw_input == "1":
                townLocations(2)
                break
            elif raw_input == "1":
                townLocations(3)
                break
            elif raw_input == "1":
                townLocations(4)
                break
            else:
                break

    else:
        exploreEncounter = randint(1, 10)

        if exploreEncounter == 1:
            print()

def rest(location):
    print()

def encounter(play, location):
    
    while play == 1:
        chooseEnemy = randint(1, 100)
        if 1 <= chooseEnemy <= 50:
            enemy = choice(enemies["common"])
        elif 51 <= chooseEnemy <= 80:
            enemy = choice(enemies["uncommon"])
        elif 81 <= chooseEnemy <= 95:
            enemy = choice(enemies["rare"])
        else:
            enemy = choice(enemies["mythic"])

        print(f"\n{adventurer.name} encounters a wild {enemy.name}!")

        while enemy.alive() and adventurer.alive():
            adventurer.status()
            enemy.status()
            print("\nActions:\n" + "-" * 20)
            print(f"1. Attack {enemy.name}")
            print("2. Defend")
            if adventurer.rpgClass == "mage":
                print("3. Use Item/Magic")
            else:
                print("3. Use Item")
            print("4. Flee")
            print("5. Quit")
            print("-" * 20)
            print("Choose an action (1-5): ", end="")
            raw_input = input()
            
            if raw_input == "1":
                adventurer.attack(enemy)
                if enemy.alive():
                    enemy.attack(adventurer)
                else:
                    adventurer.loot(enemy)

            elif raw_input == "2":
                defenseCheck = adventurer.defend(enemy)
                if enemy.alive():
                    enemy.attack(adventurer, defenseCheck)

            elif raw_input == "3":
                adventurer.use(enemy)
                if enemy.alive():
                    enemy.attack(adventurer)
                else:
                    adventurer.loot(enemy)

            elif raw_input == "4":
                enemy.attack(adventurer)
                loseGold = randint(1, enemy.power)
                if adventurer.alive():
                    adventurer.items["Gold"] -= randint(1, enemy.power)
                    print(f"{adventurer.name} fled to fight another day and lost {loseGold} gold.")
                break

            elif raw_input == "5":
                print("Thank you for playing.")
                play = 0
                break
            else:
                print(f"Please make a valid choice.")

        # If enemy dies, another enemy of the same type must be able to respawn.

        if enemy.alive() == False:
            enemy.health = int(enemy.endurance * 10)

        if adventurer.alive() == False:
            play = 0

#-------------------------------------------------------------------------------------#
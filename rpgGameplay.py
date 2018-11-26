# Module:  Gameplay mechanics definitions.

#-------------------------------------------------------------------------------------#

# Initialize

# from random import randint
# from random import choice
from rpgCharacter import *

#-------------------------------------------------------------------------------------#

# Character creation

input("\nNote:  When text is followed by '...' Press ENTER to continue...")

yourName = input("\nWhat is your name, adventurer?\n")
print(f"\nWelcome, {yourName}, what is your class?\n" + "-" * 20)
print("1. Warrior: Gifted with overwhelming strength and steadfast endurance.")
print("2. Assassin: Gifted with blinding speed and deadly skill.")
print("3. Mage: Gifted with arcane knowledge and mystical powers.")
print("-" * 20)
chooseClass = 0

while chooseClass == 0:
    yourClass = input("Choose an option (1-3): ")
    if yourClass not in ("1", "2", "3"):
        print("Please select a valid selection")
    else:
        if yourClass == "1":
            adventurer = Character(yourName, "warrior", "player", 5, 5, 3, 3)
        elif yourClass == "2":
            adventurer = Character(yourName, "assassin", "player", 2, 3, 6, 4)
        else:
            adventurer = Character(yourName, "mage", "player", 1, 2, 3, 8)
        
        chooseClass = 1

print(f"\nAh, a {adventurer.rpgClass}.  I should have guessed by ", end = "")
if adventurer.rpgClass == "warrior":
    print("that intimidating sword on your back...")
elif adventurer.rpgClass == "assassin":
    print("those sharp daggers you have sheathed...")
else:
    print("that strange staff you're holding...")
input()
print("Not many travelers venture here to the town of Dunwich...")
input()
print("There have been all manners of savage beasts and ungodly creatures...")
input()
print("That've started plaguing the surrounding areas...")
input()
print("Only daring adventurers seeking glory or treasures traverse these lands...")
input()
print("Though some would use another word to describe them...")
input()
print("Pay them no mind.  Many here welcome any who come to rid us of the surrounding blight...")
input()
print("The local Adventurer's Guild has a list of quests if you seek to be rewarded for your efforts...")
input()
print("The local stores can help replenish your stock or provide new wares...")
input()
print("Among a few other places of interest...")
input()
print("But enough of my rambling.  I'll let you explore for yourself...")
input()
print("Town of Dunwich")

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

# Gameplay definitions.

def idle(location):

    while True:
        
        print("\nActions:\n" + "-" * 20)
        print("1. Travel to a new area")
        print("2. Explore the area")
        print("3. Rest for the day")
        print("4. Check status")
        print("5. Quit")
        print("-" * 20)
        raw_input = input("Choose an action (1-5): ")

        if raw_input == "1":
            travel(location)
        elif raw_input == "2":
            explore(location)
        elif raw_input == "3":
            if location == "Steppe of Sheol":
                print(f"\nThis area is cursed. {adventurer.name} cannot rest here.")
            else:
                rest()
        elif raw_input == "4":
            print()
            adventurer.status()
        elif raw_input == "5":
            print("\nThank you for playing.")
            break
        else:
            print("\nPlease select a valid choice.")

def travel(location):
   
    directions = [loc[1] for loc in worldMap[location]]
    
    while True:
    
        print("\nYou can travel:\n" + "-" * 20)
        for i in range(len(worldMap[location])):
            print(f"{i + 1}. {directions[i]}")
        back = len(directions) + 1
        print(f"{back}. Return")
        print("-" * 20)
        directionsIndex = input(f"Choose a direction (1-{len(directions)}): ")

        if directionsIndex not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "special"]:
            print("\nPlease select a valid choice.")
        elif int(directionsIndex) < 1 or int(directionsIndex) > back:
            print("\nPlease select a valid choice.")
        else:
            if directionsIndex == "special":
                print("Work in progress.")
                play = 0
            elif directionsIndex == str(back):
                play = 0
            else:
                goDirection = worldMap[location][int(directionsIndex) - 1]
                play = 1
            break

    if play == 1:

        leaveEncounter = randint(0, 1)

        if leaveEncounter == 0:
            if goDirection[0] == "Steppe of Sheol":
                print(f"\nAfter stepping through the portal, you feel a wave of dread sweep over your body...")
                input()
                print("The sky shifts through an unnatural palette of colors...")
                input()
                print("The air grows thick with the smell of sulfur and brimestone...")
                input()
                print("The very ground begins transforming into strange shapes that seem to defy possibility...")
                input()
                print("Before you can turn back, the portal collapses, leaving you trapped here...")
                input()
                print("Everything is beyond your comprehension, save for one fact...")
                input()
                print("This realm is not meant for humans to tread...")
                input()
                print("You must leave.")
            
            print(f"\n{goDirection[0]}")
            idle(goDirection[0])

        else:
            if location != "Town":
                encounter(1, location, "normal")
            print(f"\n{goDirection[0]}")
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

            print("\nPlaces of interest:\n" + "-" * 20)
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
        exploreEncounter = randint(1, 100)
        if 1 <= exploreEncounter <= 90:
            encounter(1, location, "normal")
        else:
            addGold = randint(2, 10)
            addSmallPotion = randint(1, 5) // 5
            addFireBomb = randint(1, 5) // 5

            if 96 <= exploreEncounter <= 100:
                if location in ["Graveyard", "Ancient Forest", "Ancient Ruins", 
                    "Steppe of Sheol", "Dragon's Den"]:
                    encounter(1, location, "boss")

                else:
                    if addGold >= 1:
                        adventurer.items["Gold"] += addGold
                        print(f"{adventurer.name} obtained {addGold} gold!")
                    if addSmallPotion >= 1:
                        adventurer.items["Use"]["Small Health Potion"][0] += addSmallPotion
                        print(f"{adventurer.name} obtained {addSmallPotion} small potion!")
                    if addFireBomb >= 1:
                        adventurer.items["Use"]["Fire Bomb"][0] += addFireBomb
                        print(f"{adventurer.name} obtained {addFireBomb} fire bomb!")
            else:
                if addGold >= 1:
                    adventurer.items["Gold"] += addGold
                    print(f"{adventurer.name} obtained {addGold} gold!")
                if addSmallPotion >= 1:
                    adventurer.items["Use"]["Small Health Potion"][0] += addSmallPotion
                    print(f"{adventurer.name} obtained {addSmallPotion} small potion!")
                if addFireBomb >= 1:
                    adventurer.items["Use"]["Fire Bomb"][0] += addFireBomb
                    print(f"{adventurer.name} obtained {addFireBomb} fire bomb!")

def rest():
    
    if adventurer.rpgClass == "warrior":
        adventurer.energy = adventurer.strength * 10
    elif adventurer.rpgClass == "assassin":
        adventurer.energy = adventurer.agility * 10
    elif adventurer.rpgClass == "mage":
        adventurer.energy = adventurer.mentality * 10
    adventurer.health = (adventurer.endurance + adventurer.items["Armor"][1]) * 10
    print(f"\nAfter a good rest, {adventurer.name} feels refreshed.")

def encounter(play, location, enemyType):

    if enemyType == "normal":
        chooseEnemy = randint(1, 100)
        if 1 <= chooseEnemy <= 50:
            enemy = choice(enemies["common"])
        elif 51 <= chooseEnemy <= 80:
            enemy = choice(enemies["uncommon"])
        elif 81 <= chooseEnemy <= 95:
            enemy = choice(enemies["rare"])
        else:
            enemy = choice(enemies["mythic"])
        print(enemy)
        print(f"\n{adventurer.name} encounters a wild {enemy.name}!")

    elif enemyType == "boss":
        print()
        enemy = bossEnemies[location]

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
                print(f"\n{adventurer.name} fled to fight another day and lost {loseGold} gold.")
            break

        else:
            print(f"\nPlease select a valid choice.")

    # If enemy dies, another enemy of the same type must be able to respawn.

    if enemy.alive() == False:
        enemy.health = int(enemy.endurance * 10)

#-------------------------------------------------------------------------------------#
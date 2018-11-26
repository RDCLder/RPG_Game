# This file is used to test features/bugs to be implemented/fixed.

#-------------------------------------------------------------------------------------#

# Bugs/features to be fixed/implemented

# - Create a GUI
#   - Base menu with options
#   - Very basic real-time display (e.g. pokemon games)
#   - Very basic map to the side
#   - Potentially have animations 
#   - Sound effects
# - Implement a leveling system.
#   - Have enemies scale to level.

# - Small Features
#   - Special attacks for each character class based on energy
#   - Make enemy spawning location dependent.

# - Bugs
#   - Make sure all inputs are valid.
#   - e.g. An input that requires a number...

#-------------------------------------------------------------------------------------#

from random import randint
from rpgCharacter import *

goblin1 = Character("Goblin", "goblin", "common", 1, 1, 2, 1)
bandit1 = Character("Bandit", "bandit", "common", 2, 2, 3, 2)
wolf1 = Character("Wolf", "wolf", "common", 2, 1, 4, 1)
zombie1 = Character("Zombie", "zombie", "uncommon", 1, 1, 0, 10),
troll1 = Character("Troll", "troll", "rare", 8, 8, 2, 1)
shadow1 = Character("Shadow Elemental", "shadow", "uncommon", 4, 0.1, 4, 10)
greaterShadow1 = Character("Greater Shadow Elemental", "greaterShadow", "rare", 8, 2, 5, 15)
deathShadow1 = Character("Shadow of Death", "deathShadow", "mythic", 15, 5, 6, 20)
vampire1 = Character("Vampire Fledgling", "babyVampire", "uncommon", 3, 3, 3, 2)
vampire2 = Character("Adult Vampire", "adultVampire", "rare", 5, 5, 5, 5)
vampire3 = Character("Elder Vampire", "elderVampire", "mythic", 10, 20, 8, 10)
lich = Character("Lich", "lich", "boss", 1, 10, 3, 30)
basilisk = Character("Basilisk", "basilisk", "boss", 10, 30, 4, 10)
efreet = Character("Efreet", "djinn", "boss", 20, 20, 10, 20)
ancientOne = Character("Ancient One", "elderDemon", "boss", 30, 30, 10, 25)
dragon = Character("High Dragon", "dragon", "boss", 50, 100, 15, 100)

enemies = {
    "common": (goblin1, bandit1, wolf1),
    "uncommon": (zombie1, shadow1, vampire1),
    "rare": (troll1, greaterShadow1, vampire2),
    "mythic": (vampire3, deathShadow1)
}

chooseEnemy = randint(1, 100)
if 1 <= chooseEnemy <= 50:
    enemy = choice(enemies["common"])
elif 51 <= chooseEnemy <= 80:
    enemy = choice(enemies["uncommon"])
elif 81 <= chooseEnemy <= 95:
    enemy = choice(enemies["rare"])
else:
    enemy = choice(enemies["mythic"])
print(f"\nYou encounters a wild {enemy.name}!")
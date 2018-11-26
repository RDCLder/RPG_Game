# Module:  Character class definitions.

#-------------------------------------------------------------------------------------#

# Initialize

from random import randint
from random import choice
yourName = "Hero"

#-------------------------------------------------------------------------------------#

# Character Class

class Character:

    def __init__(self, name, rpgClass, tier, strength, endurance, agility, mentality):
        
        self.name = name
        self.strength = strength
        self.endurance = endurance
        self.agility = agility
        self.mentality = mentality
        self.rpgClass = rpgClass
        self.tier = tier
        
        if tier == "player":
            if rpgClass == "warrior":
                self.items = {
                    "Gold": 50,
                    "Weapon": ("Iron Sword", 2),
                    "Armor": ("Iron Armor", 2, -1),
                    "Use": {
                        "Small Health Potion": [3, "health"],
                        "Small Energy Potion": [2, "energy"],
                        "Fire Bomb": [2, "fire"]
                        },
                    "Other": []
                    }
                self.special = "warrior"
                self.energy = strength * 10

            elif rpgClass == "assassin":
                self.items = {
                    "Gold": 50,
                    "Weapon": ("Dual Iron Daggers", 2),
                    "Armor": ("Leather Armor", 1, 0),
                    "Use": {
                        "Small Health Potion": [3, "health"],
                        "Small Energy Potoion": [3, "energy"],
                        "Fire Bomb": [3, "fire"],
                        "Ice Bomb": [2, "ice"]
                        },
                    "Other": []
                    }
                self.special = "assassin"
                self.energy = agility * 10

            elif rpgClass == "mage":
                self.items = {
                    "Gold": 50,
                    "Weapon": ("Fire Staff", 2, "fire"),
                    "Armor": ("Mage Robe", 1, 0),
                    "Use": {
                        "Small Health Potion": [3, "health"],
                        "Small Energy Potion": [3, "mana"],
                        "Fire Bomb": [1, "fire"],
                        "Ice Bomb": [1, "ice"],
                        "Fire Bolt": [1, "fire", 5],
                        "Ice Bolt": [1, "ice", 5]
                        },
                    "Other": []
                    }
                self.special = "magic"
                self.energy = mentality * 10
            
            self.power = (self.strength + self.items["Weapon"][1]) * 2
            self.health = (self.endurance + self.items["Armor"][1]) * 10
            self.agile = self.agility + self.items["Armor"][2]
            self.mind = self.mentality * 10

        else:
            self.health = int(self.endurance * 10)
            self.power = int(self.strength * 2)
            self.agile = self.agility
            self.mind = int(self.mentality * 10)
            if rpgClass == "zombie":
                self.special = "undying"
            elif rpgClass == "shadow":
                self.special = "shadow"
            elif rpgClass == "dragon":
                self.special = "fireproof"
            else:
                self.special = "normal"

    def __str__(self):
        return self.name

    def attack(self, target, targetDefense=0):
        
        # Attack modifiers.  Player characters have a 20% chance to "critical hit" for 2x damage.
        
        if self.tier == "player":
            if randint(1, 5) // 5 == 1:
                damage = self.power * 2
            else:
                damage = randint(0, self.power)
        else:
            damage = randint(0, self.power)
        
        # Defense prevents some damage.

        if targetDefense > damage:
            targetDefense = damage
        damage -= targetDefense

        # Vampires gain back some of the damage they deal as health.

        if self.rpgClass == "vampire":
            self.health += randint(damage // 4, damage)

        # Shadow Elementals are hard to hit.

        if target.rpgClass == "shadow":
            if randint(1, 10) // 10 == 1:
                pass
            else:
                damage = 0

        target.health -= damage
        print(f"\n{self.name} does {damage} damage to {target.name}.")
        
        # Zombies only die to fire damage
        
        if target.rpgClass == "zombie":
            if len(self.items["Weapon"]) == 3:
                if self.items["Weapon"][2] == "fire":
                    if target.health <= 0:
                        print(f"{target.name} is dead.")
            else:
                pass
        
        # Check if adventurer or enemy is dead
        
        elif target.rpgClass == "adventurer":
            if target.health <= 0:
                print(f"{target.name} is dead!  You lose!")
        else:
            if target.health <= 0:
                print(f"{target.name} is dead.")
                    
    def defend(self, target):
        
        defense = randint(0, self.power // 2)
        print(f"{self.name} prevents {defense} damage.")
        return defense

    def use(self, target):

        useFinish = 0

        while useFinish == 0:
            itemsList = [item for item in self.items["Use"].items()]

            print(f"\n{self.name} can use the following items:\n" + "-" * 20)
            for i in range(len(itemsList)):
                print(f"{i + 1}. {itemsList[i][1][0]}x {itemsList[i][0]}")
            print("-" * 20)
            itemIndex = input(f"Select an item to use (1-{len(itemsList)}): ")

            if int(itemIndex) < 1 or int(itemIndex) > len(itemsList):
                print("\nPlease select a valid item.")
            else:
                useItem = itemsList[int(itemIndex) - 1][0]
            
            while useFinish == 0:
                print()
                if self.items["Use"][useItem][0] > 0:
                    if useItem == "Small Health Potion":
                        if self.health > (self.endurance + self.items["Armor"][1]) * 10 - 30:
                            self.health = (self.endurance + self.items["Armor"][1]) * 10
                        elif self.health <= (self.endurance + self.items["Armor"][1]) * 10 - 30:
                            self.health += 30
                        print(f"\n{useItem} restored 30 health.")
                    
                    elif useItem == "Small Energy Potion":
                        if self.rpgClass == "warrior":
                            startEnergy = self.strength * 10
                        elif self.rpgClass == "assassin":
                            startEnergy = self.agility * 10
                        elif self.rpgClass == "mage":
                            startEnergy = self.mentality * 10

                        if self.energy > startEnergy - 30:
                            self.energy = startEnergy
                        elif self.energy <= startEnergy - 30:
                            self.energy += 30
                        print(f"\n{useItem} restored 30 energy.")
                    
                    elif useItem == "Fire Bomb":
                        target.health -= 30
                        target.special = "fire"
                        print(f"{useItem} does 30 fire damage.")
                        if target.health <= 0:
                            target.health = 0
                            print(f"{target.name} is dead.")
                    
                    elif useItem == "Ice Bomb":
                        target.health -= 30
                        target.agile -= 3
                        print(f"{useItem} does 30 ice damage.")
                        if target.agile <= 0:
                            target.agile = 0
                            print(f"{target.name} has been frozen for the turn.")
                        else:
                            print(f"{target.name} has been slowed down.")

                    elif useItem == "Fire Bolt":
                        damage = randint(self.mentality, self.mentality * 2)
                        target.special = "fire"
                        print(f"{useItem} does {damage} fire damage.")
                        target.health -= damage
                        if target.health <= 0:
                            target.health = 0
                            print(f"{target.name} is dead.")
                    
                    elif useItem == "Ice Bolt":
                        damage = randint(self.mentality, self.mentality * 2)
                        print(f"{useItem} does {damage} ice damage.")
                        target.health -= damage
                        target.agile -= 2
                        
                        if target.agile <= 0:
                            target.agile = 0
                            print(f"{target.name} has been frozen for the turn.")
                        else:
                            print(f"{target.name} has been slowed down.")

                    if useItem == "Ice Bolt" or useItem == "Fire Bolt":
                        self.energy -= self.items["Use"][useItem][2]
                    else:
                        self.items["Use"][useItem][0] -= 1
                    useFinish = 1

                else:
                    print("Please select a valid item.")

    def loot(self, target):
        
        if target.tier == "common":
            addGold = randint(0, 8)
            addSmallPotion = randint(1, 8) // 8
            addFireBomb = randint(1, 8) // 8

        elif target.tier == "uncommon":
            addGold = randint(2, 10)
            addSmallPotion = randint(1, 5) // 5
            addFireBomb = randint(1, 5) // 5

        elif target.tier == "rare":
            addGold = randint(5, 20)
            addSmallPotion = randint(1, 3) // 3
            addFireBomb = randint(1, 3) // 3

        elif target.tier == "mythic":
            addGold = randint(50, 200)
            addSmallPotion = randint(2, 5)
            addFireBomb = randint(2, 5)

        elif target.rpgClass == "dragon":
            addGold = randint(500, 2000)
            addSmallPotion = randint(5, 8)
            addFireBomb = randint(5, 8)
            self.items["Other"].extend(
                {"Weapon": ("Dragon's Fury", 25, "fire")},
                {"Armor": ("Dragonscale Armor", 20)}
                )

        if addGold >= 1:
            self.items["Gold"] += addGold
            print(f"{self.name} obtained {addGold} gold!")
        if addSmallPotion >= 1:
            self.items["Use"]["Small Health Potion"][0] += addSmallPotion
            print(f"{self.name} obtained {addSmallPotion} small potion!")
        if addFireBomb >= 1:
            self.items["Use"]["Fire Bomb"][0] += addFireBomb
            print(f"{self.name} obtained {addFireBomb} fire bomb!")

    def alive(self):
        
        if self.name == "Zombie":
            if self.special == "fire" and self.health <= 0:
                return False
            else:
                return True
        else:
            if self.health > 0:
                return True
            if self.health <= 0:
                return False
    
    def status(self):
        
        if self.tier == "player":
            print(f"{self.name} has {self.health} health, {self.energy} energy and {self.power} power.")
        else:
            print(f"{self.name} has {self.health} health and {self.power} power.")

#-------------------------------------------------------------------------------------#

# Generate Enemies

goblin1 = Character("Goblin", "goblin", "common", 1, 1, 2, 1)
bandit1 = Character("Bandit", "bandit", "common", 2, 2, 3, 2)
wolf1 = Character("Wolf", "wolf", "common", 2, 1, 4, 1)
zombie1 = Character("Zombie", "zombie", "uncommon", 1, 1, 0, 10),
troll1 = Character("Troll", "troll", "rare", 8, 8, 2, 1)
shadow1 = Character("Shadow Elemental", "shadow", "uncommon", 4, 0.1, 4, 10)
greaterShadow1 = Character("Greater Shadow Elemental", "shadow", "rare", 8, 2, 5, 15)
deathShadow1 = Character("Shadow of Death", "shadow", "mythic", 15, 5, 6, 20)
babyVampire1 = Character("Vampire Fledgling", "vampire", "uncommon", 3, 3, 3, 2)
adultVampire1 = Character("Adult Vampire", "vampire", "rare", 5, 5, 5, 5)
elderVampire1 = Character("Elder Vampire", "vampire", "mythic", 10, 20, 8, 10)
lich = Character("Lich", "lich", "boss", 1, 10, 3, 30)
basilisk = Character("Basilisk", "basilisk", "boss", 10, 30, 4, 10)
efreet = Character("Efreet", "djinn", "boss", 20, 20, 10, 20)
ancientOne = Character("Ancient One", "elderDemon", "boss", 30, 30, 10, 25)
dragon = Character("High Dragon", "dragon", "boss", 50, 100, 15, 100)

enemies = {
    "common": (goblin1, bandit1, wolf1),
    "uncommon": (zombie1, shadow1, babyVampire1),
    "rare": (troll1, greaterShadow1, adultVampire1),
    "mythic": (elderVampire1, deathShadow1)
}

bossEnemies = {
    "Graveyard": lich,
    "Deep Forest": basilisk,
    "Ancient Ruins": efreet,
    "Steppe of Sheol": ancientOne,
    "Dragon's Den": dragon
}

# In the future, enemies will become location dependent.
# e.g. dragon will only appear in Dragon's Den, zombie will only appear in Graveyard, etc.

#-------------------------------------------------------------------------------------#
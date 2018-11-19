#!/usr/bin/env python

# In this simple RPG game, the hero fights an enemy. He has the options to:

# 1. fight enemy
# 2. do nothing - in which case the enemy will attack him anyway
# 3. flee

#-------------------------------------------------------------------------------------#

# Initialize

from random import randint

class Character:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        damage = randint(0, self.power)
        target.health -= damage
        print(f"The {self.name} does {damage} damage to the {target.name}.")
        if target.health <= 0:
            print(f"The {target.name} is dead.")

    def alive(self):
        if self.health > 0:
            return True
    
    def status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")


goblin = Character("Goblin", 10, 2)
zombie = Character("Zombie", 9000, 1)
dragon = Character("Dragon", 1000000, 100)
enemies = [zombie, goblin, dragon]

#-------------------------------------------------------------------------------------#

# Main Program

yourName = input("What is your name, adventurer?\n")
adventurer = Character(yourName, 40, 5)

def main():
    
    enemy = enemies[randint(0, len(enemies) - 1)]
    print(f"\n{adventurer.name} encounters a wild {enemy.name}!")

    while enemy.alive() and adventurer.alive():
        adventurer.status()
        enemy.status()
        print("\nWhat do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            adventurer.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.health > 0:
            enemy.attack(adventurer)

main()

#-------------------------------------------------------------------------------------#
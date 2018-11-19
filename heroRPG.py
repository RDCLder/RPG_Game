#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"You do {self.power} damage to the goblin.")
        if target.health <= 0:
            print(f"The {target.name} is dead.")

    def alive(self):
        if self.health > 0:
            return True
    
    def status(self):
        print(f"You have {self.health} health and {self.power} power.")

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    hero = Character("Hero", hero_health, hero_power)
    goblin = Character("Goblin", goblin_health, goblin_power)

    while goblin.alive() and hero.alive():
        hero.status()
        goblin.status()
        print("\nWhat do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()
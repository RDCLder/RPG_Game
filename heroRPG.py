#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    hero = Hero(hero_health, hero_power)
    goblin = Goblin(goblin_health, goblin_power)

    while goblin.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print()
        print("What do you want to do?")
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

        if goblin_health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()

# Step 1

class Hero:

    def __init__(self, hero_health, hero_power):
        self.hero_health = hero_health
        self.hero_power = hero_power

    def attack(self, goblin):
        goblin.goblin_health -= self.hero_power
        print(f"You do {self.hero_power} damage to the goblin.")
        if goblin.goblin_health <= 0:
            print("The goblin is dead.")

    def alive(self):
        if self.hero_health > 0:
            return True

class Goblin:

    def __init__(self, goblin_health, goblin_power):
        self.goblin_health = goblin_health
        self.goblin_power = goblin_power
    
    def attack(self, hero):
        hero.hero_health -= self.goblin_power
        print(f"The goblin does {self.goblin_power} damage to you.")
        if hero.hero_health <= 0:
            print("You are dead.")
    
    def alive(self):
        if self.goblin_health > 0:
            return True
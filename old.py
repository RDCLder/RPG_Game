# File containing "obsolete" code that might need to be referred to later

#-------------------------------------------------------------------------------------#

# Item Use Testing

allItems = {
    "Gold": 20,
    "Weapon": ("Iron Sword", 2),
    "Armor": ("Iron Armor", 2, -1),
    "Use": {
        "Small Health Potion": [3, "health"],
        "Small Mana Potion": [3, "mana"],
        "Fire Bomb": [2, "fire"],
        "Fire Bolt": [5, "fire"],
        "Ice Bolt": [5, "ice"]
        },
    "Other": []
    }

name = "Hero"
endurance = 3
health = (endurance + allItems["Armor"][1]) * 10
enemyName = "Enemy"
enemyHealth = 20
useFinish = 0


while useFinish == 0:

    itemsList = [item for item in allItems["Use"].items()]

    print(f"\nYou can use the following items:\n" + "-" * 20)
    for i in range(len(itemsList)):
        print(f"{i + 1}. {itemsList[i][1][0]}x {itemsList[i][0]}")
    print("-" * 20)
    itemIndex = input(f"Select an item to use (1-{len(itemsList)}): ")

    if int(itemIndex) < 0 or int(itemIndex) > len(itemsList):
        print("\nPlease select a valid item.")
    else:
        useItem = itemsList[int(itemIndex) - 1][0]
        
        if useItem == "Small Health Potion":
            if health > (endurance + allItems["Armor"][1]) * 10 - 30:
                health = (endurance + allItems["Armor"][1]) * 10
            elif health <= (endurance + allItems["Armor"][1]) - 30:
                health += 30
            print(f"\nSmall Health Potion restored 30 health. {name} now has {health} health.")
        
        elif useItem == "Fire Bomb":
            if enemyHealth <= 0:
                enemyHealth = 0
                print(f"{enemyName} is dead.")
            else:
                print(f"{enemyName} now has {enemyHealth} health.")
        
        allItems["Use"][useItem][0] -= 1
        useFinish = 1

print(allItems["Use"][useItem][0])

#-------------------------------------------------------------------------------------#


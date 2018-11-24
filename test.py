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

from rpgGameplay import worldMap

def travel(play, location):
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
    
    print(f"You are now in {goDirection[0]}.")

travel(1, "Town")
travel(1, "Forest")
# module 5 lab part 1
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 6/30/26 - foxes
# modified 6/30/26 - foxes
#
# description: Goldfish Playdate Planner

import random

goldfish = ["Bubbles", 
            "Finley", 
            "Goldie", 
            "Splash", 
            "Nemo"]

print("Welcome to the Goldfish Playdate Planner!")
print("Our goldfish friends are: " + ", ".join(goldfish))

new_fish = input("Enter the name of a new goldfish: ")
goldfish.append(new_fish)

print("Updated goldfish list: " + ", ".join(goldfish))

fish_to_remove = input("Enter the name of a goldfish to remove: ")
if fish_to_remove in goldfish:
    goldfish.remove(fish_to_remove)
    print(fish_to_remove + " has been removed from the list.")
else:
    print("Sorry, " + fish_to_remove + " is not in the list.")

print("Current goldfish list: " + ", ".join(goldfish))

print("\nLet's create some playdate pairs!")
random.shuffle(goldfish)

for i in range(0, len(goldfish), 2):
    if i + 1 < len(goldfish):
        print(goldfish[i] + " will have a playdate with " + goldfish[i+1])
    else:
        print(goldfish[i] + " will have a solo play session.")

# Optional Extension

playdate_schedule = []

for i in range(len(goldfish)):
    day = input("Enter a day for " + goldfish[i] + "'s playdate: ")
    playdate_schedule.append(day)

print("\nPlaydate Schedule:")
for i in range(len(goldfish)):
    print(goldfish[i] + " has a playdate on " + playdate_schedule[i])

search_fish = input("\nEnter a goldfish name to find its playdate: ")
if search_fish in goldfish:
    index = goldfish.index(search_fish)
    print(search_fish + " has a playdate on " + playdate_schedule[index])
else:
    print("Sorry, " + search_fish + " is not in the list.")
# module 7 lab part 1
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/8/26 - foxes
# modified 7/9/26 - foxes
#
# description: Data Structures

# Let's start with dictionaries to represent food stands
food_stands = {
    "Pronto Pups": "Corn Dogs",
    "Big Fat Bacon": "Bacon-on-a-Stick"
}

# Printing the food stands
print("Food stands at the fair:")
for stand, food in food_stands.items():
    print(stand + ": " + food)

# Adding a new food stand
food_stands["Fresh French Fries"] = "Fries"

# Adding a new food stand for optional challenge
food_stands["Sweet Martha's"] = "Pancakes and pasteries"

# Adding a new food stand for optional challenge
food_stands["The Cheese Curd Tacos"] = "Tacos with a Midwest Flair"

# Updating a food item
food_stands["Pronto Pups"] = "Footlong Corn Dogs"

# Removing a food stand
del food_stands["Big Fat Bacon"]
print("\nAfter adding Fries stand, updating Pronto Pups and removing Big Fat Bacon:")
print(food_stands)

# Now let's use tuples for fair attractions
attractions = [
    ("Giant Slide", "East of the Grandstand"),
    ("Skyride", "Near Dan Patch Avenue")
]

# Printing the attractions
print("\nFair attractions:")
for attraction in attractions:
    print(attraction[0] + " is located " + attraction[1])

# Adding a new attraction
new_attraction = ("Haunted House", "Near the Midway")
attractions.append(new_attraction)
print("\nAfter adding a new attraction:")
for attraction in attractions:
    print(attraction[0] + " is located " + attraction[1])

# Finally, let's use sets for unique fair activities
activities = {"Riding the Giant Slide", "Watching the Parade"}

print("\nInitial set of activities:")
print(activities)

# Trying to add a duplicate activity
activities.add("Watching the Parade")
print("\nAfter trying to add a duplicate activity:")
print(activities)

# Removing an activity
activities.remove("Riding the Giant Slide")
print("\nAfter removing an activity:")
print(activities)

# Let's create a daily planner using all three data structures
daily_planner = {
    "Morning": [("Breakfast", food_stands["Sweet Martha's"]), ("Ride", attractions[0][0])],
    "Afternoon": [("Lunch", food_stands["Pronto Pups"]), ("Activity", list(activities)[0])],
    "Evening": [("Dinner", food_stands["The Cheese Curd Tacos"]), ("Ride", attractions[2][0])]
}

print("\nYour Minnesota State Fair Daily Planner:")
for time, plans in daily_planner.items():
    print(time + ":")
    for plan in plans:
        print("- " + plan[0] + ": " + plan[1])
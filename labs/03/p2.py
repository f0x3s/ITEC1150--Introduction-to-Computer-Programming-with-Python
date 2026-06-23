# module 3 lab part 1
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 6/23/26 - foxes
# modified 6/23/26 - foxes
#
# description: simple ordering system for a barbecue truck.

SANDWITCH_PRICE = 8
PLATTER_PRICE = 12

customer_name = input("Please enter your name: ")

meal_choice = input("Do you want a sandwitch meal or a platter meal? (sandwitch/platter): ")

if meal_choice.lower() == "sandwitch":
    meal_price = SANDWITCH_PRICE
elif meal_choice.lower() == "platter":
    meal_price = PLATTER_PRICE
else:
    print("Invalid choice. Defaulting to sandwitch meal.")
    meal_choice = "sandwitch"
    meal_price = SANDWITCH_PRICE

num_meals = input("How many meals do you want?: ")
try:
    num_meals = int(num_meals)
    total_cost = meal_price * num_meals
except:
    print("error: Expecting numeric input for number of Meals")
    quit()

extra_sauce = input("Do you want extra sauce? (Yes/no): ")
if extra_sauce.lower() == "yes":
    total_cost += 0.50 * num_meals

original_total = meal_price * num_meals
sauce_added = extra_sauce.lower() == "yes"

print("\nOrder Summary: ")
print("Customer Name: " + customer_name)
print("Meal type: " + meal_choice + " meal")
print(f"Number of Meals: {num_meals}")
print("Extra Sauce: " + ("Yes" if sauce_added else "No"))
print(f"Original Total: ${original_total:.2f}")
print(f"Final Total: ${total_cost:.2f}")
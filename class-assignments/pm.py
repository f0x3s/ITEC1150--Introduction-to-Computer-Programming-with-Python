# Practice Midterm
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/9/26 - foxes
# modified 7/9/26 - foxes
#
# description: Python- based application to help customers select toppings for their tacos


print("Welcome to Catrinas Mexican Grill")

tortilla_types = ["Corn", "Flour", "Whole Wheat"]
filling_types: ["Beans", "Chicken", "Fish", "Beef"]
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]

def display_options(options) :
    for index, option in enumerate(options) :
        print(f"{index + 1}. {option}")

display_options
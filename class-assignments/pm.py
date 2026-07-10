# Practice Midterm
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/9/26 - foxes
# modified 7/9/26 - foxes
#
# description: Python- based application to help customers select toppings for their tacos

class Taco :
    def __init__(self, tortilla, filling, toppings) :
        self.tortilla = tortilla
        self.filling = filling
        self.toppings = toppings 

print("Welcome to Catrinas Mexican Grill")

MAX_TOPPINGS = 4
human_numbers = ["first", "second", "third", "fourth", "fifth","sixth","seventh","eighth","ninth","tenth"]

taco_options = {
    "tortilla" : (1, ["Corn", "Flour", "Whole Wheat"]),
    "filling" : (1, ["Beans", "Chicken", "Fish", "Beef"]),
    "topping" : (MAX_TOPPINGS, ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"])
}

def display_options(options, key) :
    for index, option in enumerate(options[key][1]) :
        print(f"{index + 1}. {option}")

    print(f"{len(options[key][1])+1}. Done (no more {key}s)" if options[key][0] > 1 else "")

def count_options(options) :
    return len(options)

def human_number(number) :
    return human_numbers[number]

print("Welcome to Catrinas!")
print("Get ready to build your taco...")

for key in taco_options.keys() :
   
   num_items = taco_options[key][0]
   for index in range(num_items) :
       
       str_index = "" if num_items == 1 else  human_number(index) + " "

       print(f"Select your {str_index}{key} (1-{count_options(taco_options[key][1])}):") 
       display_options(taco_options, key)
       






#print(f"\nSelect yout tortilla type (1-{count_options(tortilla_types)}):")
#display_options(tortilla_types)
while True:
    user_tortilla_type = input()[0:1]
    try :
        user_tortilla_type = int(user_tortilla_type)
        user_tortilla_type = tortilla_types[user_tortilla_type]
        break
    except :
        print(f"Error, expecting a number between 1 and {count_options(tortilla_types)}:")

print("Done")
# Midterm
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/14/26 - foxes
# modified 7/14/26 - foxes
#
# description: Python-based application to help BTG customers order burgers.

class Customer :
    def __init__(self):
        pass

class Burger :
    def __init__(self):
        self.toppings = []
        self.name = None
        pass

    def add_topping(self, topping) :
        self.toppings.append(topping)

    def check_for_name(self) :
        pass

TOPPINGS = {
    "Classic" : {
        "Lettuce" : 50,
        "Tomatoes" : 50,
        "Pickles" : 75,
        "Raw onions" : 100
        },

    "Gourmet" : {
        "Bacon" : 250,
        "Grilled Onions" : 200,
        "Green peppers" : 150,
        "Jalapeños" : 180,
        "Mushrooms" : 180,
        },

    "Sauces" : {
        "Mayonnaise" : 25,
        "Ketchup" : 25,
        "Mustard" : 25,
        "Sweet and Sour Relish" : 75,
        "BBQ sauce" : 25,
        "A1 Original Steak Sauce" : 75,
        "Frank's Original Hot Sauce" : 80,
        }
    }

def is_integer(value) :
    return isinstance(value, int)

def display_toppings(options, layer) :

    for key, value in options.items() :
        tabs = "\t" * layer

        if is_integer(value) :
            human_price = int(value)/100

            print(f"{tabs}{key}:", end = "")
            print("$%.2f" % human_price)
            # track recursion level
            layer == 0
            
        else :
            # track recursion level
            layer += 1
            print(f"{tabs}{key}:", end = "\n")
            display_toppings(value, layer)





# I wanted to practice string operations, so I added an additional program element
# As a promotional easter egg, creating a named burger applies a slight discount
# Encouraging customers to explore the Menu
# source: https://www.tastingtable.com/2099199/five-guys-burgers-popular-picks-toppings-ranked/
STYLES = {
    "Bacon & BBQ" : ["BBQ sauce", "Bacon", "Grilled onions", "Lettuce" ],
    "All the Way" : ["Grilled Onions", "Mushrooms", "Lettuce", "Pickles", "Tomatoes", "Mustard", "Mayo", "Ketchup"],
    "Veggies" : ["Lettuce", "Tomatoes", "Green Peppers", "Raw Onions", "Pickles", "Ketchup"],
    "Spicy" : ["Cheese", "Jalapeños", "Frank's Original Hot Sauce", "Tomatoes", "Mayonnaise"],
    "Briny Bite" : ["pickles", "Sweet and Sour Relish", "Mustard", "Raw Onions"]
}

print("Welcome to Burgers to Go!")
display_toppings(TOPPINGS, 0)
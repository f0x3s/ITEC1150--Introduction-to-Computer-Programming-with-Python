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

# for this assignment, I wanted to practice recursion, so I made a nested dict to parse.
TOPPINGS = {
    "Classic Toppings" : {
        "Lettuce" : 50,
        "Tomatoes" : 50,
        "Pickles" : 75,
        "Raw onions" : 100
        },

    "Gourmet Toppings" : {
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

def format_price(item, cents, adj) :
    human_price = int(cents)/100
    extra_spaces = " " * adj
    return extra_spaces + item + ": " + f"${human_price:.2f}"

def maximum_length(text ) :
    max_length = 0

    for key, value in text.items() :

        for key, value in text.items() :
            if is_integer(value) :
                current_length = len(format_price(key, value, 0))

            else : 

                current_length = maximum_length(value)
        
            if current_length > max_length :
                max_length = current_length

    return max_length

# compares length of two strings and returns the difference.
def calculate_str_adj(maximum, text) :
    return abs(maximum - len(text))

def display_topping_selection(options, layer, longest) :

    # check for first iteration
    if layer == 0:
        # if first iteration (header), calculate longest formatted item & price
        longest = maximum_length(options)
            
    for key, value in options.items() :

        # adjustment to indent levels
        spacing = "  " * layer
        
        # check if lowest level reached
        if is_integer(value) :
    
            # compare length of formatted item and price to maximum lenght of all formatted items and prices to caclulate adjustment
            test_str = format_price(key, value, 0)
            adj_spaces = calculate_str_adj(longest, test_str)

            # add adjustemnt to formatted item and price & print
            print(f"{spacing}{format_price(key, value, adj_spaces)}")
            
        else :

            # not at lowest level, just print key with proper indentation
            print(f"{spacing}{key}: ")

            # recurse with sub-dict
            display_topping_selection(value, layer + 1, longest)





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
display_topping_selection(TOPPINGS, 0, None)
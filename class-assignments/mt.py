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
    return item + ": " + extra_spaces + f"${human_price:.2f}"

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

def calculate_str_adj(maximum, text) :
    return maximum - len(text)

def display_toppings(options, layer) :

    longest = 0


    longest = maximum_length(options)
  
            
    for key, value in options.items() :
        spacing = "  " * layer

        if is_integer(value) :
            
            test_str = format_price(key, value, 0)

            adj_spaces = calculate_str_adj(longest, test_str)

            print(f"{spacing}{format_price(key, value, adj_spaces)}")
            # track recursion level
            
        else :
            # track recursion level
            print(f"{spacing}{key}: ")
            display_toppings(value, layer + 1)





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
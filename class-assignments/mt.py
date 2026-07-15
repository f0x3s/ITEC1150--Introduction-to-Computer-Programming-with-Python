# Midterm
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/14/26 - foxes
# modified 7/14/26 - foxes
#
# description: Python-based application to help BTG customers order burgers.
import math

class Customer :
    def __init__(self, name):
        self.name = name
        self.items = []

class Toppings :
    def __init__ (self) :
        self.selected_toppings = {}
        self.menu = TOPPINGS_OPTIONS
    
    def display_menu(self) :
        print(calculate_toppings_display_string(self.menu))

    def display_toppings(self) :
        print(calculate_toppings_display_string(self.selected_toppings))

    def add_topping_to_selected(self, user_topping) :

        validated_topping = validate_customer_input_string(user_topping, self.menu)

        if validated_topping is None :
            raise ValueError(f"We dont have {user_topping}, have you spelled it correctly?")

        if validated_topping[0] in self.selected_toppings.keys() :
            raise ValueError(f"You have already added {validated_topping[0]}")

        
        self.selected_toppings[validated_topping[0]] = validated_topping[1]

        return validated_topping[0]

class Burger(Toppings) :
    def __init__(self, identifier):
        super().__init__()
        self.identifier = identifier
        self.name = None
    
    def check_for_name(self) :
        pass

    def calculate_subtotal(self) :
        pass

HUMAN_NUMBERS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

def human_number(number) :
    return HUMAN_NUMBERS[number]

# for this assignment, I wanted to practice recursion, so I made a nested dict to parse.
TOPPINGS_OPTIONS = {
    "Classic Toppings" : {
        "Lettuce" : 50,
        "Tomatoes" : 50,
        "Pickles" : 75,
        "Raw Onions" : 100
        },

    "Gourmet Toppings" : {
        "Bacon" : 250,
        "Grilled Onions" : 200,
        "Green Peppers" : 150,
        "Jalapenos" : 180,
        "Mushrooms" : 180,
        },

    "Sauces" : {
        "Mayo" : 25,
        "Ketchup" : 25,
        "Mustard" : 25,
        "Sweet and Sour Relish" : 75,
        "BBQ Sauce" : 100,
        "A1 Original Steak Sauce" : 75,
        "Frank's Original Hot Sauce" : 80,
        }
    }

# check if object is integer
def is_integer(value) :
    return int(value) if isinstance(value, int) else False

# format key and value pair as item and price in dollars, offset by some number of spaces
def format_price(item, cents, adj) :
    human_price = int(cents)/100
    extra_spaces = " " * adj
    return extra_spaces + item + ": " + f"${human_price:.2f}"

# iterates over dict object recursively to find all key & value pairs where the value is an integer
# determines maximum length out of all key and value pairs after they have been formatted as item and price in dollars, with no offset spaces
def maximum_length(text) :
    max_length = 0

    for key, value in text.items() :

        if is_integer(value) :
            # lowest level reached
            current_length = len(format_price(key, value, 0))

        else : 
            # not at lowest level, recurse with sub-dict
            current_length = maximum_length(value)

        if current_length > max_length :
            max_length = current_length

    return max_length

# compares length of two strings and returns the difference.
def calculate_str_adj(maximum, text) :
    return abs(maximum - len(text))

def calculate_toppings_display_string(options, layer=0, longest=0, out_string="") :

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
            out_string += f"{spacing}{format_price(key, value, adj_spaces)}\n"

        else :

            # not at lowest level, just print key with proper indentation
            out_string += f"{spacing}{key}: \n"

            # recurse with sub-dict
            out_string = calculate_toppings_display_string(value, layer + 1, longest, out_string)
    
    
    return out_string

def validate_customer_input_integer(test) :
    try : 
        test = int(test)
        if test < 1 :
            raise ValueError('Number cannot be less than 0') 
        
        return test

    except :
        return False

def validate_customer_input_string(test, library) :

    try :
        return test, library[test]
    
    except :

        for value in library.values() :

            if isinstance(value, dict) :
                result = validate_customer_input_string(test, value)
                
                if result is not None :
                    return result

    return None

def center_text(text, reference) :

    reference_width = maximum_length(reference)

    calculate_str_adj(reference_width, text)

    return " " * math.ceil((calculate_str_adj(reference_width, text)/2) + 1) + text

# I wanted to practice string operations, so I added an additional program element
# As a promotional easter egg, creating a named burger applies a slight discount
# Encouraging customers to explore the Menu
# source: https://www.tastingtable.com/2099199/five-guys-burgers-popular-picks-toppings-ranked/
STYLES = {
    "Bacon & BBQ" : ["BBQ sauce", "Bacon", "Grilled onions", "Lettuce" ],
    "All the Way" : ["Grilled Onions", "Mushrooms", "Lettuce", "Pickles", "Tomatoes", "Mustard", "Mayo", "Ketchup"],
    "Veggies" : ["Lettuce", "Tomatoes", "Green Peppers", "Raw Onions", "Pickles", "Ketchup"],
    "Spicy" : ["Cheese", "Jalapenos", "Frank's Original Hot Sauce", "Tomatoes", "Mayonnaise"],
    "Briny Bite" : ["pickles", "Sweet and Sour Relish", "Mustard", "Raw Onions"]
}

print("Welcome to Burgers to Go!")

while(True) :
    print("How many in your party?: ")
    party_count = validate_customer_input_integer(input())
    if party_count :
        break

    else :
        print("Error: Expected an integer of at least 1")

party = []

for individual in range(party_count) :

    if party_count == 1 :
        print(f"\nWhat is your name?: ")
    else : 
        print(f"\n{human_number(individual).capitalize()} party member, what is your name?: ") # output: First party member, what is your name?

    name = input()

    customer = Customer(name)

    while(True) :

        print("\nHow many Burgers would you like?: ")
        burger_count = validate_customer_input_integer(input())

        if burger_count :
            break

        else :
            print("\nError: Expected an integer of at least 1")

    for item in range(burger_count) :

        if burger_count == 1 :
            print(f"\nLet's build your burger!")

        else : 
            print(f"\nLet's build your {human_number(item)} burger!")

        print("You will be prompted for each topping selection individually.\n")

        burger = Burger(f"Burger {item + 1}")

        print(center_text("MENU", burger.menu))

        burger.display_menu()

        while True :
            print("Select Topping (Please enter the name of your selection) or type 'Done': ")
            try :
                selected = input()

                if selected.lower() == "done" :
                    break

                print("Added " + burger.add_topping_to_selected(selected))
            
            except Exception as e:
                print(e)
        


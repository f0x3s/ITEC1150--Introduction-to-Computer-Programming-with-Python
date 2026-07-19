import math

class Topping() :
    def __init__(self, name, price_cents):
        self.name = name 
        self.price_cents = price_cents

class Menu() :
    def __init__(self, toppings):
        self.toppings = toppings
        pass
    
    def __str__(self):
        
        output_list = {}
        output_string = ""

        output_string += center_text("MENU", self.toppings) + "\n"
        longest_menu_str_length = longest_formatted_display_string(self.toppings)


        for name, topping_object in self.toppings.items() :
            price = cents_int_to_dollars_str(topping_object.price_cents)
            sep = calculate_str_adj(longest_menu_str_length, topping_display_str(topping_object)) + 1
            sep = sep * " "

            output_string += f"{topping_object.name}{sep}{price}\n"


        return output_string

class Burger:
    BASE_PRICE_CENTS = 1030

    def __init__(self):
        self.toppings = []

class Order:
    def __init__(self):
        self.burgers = []

def cents_int_to_dollars_str(cents) :
    dollars = cents/100
    dollars = f"${dollars:.2f}"

    return dollars

def topping_display_str(topping_object) :
    return f"{topping_object.name} {cents_int_to_dollars_str(topping_object.price_cents)}"

def longest_formatted_display_string(toppings) :
    longest = ""

    for topping_object in toppings.values() :
        curent_str = topping_display_str(topping_object)
        current_length = len(topping_display_str(topping_object))

        longest = curent_str if current_length > len(longest) else longest
    
    return longest

def center_text(text, reference) :

    reference_width = longest_formatted_display_string(reference)

    calculate_str_adj(reference_width, text)

    return " " * math.ceil((calculate_str_adj(reference_width, text)/2) + 1) + text

# compares length of two strings and returns the difference.
def calculate_str_adj(maximum, text) :
    return abs(len(maximum) - len(text))


MENU = {
        "Lettuce" : Topping("Lettuce", 50),
        "Tomatoes" : Topping("Tomatoes", 50),
        "Pickles" : Topping("Pickles", 75),
        "Raw Onions" : Topping("Raw Onions", 100),

        "Bacon" : Topping("Bacon", 250),
        "Grilled Onions" : Topping("Grilled Onions", 200),
        "Green Peppers" : Topping("Green Peppers", 150),
        "Jalapenos" : Topping("Jalapenos", 180),
        "Mushrooms" : Topping("Mushrooms", 180),

        "Mayo" : Topping("Mayo", 25),
        "Ketchup" : Topping("Ketchup", 25),
        "Mustard" : Topping("Mustard", 25),
        "Sweet and Sour Relish" : Topping("Sweet and Sour Relish", 75),
        "BBQ Sauce" : Topping("BBQ Sauce", 100),
        "A1 Original Steak Sauce" : Topping("A1 Original Steak Sauce", 75),
        "Zoey's Original Hot Sauce" : Topping("Zoey's Original Hot Sauce", 80)
    }

menu = Menu(MENU)

print(menu)

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

    def __init__(self, menu):
        self.toppings = {}
        self.menu = menu

    def add_topping_to_selected(self, user_topping) :

        validated_topping = validate_customer_input_string(user_topping, self.menu)

        if validated_topping is None :
            raise ValueError(f"We dont have {user_topping}, have you spelled it correctly?")

        if validated_topping.name in self.toppings.keys() :
            raise ValueError(f"You have already added {validated_topping.name}")

        self.toppings[validated_topping.name] = validated_topping

        return validated_topping.name

class Order:
    def __init__(self, name):
        self.name = name
        self.burgers = []
    
    def add_burger(self, burger) :
        self.burgers.append(burger)

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

    return " " * math.ceil(calculate_str_adj(reference_width, text)/2) + text

# compares length of two strings and returns the difference.
def calculate_str_adj(maximum, text) :
    return abs(len(maximum) - len(text))

def validate_customer_input_integer(test) :
    try : 
        test = int(test)
        if test < 1 :
            raise ValueError('Number cannot be less than 0') 
        
        return test

    except :
        return False

def validate_customer_input_string(test, library) :

    test = test.lower()
    
    try :
        return library[test]
    
    except :

        for value in library.values() :
  
            if isinstance(value, dict) :
                result = validate_customer_input_string(test, value)
                
                if result is not None :
                    return result

    return None

HUMAN_NUMBERS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

def human_number(number) :
    return HUMAN_NUMBERS[number]
MENU = {
        "lettuce" : Topping("Lettuce", 50),
        "tomatoes" : Topping("Tomatoes", 50),
        "pickles" : Topping("Pickles", 75),
        "raw onions" : Topping("Raw Onions", 100),

        "bacon" : Topping("Bacon", 250),
        "grilled onions" : Topping("Grilled Onions", 200),
        "green peppers" : Topping("Green Peppers", 150),
        "jalapenos" : Topping("Jalapenos", 180),
        "mushrooms" : Topping("Mushrooms", 180),

        "mayo" : Topping("Mayo", 25),
        "ketchup" : Topping("Ketchup", 25),
        "mustard" : Topping("Mustard", 25),
        "Sweet and sour relish" : Topping("Sweet and Sour Relish", 75),
        "bbq sauce" : Topping("BBQ Sauce", 100),
        "a1 original steak sauce" : Topping("A1 Original Steak Sauce", 75),
        "zoey's original hot sauce" : Topping("Zoey's Original Hot Sauce", 80)
    }

menu = Menu(MENU)

print("Welcome to Burgers to Go!")

print(f"\nWhat is your name?: ")

customer = Order(input())

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

    burger = Burger(menu.toppings)

    print(menu)

    while True :
        print("Select Topping (Please enter the name of your selection) or type 'Done': ")
        try :
            selected = input()

            if selected.lower() == "done" :
                break

            print(f"Added {burger.add_topping_to_selected(selected)}\n")
        
        except Exception as e:
            print(e)
    
    customer.add_burger(burger)


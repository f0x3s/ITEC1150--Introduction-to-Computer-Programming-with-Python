import math

WELCOME_MSG = "Welcome to Burgers to Go!"

class Topping() :
    def __init__(self, name, price_cents):
        self.name = name 
        self.price_cents = price_cents

# when menu object called as a string, print the menu
class Menu() :
    def __init__(self, toppings):
        self.toppings = toppings
        pass
    
    def __str__(self):
        
        output_list = {}
        output_string = ""

        # menu header, dynamically centered atop menu items
        output_string += center_text("MENU", self.toppings) + "\n"

        longest_menu_str_length = longest_formatted_display_string(self.toppings)

        for topping_object in self.toppings.values() :

            price = cents_int_to_dollars_str(topping_object.price_cents)

            # insert whitespace between each topping and its price to match longest topping & price string
            sep = calculate_str_adj(longest_menu_str_length, topping_display_str(topping_object)) + 1
            sep = sep * " "
            output_string += f"{topping_object.name}{sep}{price}\n"


        return output_string

class Burger:
    BASE_PRICE_CENTS = 1030

    def __init__(self, menu):
        self.toppings = {}
        self.menu = menu

    def add_topping_to_selected(self, user_topping):

        key = user_topping.strip().lower()

        # check to make sure user has selected valid topping
        validated_topping = validate_customer_input_string(key, self.menu)

        # throw exceptions if topping DNE or duplicate, so loop cna be triggered in main code prompting user again
        if validated_topping is None:
            raise ValueError(
                f"We don't have {user_topping}... have you spelled it correctly?"
            )

        if key in self.toppings:
            raise ValueError(
                f"You have already added {validated_topping.name}"
            )
        
        # add validated topping to self.toppings dict in same format as menu:  <searchable text>: <ToppingObject>
        self.toppings[key] = validated_topping
        # return topping name to display confirmation to user
        return validated_topping.name


class Order:

    def __init__(self, name):
        self.name = name
        self.burgers = []
    
    # when each order is called as a string, return the formatted receipt
    def __str__(self):

        # cut off extraordinarily long names if needed
        display_name = f"{self.name[:16]}..." if len(self.name) > 21 else f"{self.name}"
        output_string = f"\n{display_name}: "
        
        total = 0

        # create section for each burger on receipt
        for index, burger in enumerate(self.burgers):
            base_price = burger.BASE_PRICE_CENTS 

            # burger label & base cost
            output_string += f"\nHamburger {index + 1}:   {cents_int_to_dollars_str(base_price)}\n"

            
            if not burger.toppings :
                output_string += f"- no toppings\n"
            
            # formatted toppign & price line
            for topping_object in burger.toppings.values():
                base_price += topping_object.price_cents

                # if topping name > 10 char, slice and add ... to keep reciept columns lined up.
                # I didn't use the same approach as the menu because responsive-width receipts dont make sense here
                topping_name = f"{topping_object.name[:7]}..." if len(topping_object.name) > 10 else f"{topping_object.name}"
                
                # format each topping line, ensure each topping name + whitespace before price is 13 char minumum (in this case, exactly becaus it can never exceed 10 char)
                output_string += f"- {topping_name:<13} {cents_int_to_dollars_str(topping_object.price_cents)} \n"
            
            total += base_price
            output_string += f"Subtotal:      {cents_int_to_dollars_str(base_price)}\n"

        output_string += "\n---------------------\n"
        output_string += f"Total:         {cents_int_to_dollars_str(total)}"

        # entire reciept
        return output_string

    # add burger to order
    def add_burger(self, burger) :
        self.burgers.append(burger)

# convert price in cents to string formatted as $<dollars>.<cents>
def cents_int_to_dollars_str(cents) :
    dollars = cents/100
    dollars = f"${dollars:02.2f}"

    return dollars

# 'unit' menu display line i.e no whitespace inserted
def topping_display_str(topping_object) :
    return f"{topping_object.name} {cents_int_to_dollars_str(topping_object.price_cents)}"

# uses above function to process each topping object in menu and determine which one is the longest
# to use as formatting reference
# returns longest string
def longest_formatted_display_string(toppings) :
    longest = ""

    # check each new formatted topping string against running longest string
    for topping_object in toppings.values() :
        curent_str = topping_display_str(topping_object)
        current_length = len(topping_display_str(topping_object))

        longest = curent_str if current_length > len(longest) else longest
    
    return longest

# centers text string within longest formatted string from reference, justified one char right if center impossible
def center_text(text, reference) :

    reference_width = longest_formatted_display_string(reference)

    calculate_str_adj(reference_width, text)

    return " " * math.ceil(calculate_str_adj(reference_width, text)/2) + text

# compares length of two strings and returns the difference.
def calculate_str_adj(maximum, text) :
    return abs(len(maximum) - len(text))

# checks for cutomer input is integer greater than 1
def validate_customer_input_integer(test) :
    try : 
        test = int(test)
        if test < 1 :
            raise ValueError('Number cannot be less than 0') 
        
        return test

    except :
        return False

# checks customer input matches key in menu object 
def validate_customer_input_string(test, menu):
    test = test.strip().lower()

    return menu.get(test.strip().lower())

HUMAN_NUMBERS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

# function to convert index integer to ordinal string: 0 == "first", 1 == "second", etc using HUMAN_NUMBERS list
def human_number(number) :
    return HUMAN_NUMBERS[number]

# menu of toppings stored as a dict with normalized lowercase values as keys and each topping object as values
# this is done because menu keys are more natively searchable than values in objects, which would require iteration
# also lets displaymenu/receipt display use special chars like ñ without reuiring user to type them for search
MENU = {
        "lettuce" : Topping("Lettuce", 50),
        "tomatoes" : Topping("Tomatoes", 50),
        "pickles" : Topping("Pickles", 75),
        "raw onions" : Topping("Raw Onions", 100),

        "bacon" : Topping("Bacon", 250),
        "grilled onions" : Topping("Grilled Onions", 200),
        "green peppers" : Topping("Green Peppers", 150),
        "jalapenos" : Topping("Jalapeños", 180),
        "mushrooms" : Topping("Mushrooms", 180),

        "mayo" : Topping("Mayo", 25),
        "ketchup" : Topping("Ketchup", 25),
        "mustard" : Topping("Mustard", 25),
        "sweet and sour relish" : Topping("Sweet and Sour Relish", 75),
        "bbq sauce" : Topping("BBQ Sauce", 100),
        "a1 original steak sauce" : Topping("A1 Original Steak Sauce", 75),
        "zoey's original hot sauce" : Topping("Zoey's Original Hot Sauce", 80)
    }

def main() :
    menu = Menu(MENU)
    
    print(WELCOME_MSG)

    print(f"\nWhat is your name?: ")

    customer = Order(input())

    # prompt user repeatedly for # of burgers until valid input
    while(True) :

        print("\nHow many Burgers would you like?: ")
        burger_count = validate_customer_input_integer(input())

        if burger_count :
            break

        else :
            print("\nError: Expected an integer of at least 1")

    # for each requested burger
    for item in range(burger_count) :

        if burger_count == 1 :
            print(f"\nLet's build your burger!")

        else : 
            print(f"\nLet's build your {human_number(item)} burger!")

        print("You will be prompted for each topping selection individually.\n")

        # create burger with current menu object's toppings dict as options
        burger = Burger(menu.toppings)

        # display menu to user
        print(menu)

        # prompt user until valid topping or done is selected
        while True :
            print("Select Topping (Please enter the name of your selection) or type 'Done': ")
            try :
                selected = input()

                if selected.lower() == "done" :
                    break

                print(f"Added {burger.add_topping_to_selected(selected)}\n")
            
            # print reason for invalid topping (DNE or repeated) as thrown from .add_topping_to_selected() method
            except Exception as e:
                print(e)
        
        customer.add_burger(burger)

    print(customer)

if __name__ == "__main__":
    main()
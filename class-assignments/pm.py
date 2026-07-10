# Practice Midterm
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/9/26 - foxes
# modified 7/9/26 - foxes
#
# description: Python- based application to help customers select toppings for their tacos

class CustomerOrder :
    def __init__(self, name) :
        self.name = name 
        self.order = {}
    
    def build_order(self, options) :
        order = {}

        for option in options:
    
            order[option.name] = []

            done_flag = False

            for index in range(option.max_selections) :
                if done_flag :
                    break
            
                str_index = "" if option.max_selections == 1 else  human_number(index) + " "

                print(f"\nSelect your {str_index}{option.name} (1-{option.count_options()}):") 
                option.display()

                while True :
                    user_input = input()
                    try :
                        user_input = int(user_input)

                        if(option.is_done(user_input)):
                                done_flag = True
                                break
                        
                        user_input = option.get_choice(user_input)

                        order[option.name].append(user_input )
                        break
                
                    except ValueError :
                        print(f"Error, expecting a number between 1 and {option.count_options()}:")
        
        self.order = order

    def display_order(self) :
        print(f"{self.name} :")

        for key, choices in self.order.items() :

            print(f"\t{key.capitalize()}: ", end="")

            selections = ", ".join(choices) if choices else "None"
            print(selections)

            if "Salsa" in choices:
                print("\t\tOne Spicy Taco coming up!")

class MenuItem :
    def __init__(self, name, max_selections, items) :
        self.name = name
        self.max_selections = max_selections
        self.items = items

    def display(self) :
        for index, choice in enumerate(self.items) :
            print(f"{index + 1}. {choice}")

        if self.max_selections > 1 :
            print(f"{len(self.items) + 1}. Done (no more {self.name}s)")
    
    def count_options(self) :
        count = len(self.items) 

        return count + 1 if self.max_selections > 1 else count
    
    def is_done(self, selection) :
        num_options = self.count_options()

        if selection > num_options or selection < 1 :
            raise ValueError("selection not in bounds")

        return self.max_selections > 1 and selection == num_options
    
    def get_choice(self, selection) :
        if selection < 1 or selection > len(self.items) :
            raise ValueError("selection not in bounds")
        
        return self.items[selection - 1]
    
party_count = 0

MAX_TOPPING = 4
MAX_DIP = 2

HUMAN_NUMBERS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

menu_options = [
    MenuItem("tortilla", 
             1, 
             ["Corn", "Flour", "Whole Wheat"]),

    MenuItem("filling", 
             1, 
             ["Beans", "Chicken", "Fish", "Beef"]),

    MenuItem("topping(s)", 
             MAX_TOPPING, 
             ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]),

    MenuItem("side", 
             1, 
             ["White Rice", "Brown Rice", "Beans"]),

    MenuItem("dip(s)", 
             MAX_DIP, 
             ["Red Sauce", "Green Sauce", "Queso Blanco", "Guacamole"]),

    MenuItem("drink", 
             1, 
             ["Mexican Coke", "Jarritos", "Water", "Horchata"])
]

def human_number(number) :
    return HUMAN_NUMBERS[number]

def sanitize_party_count(count, maximum) :
    count = int(count)
    
    if count < 1 or count > maximum:
        raise ValueError("selection not in bounds")
        
    return count



print("Welcome to Catrinas Mexican Grill")
print("Get ready to build your taco(s)...")
max_guests = len(HUMAN_NUMBERS)

print(f"\nHow many are in your party? (maximum {max_guests} guests): ")

while True :
    try :
        party_count = sanitize_party_count(input(),max_guests)
        break
    except ValueError :
        print(f"Expecting an integer between 1 and {max_guests}:")

party_orders = []

for individual in range(party_count):

    party_index = "W" if party_count == 1 else human_number(individual).capitalize() + " party member, w"

    print(f"\n{party_index}hat is your name?: ")
    name = input()

    customer = CustomerOrder(name)
    customer.build_order(menu_options)
    party_orders.append(customer)

print("\nOrder complete!\n")

for customer in party_orders:
    customer.display_order()
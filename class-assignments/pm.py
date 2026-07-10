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
        self.order = query_user(options)

    def display_order(self) :
        print(f"{self.name} :")

        for key in self.order.keys() :

            print(f"\t{key.capitalize()}: ", end="")

            selections = ", ".join(self.order[key]) if self.order[key] else "None"
            print(selections)

            if "Salsa" in self.order[key]:
                print("\t\tOne Spicy Taco coming up!")

class MenuItem :
    def __init__(self, name, items, max_selections)
        self.name = name
        self.max_selections = max_selections
        self.items = items

    def display(self) :
        for index, choice in enumerate(self.choices) :
            print(f"{index + 1}. {choice}")

        if self.max_selections > 1 :
            print(f"{len(self.choices) + 1}. Done (no more {self.name}s)")
    
    def count_options(self) :
        count = len(self.choices) 

        return count + 1 if self.max_selections > 1 else count
    
    def is_done(self, selection)
        num_options = self.count_options()

        if selection > num_options or selection < 1 :
            raise ValueError("selection not in bounds")

        return self.max_selections > 1 and selection == num_options
    
party_count = 0

MAX_TOPPING = 4
MAX_DIP = 2

HUMAN_NUMBERS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

menu_options = {
    MenuItem("tortilla", 
             1, 
             ["Corn", "Flour", "Whole Wheat"]),

    MenuItem("filling", 
             1, 
             ["Beans", "Chicken", "Fish", "Beef"]),

    MenuItem("topping(s)", 
             MAX_TOPPING, 
             ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]),

    MenuItem("dip(s)", 
             MAX_DIP, 
             ["Red Sauce", "Green Sauce", "Queso Blanco", "Guacamole"]),

    MenuItem("drink", 
             1, 
             ["Mexican Coke", "Jarritos", "Water", "Horchata"])
}

def human_number(number) :
    return HUMAN_NUMBERS[number]

def query_user(options) :
    order = {}

    for option in options:
   
        order[option.name] = []

        done_flag = False

        for index in range(option.max_selections) :
            if done_flag :
                break
        
            str_index = "" if option.max_selections == 1 else  human_number(index) + " "

            print(f"\nSelect your {str_index}{option.name} (1-{option.count_options()}):") 
            display_options(options, key)

            while True :
                user_input = input()
                try :
                    user_input = int(user_input)
                    if(is_done(options, key, user_input)) :
                            done_flag = True
                            break
                    
                    user_input = options[key][1][user_input-1]

                    order[key].append(user_input)
                    break
            
                except :
                    print(f"Error, expecting a number between 1 and {count_options(options, key)}:")
    
    return order

def sanitize_party_count(count, max) :
    count = int(count)
    
    if count < 1 or count > max:
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
    except :
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
    customer.displayOrder()
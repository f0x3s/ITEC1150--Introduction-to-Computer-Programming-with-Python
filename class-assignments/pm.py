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
    
    def buildOrder(self, options) :
        self.order = query_user(options)

    def displayOrder(self) :
        print(f"{self.name} :")

        for key in self.order.keys() :

            print(f"\t{key.capitalize()}: ", end="")

            selections = ", ".join(self.order[key]) if self.order[key] else "None"
            print(selections)

            if "Salsa" in self.order[key]:
                print("\t\tOne Spicy Taco coming up!")

party_count = 0

MAX_TOPPING = 4
MAX_DIP = 2

HUMAN_NUMBERS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

menu_options = {
    "tortilla" : (1, ["Corn", "Flour", "Whole Wheat"]),
    "filling" : (1, ["Beans", "Chicken", "Fish", "Beef"]),
    "topping(s)" : (MAX_TOPPING, ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]),
    "dip(s)" : (MAX_DIP, ["Red Sauce", "Green Sauce", "Queso Blanco", "Guacamole"]),
    "drink" : (1, ["Mexican Coke", "Jarritos", "Water", "Horchata"])
}

def display_options(options, key) :
    for index, option in enumerate(options[key][1]) :
        print(f"{index + 1}. {option}")

    if options[key][0] > 1 :
        print(f"{len(options[key][1]) + 1}. Done (no more {key}s)")

def count_options(options, key) :
    count = len(options[key][1]) 

    return count + 1 if options[key][0] > 1 else count

def human_number(number) :
    return HUMAN_NUMBERS[number]

def is_done(options, key, selection) :

    num_options = count_options(options, key)

    if selection > num_options or selection < 1 :
        raise ValueError("selection not in bounds")

    return options[key][0] > 1 and selection == num_options

def query_user(options) :
    order = {}

    for key in options.keys() :
   
        order[key] = []

        num_items = options[key][0]
        done_flag = False

        for index in range(num_items) :
        
            if done_flag :
                print("done")
                break
        
            str_index = "" if num_items == 1 else  human_number(index) + " "

            print(f"\nSelect your {str_index}{key} (1-{count_options(options, key)}):") 
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
    customer.buildOrder(menu_options)
    party_orders.append(customer)

print("\nOrder complete!\n")

for customer in party_orders:
    customer.displayOrder()
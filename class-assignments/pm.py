# Practice Midterm
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/9/26 - foxes
# modified 7/9/26 - foxes
#
# description: Python-based application to help customers select toppings for their tacos

class CustomerOrder :
    def __init__(self, name) :
        self.name = name 
        self.order = {}
    
    # takes list of MenuItem objects as 'options'
    def build_order(self, options) :
        order = {}

        for option in options:
            
            # creates key in order dict for MenuItem object with an empty list as its value
            order[option.name] = []
            
            done_flag = False

            # In my architecture, I felt a for loop made more sense than the while loop asked in the instructions, since max_selections is constant per MenuItem. 
            # If I were to implement a while loop, I would check an incremented index value against option.max_selections.
            for index in range(option.max_selections) :

                # used to break loop if user does not want to select the maximum number of options allowed by MenuItem's max_selections
                if done_flag :
                    break
            
                # for ux; displays 'select your <>' vs 'select your n-th <>' contextually
                str_index = "" if option.max_selections == 1 else  human_number(index) + " "
                print(f"\nSelect your {str_index}{option.name} (1-{option.count_options()}):") 

                option.display()

                while True :
                    user_input = input()
                    try :
                        user_input = int(user_input)

                        # convert integer to named option. Throws ValueError if selection OOB.
                        user_input = option.get_choice(user_input)

                        # exit loop if user selects "Done" for item allowing multiple selections
                        if user_input is None:
                                done_flag = True
                                break

                        # append named option to the list (value) associated with current MenuItem's key in the orders dict.
                        order[option.name].append(user_input)
                        break
                
                    except ValueError :
                        print(f"Error, expecting a number between 1 and {option.count_options()}:")

        self.order = order

    # handles final human-readable output
    def display_order(self) :
        print(f"{self.name} :")

        for key, choices in self.order.items() :
            
            # Name of menu item
            print(f"\t{key.capitalize()}: ", end="")

            # stored user choices
            selections = ", ".join(choices) if choices else "None"
            print(selections)

            if "Salsa" in choices:
                print("\t\tOne Spicy Taco coming up!")

class MenuItem :
    def __init__(self, name, max_selections, choices) :
        self.name = name
        self.max_selections = max_selections
        self.choices = choices

    # print choices
    def display(self) :
        for index, choice in enumerate(self.choices) :
            print(f"{index + 1}. {choice}")

        # incl."done" choice where max_selections allows multiple items
        if self.max_selections > 1 :
            print(f"{len(self.choices) + 1}. Done (no more {self.name})")
    
    # returns # of options
    def count_options(self) :
        count = len(self.choices) 

        # (1) added to first case because items that allow multiple selections also include a 'done' option.
        return count + 1 if self.max_selections > 1 else count
    
    # convert selection integer to named option from choices list, or None if user selects "done" for item allowing multiple selections.
    def get_choice(self, selection):
        
        num_options = self.count_options()

        if selection < 1 or selection > num_options:
            raise ValueError("selection not in bounds")
        
        if self.max_selections > 1 and selection == num_options:
            return None

        return self.choices[selection - 1]
    
party_count = 0

MAX_TOPPING = 4
MAX_DIP = 2

HUMAN_NUMBERS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

# list of MenuItem(<name>, <max qty>, [<choices>]) objects representing orderable menu items. 
# I added a couple additional options to show the scalability of my code.
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

# function to convert index integer to ordinal string: 0 == "first", 1 == "second", etc using HUMAN_NUMBERS list
def human_number(number) :
    return HUMAN_NUMBERS[number]

# make sure party count is between one and some maximum number of people, othewise throwing a ValueError to function within a looped try/except block.
def sanitize_party_count(count, maximum) :
    count = int(count)

    if count < 1 or count > maximum:
        raise ValueError("selection not in bounds")
        
    return count

print("Welcome to Catrinas Mexican Grill")
print("Get ready to build your taco(s)...")
max_guests = len(HUMAN_NUMBERS) # a little cheesy, but guest # limited by number of human-readable numerical strings in HUMAN_NUMBERS. I'm sure there is a module that could handle the conversion better ^.^

print(f"\nHow many are in your party? (maximum {max_guests} guests): ")

# prompts user for # of guests in party (repeatedly, if necessary, until acceptable response given. sanitize_party_count() throws a valueError for unacceptable input, triggering the except block before the break statement).
while True :
    try :
        party_count = sanitize_party_count(input(),max_guests)
        break
    except ValueError :
        print(f"Expecting an integer between 1 and {max_guests}:")

# list for customer objects containing orders
party_orders = []

for individual in range(party_count):

    if party_count == 1 :
        print(f"\nWhat is your name?: ")
    else : 
        print(f"\n{human_number(individual).capitalize()} party member, what is your name?: ") # output: First party member, what is your name?

    name = input()

    customer = CustomerOrder(name)

    # prompt each customer one by one for their order
    customer.build_order(menu_options)

    # store orders (contained within each customer object) in the party_orders list
    party_orders.append(customer)

print("\nOrder complete!\n")

for customer in party_orders:
    customer.display_order()
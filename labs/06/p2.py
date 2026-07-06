# module 6 lab part 2
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/2/26 - foxes
# modified 7/6/26 - foxes
#
# description: Animal Shelter Management System

CAPACITY = 9

# adds new animal to input list as tuple per element (<name>, <species>) and returns copy of list
def add_animal(name, species, input_animals) :
    print(f"Adding: {name}, {species}...")

    # basic cinput check to make sure user has entered both name and species.
    if (species is None or species == "") or (name is None or name == "") : 
        print("\033[91mERROR: Could not add animal. Check name and species.\033[0m") # using ansi color escape codes for compatibility

    else :
        try :
            name = name.lower().replace(" ", "") # pulling double duty to ensure inputs are strings
            species = species.lower().replace(" ", "")

            # use get_animal_count() to check current # of animals against CAPACITY
            if get_animal_count(input_animals) < CAPACITY :
                input_animals.append((name, species))
                print(f"Added {name.capitalize()} the {species}.")
                print(f"Remaining capacity: {CAPACITY-get_animal_count(input_animals)}")
            else :
                print(f"The shelter is at capacity, could not add {name.capitalize()} the {species}.")
            
        except :
            print("\033[91mERROR: Could not add animal. Expecting fomat: <string>, <string>.\033[0m") # using ansi color escape codes for compatibility
     
    return list(input_animals) # copy of input list.

# return a list with each unique species (2nd element of input list's tuples)
def available_species(available) :
    seen = []

    # parse through all species in available list, add first occurrence to buffer
    for individual in available :
        if individual[1] not in seen :
            seen.append(individual[1])
    
    return seen

def adopt_animal(species, input_animals) :

    pending_adoption = []

    for individual in animals :
        if species == individual[1] :
            pending_adoption.append(individual)
    
    if len(pending_adoption) > 1 :

        print(f"\nWe have multiple {plural(species)}:")
        for individual in pending_adoption :
            print(individual[0].capitalize())
        
        print("\nWhich one would you like? Enter their name: ")

        return get_valid_animal(pending_adoption)

# returns number of animals in shelter
def get_animal_count(input_animals) :
    return len(input_animals)

# specialty function for correcting irregular plurals
def plural(animal_type) :
    if animal_type == "mouse" :
        animal_type = "mice"
    else :
        animal_type = animal_type + "s"

    return animal_type 

# recursive functions
def get_valid_species(input_animals) :
    print("\nWhich species would you like?")
    want_species = input()

    if want_species is None or want_species == "" : 
        print("\033[91mERROR: Please enter species of desired animal: .\033[0m") # using ansi color escape codes for compatibility
        return get_valid_species(input_animals)

    want_species = want_species.lower().replace(" ", "") # input() always a string, no need to perform error checking like in add_animal() where we don't use input
        
    if want_species not in available_species(animals) :
        print(f"We don't have any {want_species}s.")
        return get_valid_species(input_animals)

    return want_species

def get_valid_animal(input_pending_adoption) :
    requested_name = input().replace(" ", "").lower()
    success = False

    for individual in input_pending_adoption :
        if requested_name == individual[0] : 
            print(f"\n\x1b[32mYou have adopted: {individual[0].capitalize()} the {individual[1]}.\x1b[0m")
            return individual
            
    print(f"We can't find {requested_name.capitalize()}. Please ensure correct spelling:")
    get_valid_animal(input_pending_adoption)
    
## main program 

animals = [] # empty list to hold animals and species in shelter

# test animals, mix of upper and lower case formatting and additional whitespace to simulate user input.
animals = add_animal("Alice", "cat", animals)
animals = add_animal("red", None, animals)  # incorrect input
animals = add_animal("Bob", "dog", animals)
animals = add_animal("angel", "Cat", animals)
animals = add_animal("Zoey", "cat ", animals)
animals = add_animal("spot", "dog", animals)
animals = add_animal(30, 20, animals) # incorrect input
animals = add_animal("Zeke", "Bird", animals)
animals = add_animal("Moxxy ", "mouse", animals)
animals = add_animal("Nim", "mouse ", animals)
animals = add_animal("", "mouse", animals)
animals = add_animal("Steven", "mouse", animals)
animals = add_animal("poly", "Bird", animals)

print(f"\nWeclome to the animal shelter! We have {get_animal_count(animals)} animals. Current available types are: ")

# return unique species as list, unpack list and split with newlines
print(*available_species(animals), sep="\n")

want_species = get_valid_species(animals)

animals.remove(adopt_animal(want_species, animals))

print(f"\n{get_animal_count(animals)} animals remain.")

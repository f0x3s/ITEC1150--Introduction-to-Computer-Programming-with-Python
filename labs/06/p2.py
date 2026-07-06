# module 6 lab part 2
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/2/26 - foxes
# modified 7/2/26 - foxes
#
# description: Animal Shelter Management System

CAPACITY = 9

# adds new animal to input list as tuplet per element (<name>, <species>) and returns copy of list
def add_animal(name, species, in_list) :
    print(f"Adding: {name}, {species}")

    # basic cinput check to make sure user has entered both name and species.
    if (species is None or species == "") or (name is None or name == "") : 
        print("Could not add animal. Check name and species.")

    else :

        # use get_animal_count() to check current # of animals against CAPACITY
        if get_animal_count() < CAPACITY :
            in_list.append((name, species))
            print(f"Added {name} the {species}.")
            print(f"Remaining capacity: {CAPACITY-get_animal_count()}")
        else :
            print(f"The shelter is at capacity, could not add {name} the {species}.")
    
    return list(in_list) # copy of input list

def available_species(available) :
    seen = []

    # parse through all species in available list, add first occurrence to temporary buffer
    for individual in available :
        if individual[1] not in seen :
            seen.append(individual[1])
    
    return seen

def adopt_animal(species) :

    pending_adoption = []

    for individual in animals :
        if species == individual[1] :
            pending_adoption.append(individual)
    
    if len(pending_adoption) > 1 :

        print(f"We have multiple {species}s:")
        for individual in pending_adoption :
            print(individual[0])
        
        print("\nWhich one would you like? Enter their name: ")

        is_exists = False

        while not is_exists :

            requested_name = input().lower()

            for individual in pending_adoption :
                if requested_name == individual[0].lower() :
                    is_exists = True

                if is_exists : 
                    print(f"you have adopted: {individual[0]}")
                    animals.remove(individual)
                    break;
    else :
        print(f"You have adopted: {pending_adoption[0][0]} the {pending_adoption[0][1]}.")
        animals.remove(pending_adoption[0])

# returns number of animals in shelter
def get_animal_count() :
    return len(animals)


animals = [] # empty list to hold animals and species in shelter

animals = add_animal("alice", "cat", animals)
animals = add_animal("red", None, animals)
animals = add_animal("bob", "dog", animals)
animals = add_animal("angel", "cat", animals)
animals = add_animal("zoey", "cat", animals)
animals = add_animal("spot", "dog", animals)
animals = add_animal("zeke", "bird", animals)
animals = add_animal("moxxy", "mouse", animals)
animals = add_animal("nim", "mouse", animals)
animals = add_animal("steven", "mouse", animals)
animals = add_animal("poly", "bird", animals)

print(f"\nWeclome to the animal shelter! We have {get_animal_count()} animals. Current available types are: ")

# return unique species as list, unpack list and split with newlines
print(*available_species(animals), sep="\n")

while True :
    print("\nWhich species would you like?")
    want_species = input().lower()

    if want_species.lower() not in available_species(animals) :
        print(f"We don't have any {want_species}s.")
    else :
        break

adopt_animal(want_species)
print(animals)

# module 6 lab part 2
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/2/26 - foxes
# modified 7/2/26 - foxes
#
# description: Animal Shelter Management System

animals = []
CAPACITY = 9

def add_animal(name, species) :
    if get_animal_count() < CAPACITY :
        animals.append((name, species))
        print(f"Added {name} the {species}.")
        print(f"Remaining capacity: {CAPACITY-get_animal_count()}")
    else :
        print(f"The shelter is at capacity, could not add {name} the {species}.")

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


def get_animal_count() :
    return len(animals)

add_animal("alice", "cat")
add_animal("bob", "dog")
add_animal("angel", "cat")
add_animal("zoey", "cat")
add_animal("spot", "dog")
add_animal("zeke", "bird")
add_animal("moxxy", "mouse")
add_animal("nim", "mouse")
add_animal("steven", "mouse")
add_animal("poly", "bird")

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

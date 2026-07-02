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
CAPACITY = 4


def add_animal(name, species) :
    animals.append((name, species))

def available_species(available) :
    seen = []

    for individual in available :
        if individual[1] not in seen :
            seen.append(individual[1])
    
    return seen



    


def adopt_animal(species) :

    pending_adoption = []

    for individual in animals :
        if species is individual[1] :
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


def get_animal_count() :
    return len(animals)

add_animal("alice", "human")
add_animal("bob", "human")
add_animal("alice", "cat")

# unpack list and split with newlines
print(*available_species(animals), sep="\n")

# print(animals)

adopt_animal("human")
print(animals)
tortilla =  True
meat = "beef"
cheese = False
salsa = "spicy"
guacamole = False

ingredient_count = 0

print("Welcome to Python's Taco Stand!")

if tortilla:
    print("Great! We have a tortilla to start our taco.")
else:
    print("Oh no! We're out of tortillas. We can't make a taco!")

if meat == "chicken":
    print("Adding some delicious chicken to your taco!")
elif meat == "beef":
    print("Beef it is! Adding some juicy beef to your taco.")
elif meat == "pork":
    print("Pork fan, eh? Adding tasty pork to your taco.")
else:
    print("Looks like we're going vegetarian today!")

if cheese:
    print("Time for some cheese!")
    if salsa == "spicy":
        print("Adding extra cheese to balance out the spicy salsa!")
    else:
        print("Adding a normal amount of cheese.")
    
else:
    print("No cheese on this taco.")

# Optional extension activity using control flow
if tortilla:
    ingredient_count = ingredient_count + 1
if meat is not (None or ""):
    ingredient_count = ingredient_count + 1
if cheese:
    ingredient_count = ingredient_count + 1
if salsa is not (None or ""):
    ingredient_count = ingredient_count + 1
if guacamole:
    ingredient_count = ingredient_count + 1

if ingredient_count > 2:
    print(str(ingredient_count) + " ingredients; fully loaded taco.")
else:
    print(str(ingredient_count) + " ingredients;  light taco coming up!")

# Optional extension activity using casting
ingredient_count = tortilla + bool(meat) + cheese + bool(salsa) + guacamole

print("Recalculated with casting: ")
if ingredient_count > 2:
    print(str(ingredient_count) + " ingredients; fully loaded taco.")
else:
    print(str(ingredient_count) + " ingredients;  light taco coming up!")
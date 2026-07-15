# Midterm
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/14/26 - foxes
# modified 7/14/26 - foxes
#
# description: Python-based application to help BTG customers order burgers.

class Customer :
    def __init__(self):
        pass

class Burger :
    def __init__(self):
        self.toppings = []
        self.name = None
        pass

    def add_topping(self, topping) :
        self.toppings.append(topping)

    def check_for_name(self) :
        pass

TOPPINGS = {
    "Lettuce"
    "Tomatoes"
    "Pickles"
    "Bacon"
    "Grilled Onions"
    "Raw onions"
    "Green peppers"
    "Jalapeños"
    "Mushrooms"
    "Mayonnaise"
    "Ketchup"
    "Mustard"
    "Sweet and Sour Relish"
    "BBQ sauce"
    "A1 Original Steak Sauce"
    "Frank's Original Hot Sauce"
    }

# I wanted to practice string operations, so I added an additional program element
# As a promotional easter egg, creating a named burger applies a slight discount
# Encouraging customers to explore the Menu
# source: https://www.tastingtable.com/2099199/five-guys-burgers-popular-picks-toppings-ranked/
STYLES = {
    "Bacon & BBQ" : ["BBQ sauce", "Bacon", "Grilled onions", "Lettuce" ],
    "All the Way" : ["Grilled Onions", "Mushrooms", "Lettuce", "Pickles", "Tomatoes", "Mustard", "Mayo", "Ketchup"],
    "Veggies" : ["Lettuce", "Tomatoes", "Green Peppers", "Raw Onions", "Pickles", "Ketchup"],
    "Spicy" : ["Cheese", "Jalapeños", "Frank's Original Hot Sauce", "Tomatoes", "Mayonnaise"],
    "Briny Bite" : ["pickles", "Sweet and Sour Relish", "Mustard", "Raw Onions"]
}
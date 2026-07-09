# module 8 lab part 1
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/8/26 - foxes
# modified 7/9/26 - foxes
#
# description: Object Oriented Programming (OOP)

class Animal :
    def __init__(self, name, age) :
        self.name = name
        self.age = age 
    def __str__(self) :
        return f"{self.name} is {self.age} years old"
    def speak(self, sound) :
        return f"{self.name} says {sound}"
    
class Dog(Animal) :
    def speak(self, sound = "Woof"):
        return super().speak(sound)

class Duck(Animal) :
    def speak(self, sound = "Quack"):
        return super().speak(sound)

class Pig(Animal) :
    def speak(self, sound = "Oink"):
        return super().speak(sound)
    
class Cat(Animal) :
    def speak(self, sound = "meow") :
        return super().speak(sound)

bob = Dog("Bob", 5)
zoey = Cat("zoey", 14)
winston = Dog("Winston", 12)
loki = Dog("Loki", 4)
delilah = Cat("Delilah", 2)
howard = Duck("Howard", 52)
babe = Pig("Babe", 30)

menagerie = [bob, zoey, winston, loki, delilah, howard, babe]

for creature in menagerie :
    if isinstance(creature, Animal):
        print(creature)
        print(creature.speak())
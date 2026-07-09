# module 8 lab part 1
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 7/8/26 - foxes
# modified 7/9/26 - foxes
#
# description: Object Oriented Programming (OOP)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
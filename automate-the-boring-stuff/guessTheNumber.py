import random, sys, os, math

print("I am thining of a number between 1 and 20... ")

secret = random.randint(1,20)
tries = 1
ALLOWED_TRIES = 5

for guessesTaken in range(1,7):
    print("Take a guess: ")
    try:
        guess = int(input())
        if guess < secret:
            print("Nope, too low!")
        elif guess > secret:
            print("Nope! too high!")
        else: 
            break
    except:
        print("error! guess must be a numeric input! One guess Used")
try:
    if guess == secret:
        print("You got it!")
    else:
        print(f"Nope! I was thinking of {secret}")
except:
    print("something went wrong.")




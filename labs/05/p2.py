# module 5 lab part 2
# foxes
# Instructor: Corin Dennison
#
# python version 3.14.6
# created 6/30/26 - foxes
# modified 6/30/26 - foxes
#
# description: Dad Joke Generator

import random

# Dad Jokes sourced from: https://www.countryliving.com/life/a27452412/best-dad-jokes/

dad_jokes = ["What kind of shoes to frogs wear? Open-toad sandals.",
             "I just built an ATM that only gives out coins. I don’t know why no one’s thought of it before: it just makes cents!",
             "Did I ever tell you about the time I went mushroom foraging? It’s a story with a morel at the end.",
             "What happened when two slices of bread went on a date? It was loaf at first sight.",
             "Why do crabs never volunteer? Because they're shell-fish.",
             "I had a quiet game of tennis today. There was no racket.",
             "What's a shark's favorite saying? 'Man overboard!'",
             "What did one slice of bread say to the other before the race? You're toast!",
             "I poured some water over a duck's back yesterday. I don't think he cared.",
             "How did I know my girlfriend thought I was invading her privacy? She wrote about it in her diary."
            ]

print("\nThere are " + str(len(dad_jokes)) + " Dad Jokes available.")
print("\nHere are four random Dad Jokes: ")

# Display 4 random jokes with index number starting at 1 preceeding them. 
# Remove each joke after printing so the user cannot see it twice later

for i in range(4):
    joke = random.choice(dad_jokes)
    print(str(i + 1) + ". " + joke)
    dad_jokes.remove(joke)

print("\nThank you!")

# Optional Extension

# Ask User if they want another joke; display and print if yes
# Remove each joke after printing so the user cannot see it twice later

while True: 

    # Check to make sure the dad joke list still contains unseen jokes

    if not len(dad_jokes) :
        print("\nYou've seen all the jokes!")
        break

    print("\nWant Another? (Yes/No)")
    user_choice = input().lower()

    if user_choice in ["yes", "y"] :
        joke = random.choice(dad_jokes) 
        print(joke)
        dad_jokes.remove(joke)

    elif user_choice in ["no", "n"] :
        break
    else :
        print("Error: Incorrect Input")

print("\nQuitting...")
    



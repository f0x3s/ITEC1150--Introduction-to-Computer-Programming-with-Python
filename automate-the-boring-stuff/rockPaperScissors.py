import random, sys, math

wins = 0
losses = 0 
tries = 0

print("Welcome to Rock Paper Scissors!\n")


while True:
    print("Enter your move: Rock, Paper, or Scissors (or End, to stop Playing)")

    user_move = input().lower()
    computer_move = random.randint(0,2) # 0 = rock, 1 = paper, 2 = scissors.

    if user_move in ["rock", "r"]:
        tries += 1
        if computer_move == 0:
            print("It is a Tie...")
        elif computer_move == 1:
            print("Computer Wins!")
            losses += 1
        else:
            print("You Win!")
            wins += 1

    elif user_move in ["paper", "p"]:
        tries += 1
        if computer_move == 0:
            print("You Win!")
            wins += 1
        elif computer_move == 1:
            print("It is a Tie...")
        else:
            print("Computer Wins!")
            losses += 1

    elif user_move in ["scissors", "s"]:
        tries += 1
        if computer_move == 0:
            print("Computer Wins!")
            losses += 1
        elif computer_move == 1:
            print("You Win!")
            wins += 1
        else:
            print("It is a Tie...")
    elif user_move == "end":
        break
    else:
        print("Error - Invalid Input")

print("Thank you for playing!")
print(f"You tried a total of {tries} times and had {wins} wins and {losses} losses.")

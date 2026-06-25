import random

print("Welcome to the Magical Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("But beware, the number could change if you take too long!")

win_count = 0
loss_count = 0

while True:
    win_flag = False
    secret_number = random.randint(1, 100)
    guess_remaining = 5

    for guess_count in range(1, (guess_remaining + 1)) :
        print(f"\nPlease guess a whole number between 1 and 100\n{guess_remaining} guesses left: ")
        
        # Ensure user guess is a whole number between 0 and 100 without using up a guess if OOB or not an int.
        while True :
            player_guess = input()
            try :
                player_guess = int(player_guess)
            except :
                # Reminder if guess is not a whole number
                print("Remember, the guess must be a whole number.\nTry again: ")
            else :
                if player_guess < 1 or player_guess > 100 :
                    # Reminder if guess is a whole number but out of bounds
                    print("Remember, the secret number is between 1 and 100.\nTry again: ")
                else :
                    guess_remaining -= 1
                    break
            
        # Respond to player guess 
        if player_guess < secret_number :
            print("\nNope! Your gusss was too low.")
        elif player_guess > secret_number :
            print("\nNope! Your gusss was too high.")
        else :
            win_flag = True # Setting a flag to later display custom win/lose continue message before exiting
            break

        # Additional encouragement if guess is within 10 
        if abs(player_guess - secret_number) < 10 :
            print("But you were very close...")
    
    # Display custom message for win/lose after guess cycle completes or terminates on win.
    if win_flag :
        print(f"\nCongratulations! {secret_number} was correct!\nKeep the streak going!")
        win_count += 1
    else :
        print(f"\nNot Quite... The secret number was {secret_number}.\nBut don't quit on a loss!")
        loss_count += 1
    
    # prompt user to continue until proper input recieved.
    quit_flag = False 

    while True:
        print("Continue? (Yes/No): ")
        user_is_continue = input().lower()

        if user_is_continue in ["yes", "y"] :
            print("\nPicking a new number...")
            break
        elif user_is_continue in ["no", "n"] :
            quit_flag = True
            break
        else : 
            print("Invalid input. Please type Yes/Y or No/N.\n")

    # quit flag used to brea from game loop 
    if quit_flag :
        print("Quitting...\n")
        break

print("Thanks for playing!")
print(f"You had {win_count} wins and {loss_count} losses, for a total of {win_count+loss_count} games.")
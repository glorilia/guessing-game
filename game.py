"""A number-guessing game."""

from random import randint


MIN_NUM = 0
MAX_NUM = 100


#intro
print("Oh hi there! What's your name? ")

# get player name
player_name = input("(type in your name) ")

# set up variable for lowest score
lowest_score = 1000

while True:
    # choose target number between MIN and MAX constants
    target = randint(MIN_NUM,MAX_NUM)

    #prompt user by name and show range
    print(f"{player_name}, I'm thinking of a number between {MIN_NUM} and {MAX_NUM}.")
    print("Try to guess my number.")
    print(target)

    # set up variable for number of guesses
    num_guesses = 1

    while True:
        # prompt player for their guess
        guess = input("Your guess? ")

        # validate that the input is an integer (continue validating till it is)
        try:
            guess = int(guess)
        except ValueError:
            print("C'mon, you know that's not a number. Try this time.")
            continue

        # make sure guess is between MIN and MAX
        if guess < MIN_NUM or guess > MAX_NUM:
            print(f"Umm, your guess should be between {MIN_NUM} and {MAX_NUM}, remember?")
            continue

        if guess != target:
            #respond with a hint
            if guess > target:
                print("Your guess is too high, try again.")
            if guess < target:
                print("Your guess is too low, try again")

            #increment number of guesses
            num_guesses += 1

        else:
            print(f"You did it, {player_name}! You guessed the number in {num_guesses} tries!")
            
            # display best score
            if num_guesses < lowest_score:
                lowest_score = num_guesses
            print(f"Your best score is {lowest_score}.")
            break

    # ask user if they'd like to play again
    print("Wanna play again?")
    keep_going = input("(Type Y or N) ")
    while keep_going != "Y" and keep_going != "N":
        keep_going = input("You must type Y or N! ")

    if keep_going == "N":
        break





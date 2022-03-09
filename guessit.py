"""
Program: guessit.py
Author: Justin Merwin (jmerwin@grantham.edu)
Purpose: Guess the number game.
"""

import random

# Let's set some variables that'll be used in main().
# This input is proteted by the ValueError exception and by int().
def setGuess():
    while True:
        try:
            max_guesses = int(input("How many guesses should you get? "))
            num_min = int(input("What is the smallest number I should use? "))
            num_max = int(input("What is the largest number I should use? "))
            return max_guesses, num_min, num_max
        except ValueError:
            print("Expecting an integer, try again...")
            continue

# Entry point for the game. A series of if...else statements to control variables.
# If you get errors with the f-strings, try uppdating your Python version (> 3.6).
def main():
    max_guesses, num_min, num_max = setGuess()
    secretNum = random.randint(num_min, num_max)
    guessNum = max_guesses
    while True:
        if guessNum > 0:
            try:
                userGuess = int(input("What is your guess? "))
            except ValueError:
                print("You should guess an integer. ")
                continue
        if userGuess != secretNum and guessNum != 0:
            guessNum = guessNum - 1
            print(f"You guessed wrong! You have {guessNum} guesses remaining.")
        elif userGuess == secretNum:
            print(f"You guessed it right with {guessNum} guesses remaining... Mighty sus of you.")
            guessNum = 0
            break
        else:
            print("You ran out of guesses. Try again. ")
            break

if __name__ == "__main__":
    main()

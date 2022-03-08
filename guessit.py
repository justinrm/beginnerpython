"""
Program: guessit.py
Author: Justin Merwin (jmerwin@grantham.edu)
Purpose: Guess the number game.
"""

import random

def setGuess():
    while True:
        try:
            MAX_GUESSES = int(input("How many guesses should you get? "))
            NUM_MIN = int(input("What is the smallest number I should use? "))
            NUM_MAX = int(input("What is the largest number I should use? "))
            return MAX_GUESSES, NUM_MIN, NUM_MAX
        except ValueError:
            print("Expecting an integer, try again...")
            continue

def main():
    MAX_GUESSES, NUM_MIN, NUM_MAX = setGuess()
    secretNum = random.randint(NUM_MIN, NUM_MAX)
    guessNum = MAX_GUESSES
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

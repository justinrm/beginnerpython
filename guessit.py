"""
Program: guessit.py
Author: Justin Merwin (jmerwin@grantham.edu)
Purpose: A number-guessing game where the user tries to guess the secret number
         within a specified range and limited number of attempts.
"""

import random

def get_game_settings():
    """
    Get game settings from the user, including the number of guesses, 
    and the range of numbers for the secret number.
    
    Returns:
        tuple: max_guesses (int), num_min (int), num_max (int)
    """
    while True:
        try:
            max_guesses = int(input("How many guesses should you get? "))
            num_min = int(input("What is the smallest number I should use? "))
            num_max = int(input("What is the largest number I should use? "))
            
            if num_min >= num_max:
                print("Minimum number should be less than maximum. Try again.")
                continue
            
            return max_guesses, num_min, num_max
        except ValueError:
            print("Expecting an integer, try again...")

def play_guessing_game(max_guesses, num_min, num_max):
    """
    Main game logic: the user guesses a secret number within the range
    with a limited number of attempts.
    
    Args:
        max_guesses (int): The maximum number of guesses allowed.
        num_min (int): The minimum value for the secret number.
        num_max (int): The maximum value for the secret number.
    """
    secret_number = random.randint(num_min, num_max)
    remaining_guesses = max_guesses
    
    print(f"\nI have selected a secret number between {num_min} and {num_max}.")
    print(f"You have {max_guesses} guesses to find it. Good luck!\n")
    
    while remaining_guesses > 0:
        try:
            user_guess = int(input(f"Enter your guess ({remaining_guesses} guesses left): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} with {remaining_guesses} guesses remaining!")
            return
        elif user_guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        
        remaining_guesses -= 1

    print(f"Game over! You've run out of guesses. The secret number was {secret_number}.")

def main():
    """
    Entry point of the game.
    """
    max_guesses, num_min, num_max = get_game_settings()
    play_guessing_game(max_guesses, num_min, num_max)

if __name__ == "__main__":
    main()

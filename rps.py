import random

# Map numeric choices to their string equivalents
choices = {
    1: "rock",
    2: "paper",
    3: "scissors",
}

# Get user details and game configuration
user_name = input("What is your name? ").strip()
rounds = int(input(f"How many rounds would you like to play, {user_name}? \n>>> "))
wins, ties, losses = 0, 0, 0

def display_score():
    """
    Display the current score.
    """
    print(f"{user_name}, you have {wins} win(s), {ties} tie(s), and {losses} loss(es).")

def determine_winner(user_choice, computer_choice):
    """
    Determine the outcome of a single round of Rock-Paper-Scissors.
    
    Args:
        user_choice (int): The user's choice (1: Rock, 2: Paper, 3: Scissors).
        computer_choice (int): The computer's randomly chosen move.
        
    Returns:
        str: The outcome ("win", "loss", or "tie").
    """
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == 1 and computer_choice == 3) or \
       (user_choice == 2 and computer_choice == 1) or \
       (user_choice == 3 and computer_choice == 2):
        return "win"
    return "loss"

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num} of {rounds}")
    
    try:
        user_choice = int(input(f"What is your choice, {user_name}? \n 1: Rock \n 2: Paper \n 3: Scissors \n>>> "))
        if user_choice not in choices:
            print("Invalid choice! Please choose 1, 2, or 3.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    computer_choice = random.randint(1, 3)
    outcome = determine_winner(user_choice, computer_choice)

    print(f"{user_name} chose {choices[user_choice]}, and the computer chose {choices[computer_choice]}.")

    if outcome == "win":
        wins += 1
        print(f"Congratulations {user_name}, you won this round!")
    elif outcome == "tie":
        ties += 1
        print(f"It's a tie, {user_name}.")
    else:
        losses += 1
        print(f"Uh oh, {user_name}, you lost this round.")

    display_score()

print(f"\nThe game has ended after {rounds} rounds.")
print(f"Final score: {wins} win(s), {ties} tie(s), and {losses} loss(es).")

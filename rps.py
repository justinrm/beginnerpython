import random

choices = {
    1: "rock",
    2: "paper",
    3: "scissors",
}
user_name = str(input("What is your name? ").strip())
rounds = int(input(f"How many rounds would you like to play, {user_name}? \n >>> "))
wins = 0
ties = 0
losses = 0

def userWin():
           print(f"{user_name} chose " + choices.get(user_choice) + " and the computer chose " + choices.get(npc_choice) + f"! {user_name} won!")
           keepScore()

def keepScore():
    print(f"{user_name}, you have {wins} win(s), {ties} tie(s), and {losses} loss(es).")

for i in range(rounds):
    user_choice = int(input(f"What is your choice, {user_name}? \n 1: Rock \n 2: Paper \n 3: Scissors \n >>> "))
    npc_choice = random.randint(1,3)
    if user_choice == npc_choice:
        ties += 1
        print(f"{user_name}, you tied with the computer. You both chose " + choices.get(user_choice) + ".")
        keepScore()
    elif user_choice == 1 and npc_choice == 3:
        wins += 1
        userWin()
    elif user_choice == 2 and npc_choice == 1:
        wins += 1
        userWin()
    elif user_choice == 3 and npc_choice == 2:
        wins += 1
        userWin()
    else:
        losses += 1
        print(f"Uh oh! {user_name} chose " + choices.get(user_choice) + " and the computer chose " + choices.get(npc_choice) + f"... {user_name} lost!")
        keepScore()

print(f"The game has ended after {rounds} rounds.")

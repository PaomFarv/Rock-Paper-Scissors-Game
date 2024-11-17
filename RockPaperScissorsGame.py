import random

 
game_elements = {"R": "Rock", "P": "Paper", "S": "Scissors"}
winning_combos = {
"R": "S",  # Rock beats Scissors
"P": "R",  # Paper beats Rock
"S": "P"   # Scissors beats Paper
}

print("Welcome to the game 'Rock-Paper-Scissors'.\nDeveloped by Paom Farv.")
print("\n(S) to Start the game.\n(A) to Play again.\n(Q) To Quit.")

user_wins = 0
computer_wins = 0
ties = 0

while True:
    user_choice = input("\nYour response (S,A,Q): ").upper().strip()
    if user_choice == 'Q':
        print("You are out of the game.")
        break
    elif user_choice in {'S', 'A'}:
        user_response = input("\n(R) Rock, (P) Paper or (S) Scissors? ").upper().strip()
        if user_response not in game_elements:
            print("Invalid choice. Please try again.")
            continue
        
        user_pick = game_elements[user_response]
        comp_pick = random.choice(list(game_elements.values()))
        
        print(f"\nYour pick: {user_pick}")
        print(f"My pick: {comp_pick}")
        
        if user_pick == comp_pick:
            print("Oops! It's a Tie.")
            ties += 1
        elif winning_combos[user_response] == comp_pick[0]:  # Check using first letter of comp_pick
            print("You won!")
            user_wins += 1
        else:
            print("Yay! I won.")
            computer_wins += 1
    else:
        print("Invalid input. Please try again.")

print(f"\nYou won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print(f"There were {ties} ties.\n")
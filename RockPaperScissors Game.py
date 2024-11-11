import random

def rps():
    game_elements = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    winning_combos = {
        "R": "S",  # Rock beats Scissors
        "P": "R",  # Paper beats Rock
        "S": "P"   # Scissors beats Paper
    }
    
    print("Welcome to the game 'Rock-Paper-Scissors'.\nDeveloped by Paom Farv.")
    print("\n(S) to Start the game.\n(A) to Play again.\n(Q) To Quit.")
    
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
            elif winning_combos[user_response] == comp_pick[0]:  # Check using first letter of comp_pick
                print("You won!")
            else:
                print("Yay! I won.")
        else:
            print("Invalid input. Please try again.")

rps()
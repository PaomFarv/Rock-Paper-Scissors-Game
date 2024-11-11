import random  # For generating random guesses

def computer_guess():
    print("Welcome to the game 'Number Guesser'.\nDeveloped by PaomFarv.\n\n(S) to Start the game.\n(A) to Play again.\n(Q) To Quit.")
    
    while True:
        user_choice = input("\nYour response (S, A, Q): ").upper().strip()
        
        if user_choice in ('S', 'A'):
            # Set the guessing range based on user input
            try:
                low = int(input("Lowest Range: "))
                high = int(input("Highest Range: "))
            except ValueError:
                print("Invalid input. Please enter valid integers for the range.")
                continue

            # Check if the range is valid
            if low >= high:
                print("Invalid range! Please ensure the lowest number is less than the highest number.")
                continue

            while True:
                # Make an initial guess
                guess = random.randint(low, high)
                print(f"\nMy guess is {guess}")

                # Ask if the guess is correct, too low, or too high
                user_response = input("\nIs my guess correct? \n(Y) Yes\n(L) Too low\n(H) Too high\n").upper().strip()

                if user_response == 'L':  # Guess is too low
                    low = guess + 1  # Adjust range to higher numbers
                    
                elif user_response == 'H':  # Guess is too high
                    high = guess - 1  # Adjust range to lower numbers

                elif user_response == 'Y':  # Guess is correct
                    print("Yay! I guessed your number!")
                    break  # Exit guessing loop

                else:
                    print("Invalid Input. Please try again.")  # Handle wrong inputs
            
        elif user_choice == 'Q':
            print("You are out of the game.")
            break
        
        else:
            print("Invalid Input. Please try again.")

computer_guess()  # Start the game
import random
def get_user_choice():
    # Prompt the user to choose Rock, Paper, or Scissors
    print("Please choose:")
    print("1. Snake")
    print("2. Water")
    print("3. Gun")
    choice = input("Enter the number of your choice: ")

    # Map the user's input to the corresponding choice
    if choice == '1':
        return 'Snake'
    elif choice == '2':
        return 'Water'
    elif choice == '3':
        return 'Gun'
    else:
        # Handle invalid input
        print("Invalid choice, please try again.")
        return get_user_choice()


def get_computer_choice():
    # Randomly select Rock, Paper, or Scissors for the computer
    choices = ['Snake', 'Water', 'Gun']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the choices
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Snake' and computer_choice == 'Water') or \
            (user_choice == 'Water' and computer_choice == 'Gun') or \
            (user_choice == 'Gun' and computer_choice == 'Snake'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    # Main function to play the game
    print("Welcome to Snake, Water, Gun!")

    user_choice = get_user_choice()  # Get user's choice
    computer_choice = get_computer_choice()  # Get computer's choice

    # Show both choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine and display the winner
    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")


# Start the game
play_game()

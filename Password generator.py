import random
import string


# Function to generate a random password
def generate_password(length, use_uppercase, use_numbers, use_special):
    # Base character set: lowercase letters
    characters = string.ascii_lowercase

    # Add uppercase letters if required
    if use_uppercase:
        characters += string.ascii_uppercase

    # Add digits if required
    if use_numbers:
        characters += string.digits

    # Add special characters if required
    if use_special:
        characters += string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


# Function to handle user input and generate the password
def password_generator():
    print("Welcome to the Password Generator!")

    # Get the desired password length from the user
    length = int(input("Enter the desired password length: "))

    # Ask the user if they want to include uppercase letters
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    # Ask the user if they want to include numbers
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'

    # Ask the user if they want to include special characters
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password based on user choices
    password = generate_password(length, use_uppercase, use_numbers, use_special)

    # Display the generated password
    print(f"Your generated password is: {password}")


# Run the password generator
password_generator()



import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def main():
    print("Welcome to the Password Generator")

    # Prompt user to specify the password length
    length = int(input("Enter the desired length for the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()


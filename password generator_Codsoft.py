import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------------")

    # Prompt the user to specify  length of the password
    while True:
        try:
            length = int(input("Enter your password length (min 5): "))
            if length < 5:
                print("Password length must be at least 5 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter the password length.")

    # Generate password
    password = generate_password(length)

    # Display the password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
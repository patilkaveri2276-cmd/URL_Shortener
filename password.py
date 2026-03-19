import json
import random
import string

FILE_NAME = "passwords.json"

# Load existing passwords
def load_passwords():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save passwords
def save_passwords(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Generate strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

# Add new password
def add_password():
    site = input("Enter website/app name: ")
    username = input("Enter username: ")
    password = input("Enter password (leave blank to generate): ")

    if password == "":
        password = generate_password()
        print("Generated Password:", password)

    data = load_passwords()

    data[site] = {
        "username": username,
        "password": password
    }

    save_passwords(data)
    print("Password saved successfully!")

# Retrieve password
def get_password():
    site = input("Enter website name: ")
    data = load_passwords()

    if site in data:
        print("Username:", data[site]["username"])
        print("Password:", data[site]["password"])
    else:
        print("No record found!")

# Main menu
def main():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Generate Password")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            print("Generated Password:", generate_password())
        elif choice == "4":
            break
        else:
            print("Invalid choice")

main()

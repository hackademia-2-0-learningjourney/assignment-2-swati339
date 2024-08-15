
import json
import os

user_data_file = "users.json"

def load_user_data():
    if os.path.exists(user_data_file):
        with open(user_data_file, "r") as file:
            return json.load(file)
    return {}

def save_user_data(users):
    with open(user_data_file, "w") as file:
        json.dump(users, file, indent=4)

def sign_up(users):
    username = input("Enter Username: ")
    if username in users:
        print("Username already exists! Please choose a different username.")
        return
    
    password = input("Enter Password: ")
    contact = input("Enter Mobile Number: ")

    users[username] = {
        "password": password,
        "contact": contact
    }


    save_user_data(users)
    print("User signed up successfully!")

def sign_in(users):
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username]["password"] == password:
        print(f"Welcome to the device, {username}!")
        print(f"Your Mobile Number: {users[username]['contact']}")
    else:
        print("Incorrect credentials!")
        exit()

def main():
    users = load_user_data()

    while True:
        print("1. Sign Up")
        print("2. Sign In")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            sign_up(users)
        elif choice == "2":
            sign_in(users)
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()

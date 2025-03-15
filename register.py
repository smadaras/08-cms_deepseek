import json
import os

USERS_FILE = "users.json"

# Load users from file
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

# Register a new user
def register_user():
    users = load_users()
    while True:
        username = input("Enter a username: ")
        if username in users:
            print("Username already exists. Please choose a different one.")
        else:
            break
    password = input("Enter a password: ")
    users[username] = password
    save_users(users)
    print("Registration successful!")

if __name__ == "__main__":
    register_user()
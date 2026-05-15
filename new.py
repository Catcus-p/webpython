import csv
import os

FILENAME = "logindetails.csv"


# Create file with headers if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])


# Add new login details
def add_new():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("Login details added successfully.\n")


# Search login details
def search_login():
    search_username = input("Enter username to search: ")

    found = False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            if row[0] == search_username:
                print("\nLogin Details Found")
                print("Username:", row[0])
                print("Password:", row[1])
                found = True
                break

    if not found:
        print("Login details not found.\n")


# List all login details
def list_all():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        print("\nAll Login Details")
        print("--------------------------")

        for row in reader:
            print(row[0], "\t", row[1])

    print()


# Main menu
while True:
    print("===== LOGIN DETAILS MENU =====")
    print("1. Add New")
    print("2. Search Login Details")
    print("3. List All Login Details")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_new()

    elif choice == "2":
        search_login()

    elif choice == "3":
        list_all()

    elif choice == "4":
        print("Program exited.")
        break

    else:
        print("Invalid choice.\n")
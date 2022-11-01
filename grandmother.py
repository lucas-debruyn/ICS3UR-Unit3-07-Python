#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: October 2022
# This program tells a user if they are allowed to date my grandchild.


def main():
    # This function determines if they can date my grandchild

    # Input
    user_age = input("Enter your age: ")

    # Process and Output
    try:
        user_age_number = int(user_age)
        if user_age_number > 40 or user_age_number < 25:
            print("\nYou can not date my grandchild.")
        else:
            print("\nYou can date my grandchild!")
    except Exception:
        print("\nPlease input a valid number.")

    print("\nDone.")


if __name__ == "__main__":
    main()

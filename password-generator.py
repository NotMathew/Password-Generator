import random
import string
import pyperclip
import os
from datetime import datetime


def generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))


def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def get_character_set_choice():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    while True:
        print("\nChoose character sets to include in the password:")
        print("1. Lowercase letters (a-z)")
        print("2. Uppercase letters (A-Z)")
        print("3. Digits (0-9)")
        print("4. Special characters (!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~)")
        print("5. All character sets")

        choices = input("Enter the numbers of your choices (e.g., 1234 for all, or 5 for all): ")

        if not choices:
            print("Error: You must enter at least one choice. Please try again.")
            continue

        if not all(char in '12345' for char in choices):
            print("Error: Invalid input. Please use only numbers 1-5.")
            continue

        selected_chars = ""
        if '5' in choices or choices == '1234':
            selected_chars = lowercase + uppercase + digits + special_chars
        else:
            if '1' in choices:
                selected_chars += lowercase
            if '2' in choices:
                selected_chars += uppercase
            if '3' in choices:
                selected_chars += digits
            if '4' in choices:
                selected_chars += special_chars

        if not selected_chars:
            print("Error: You must select at least one character set. Please try again.")
            continue

        return selected_chars


def export_to_file(passwords):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_passwords_{timestamp}.txt"

    try:
        with open(filename, 'w') as file:
            for i, password in enumerate(passwords, 1):
                file.write(f"{i}. {password}\n")
        print(f"Passwords have been exported to {filename}")
        return True
    except IOError:
        print("Error: Unable to write to file. Please check your permissions and try again.")
        return False


def main():
    password_length = get_positive_integer_input("Enter the desired password length: ")
    num_passwords = get_positive_integer_input("Enter the number of passwords to generate: ")

    character_set = get_character_set_choice()

    while True:
        print("\nGenerated Passwords:")
        generated_passwords = []
        for i in range(num_passwords):
            password = generate_password(password_length, character_set)
            generated_passwords.append(password)
            print(f"{i + 1}. {password}")

        while True:
            print("\nWhat would you like to do with the generated passwords?")
            print("1. Copy to clipboard")
            print("2. Export to text file")
            print("3. Both copy to clipboard and export to file")
            print("4. Regenerate passwords")
            print("5. Exit without saving")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                passwords_text = "\n".join(generated_passwords)
                pyperclip.copy(passwords_text)
                print("All passwords have been copied to your clipboard.")
                return
            elif choice == '2':
                export_to_file(generated_passwords)
                return
            elif choice == '3':
                passwords_text = "\n".join(generated_passwords)
                pyperclip.copy(passwords_text)
                export_to_file(generated_passwords)
                print("All passwords have been copied to your clipboard and exported to a file.")
                return
            elif choice == '4':
                print("Regenerating passwords...")
                break
            elif choice == '5':
                print("Exiting without saving passwords.")
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

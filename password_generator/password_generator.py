import random
import string
import pyperclip  # You may need to install this with: pip install pyperclip

def get_user_input():
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return None, None
    except ValueError:
        print("Please enter a valid number.")
        return None, None

    print("Include the following in the password:")
    include_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits (0-9)? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols (!@#...)? (y/n): ").lower() == 'y'
    auto_copy = input("Copy password to clipboard automatically? (y/n): ").lower() == 'y'

    if not any([include_upper, include_lower, include_digits, include_symbols]):
        print("You must select at least one character type!")
        return None, None

    return {
        "length": length,
        "upper": include_upper,
        "lower": include_lower,
        "digits": include_digits,
        "symbols": include_symbols,
        "copy": auto_copy
    }, length

def generate_password(options):
    char_pool = ""
    if options["upper"]:
        char_pool += string.ascii_uppercase
    if options["lower"]:
        char_pool += string.ascii_lowercase
    if options["digits"]:
        char_pool += string.digits
    if options["symbols"]:
        char_pool += string.punctuation

    password = ''.join(random.choices(char_pool, k=options["length"]))

    return password

def password_strength(length):
    if length < 6:
        return "Weak ❌"
    elif 6 <= length < 10:
        return "Moderate ⚠️"
    else:
        return "Strong ✅"

# --- Main Program ---
options, length = get_user_input()
if options:
    password = generate_password(options)
    print("\nGenerated Password:", password)
    print("Password Strength:", password_strength(length))

    if options["copy"]:
        try:
            pyperclip.copy(password)
            print("(✔) Password copied to clipboard.")
        except Exception as e:
            print("(!) Could not copy to clipboard:", e)

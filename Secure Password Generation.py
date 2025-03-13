#!/usr/bin/env python3

import string
import secrets
import random
import time


def new_password(length=12):
    if length < 12:
        raise ValueError("Password length must be at least 12 characters.")

    # Ensure at least one character from each category
    pwd_chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Fill the rest of the password length
    available_chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length - 4):
        pwd_chars.append(secrets.choice(available_chars))

    random.SystemRandom().shuffle(pwd_chars)
    return ''.join(pwd_chars)


def check_password(pwd):
    # Define the requirements
    requirements = {
        "Minimum 12 characters": len(pwd) >= 12,
        "Uppercase letter": any(ch.isupper() for ch in pwd),
        "Lowercase letter": any(ch.islower() for ch in pwd),
        "Digit": any(ch.isdigit() for ch in pwd),
        "Special character": any(ch in string.punctuation for ch in pwd)
    }
    # Determine which requirements are not met
    missing = [req for req, met in requirements.items() if not met]
    if not missing:
        return "Strong password."
    elif len(missing) == 1:
        return "Moderate password. Missing: " + ', '.join(missing)
    else:
        return "Weak password. Missing: " + ', '.join(missing)


def otp_verification():
    otp = random.randint(100000, 999999)
    print("Your one-time password is:", otp)
    start_time = time.time()
    user_otp = input("Enter OTP: ")
    duration = time.time() - start_time

    if duration > 60:
        print("OTP expired. Please try again.")
        return False
    if user_otp == str(otp):
        print("OTP verified. Login successful.")
        return True
    else:
        print("Incorrect OTP.")
        return False


def run_app():
    while True:
        print("\n╔══════════════════════════╗")
        print("║   Secure Password & MFA  ║")
        print("╠══════════════════════════╣")
        print("║ 1. Generate New Password ║")
        print("║ 2. Evaluate Password     ║")
        print("║ 3. OTP Verification      ║")
        print("║ 4. Exit                  ║")
        print("╚══════════════════════════╝")

        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            try:
                pwd = new_password()
                print("Generated password:", pwd)
            except Exception as e:
                print("Error:", e)
        elif choice == "2":
            pwd_input = input("Enter password to check: ")
            result = check_password(pwd_input)
            print("Result:", result)
        elif choice == "3":
            otp_verification()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid option.")


if __name__ == '__main__':
    run_app()

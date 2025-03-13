import string
import secrets
import random
import time

def generate_password(length=12):
    if length < 12:
        raise ValueError("Password length must be at least 12 characters.")
    password_chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

def verify_password(password):
    criteria = {
        "length (>=12 characters)": len(password) >= 12,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special": any(c in string.punctuation for c in password)
    }
    missing = [name for name, passed in criteria.items() if not passed]
    if not missing:
        return "Strong password."
    elif len(missing) == 1:
        return f"Moderate password. Missing: {', '.join(missing)}."
    else:
        return f"Weak password. Missing: {', '.join(missing)}."

def mfa_otp():
    otp = random.randint(100000, 999999)
    print(f"Your OTP is: {otp}")
    start_time = time.time()
    user_input = input("Enter the OTP: ")
    elapsed_time = time.time() - start_time
    if elapsed_time > 60:
        print("OTP expired! Please try again.")
        return False
    elif user_input == str(otp):
        print("MFA Successful!")
        return True
    else:
        print("Invalid OTP!")
        return False

def main():
    while True:
        print("\nMenu:")
        print("1. Generate a new password")
        print("2. Test password strength")
        print("3. Verify login using OTP-based MFA")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            new_password = generate_password()
            print("Generated password:", new_password)
        elif choice == '2':
            pwd = input("Enter the password to verify: ")
            feedback = verify_password(pwd)
            print(feedback)
        elif choice == '3':
            mfa_otp()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()


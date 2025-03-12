# Secure-Password-Generation-and-MFA
This project is implemented in Python and demonstrates secure password generation, password strength verification, and a simulation of OTP-based Multi-Factor Authentication (MFA).

Features
Secure Password Generation

Generates a password of at least 12 characters.
Ensures the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
Utilizes the secrets module for cryptographically strong random choices.
Randomly shuffles the characters to create an unpredictable password.
Password Strength Verification

Evaluates whether a password meets the following criteria:
Minimum length of 12 characters.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Contains at least one digit.
Contains at least one special character.
Provides descriptive feedback indicating if the password is strong, moderate (if one criterion is missing), or weak (if multiple criteria are missing).
OTP-Based Multi-Factor Authentication (MFA)

Generates a 6-digit one-time password (OTP).
The OTP is valid for 60 seconds.
Prompts the user to input the OTP, verifying both its correctness and the time taken to respond.
Simulates a simple MFA flow, where successful entry of the OTP within the allowed time results in authentication.
How to Run
Prerequisites

Python 3.x is required to run this project.
Steps

Clone the repository or copy the code into a file named, for example, secure_mfa.py.
Open a terminal (or your preferred development environment) and navigate to the project directory.
Execute the script with:
bash
Copy
python secure_mfa.py
Follow the on-screen menu to:
Generate a new password.
Test a password’s strength.
Simulate OTP-based MFA.
Exit the program.
Code Overview
Password Generation (generate_password)

Raises an error if the requested password length is less than 12.
Ensures the inclusion of at least one uppercase letter, one lowercase letter, one digit, and one special character.
Completes the password with random characters from a combined set and shuffles them.
Password Verification (verify_password)

Checks if a given password meets all secure criteria.
Provides feedback on which criteria are met or missing.
OTP-Based MFA (mfa_otp)

Generates a random 6-digit OTP.
Displays the OTP and measures the response time.
Validates that the OTP is correct and that the input is received within 60 seconds.
Main Menu (main)

Offers an interactive menu to access the different functionalities.
Continues running until the user opts to exit.
This project is built using Python and showcases secure coding practices for password generation and basic MFA implementation.

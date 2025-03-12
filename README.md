# Secure-Password-Generation-and-MFA

This project is implemented in Python and demonstrates secure password generation, password strength verification, and a simulation of OTP-based Multi-Factor Authentication (MFA).

## Features

- **Secure Password Generation**
  - Generates a password of at least 12 characters.
  - Ensures inclusion of:
    - At least one uppercase letter.
    - At least one lowercase letter.
    - At least one digit.
    - At least one special character.
  - Uses the `secrets` module for cryptographically strong random choices.
  - Randomly shuffles the characters to create an unpredictable password.

- **Password Strength Verification**
  - Evaluates if a password meets the following criteria:
    - Minimum length of 12 characters.
    - Contains an uppercase letter.
    - Contains a lowercase letter.
    - Contains a digit.
    - Contains a special character.
  - Provides descriptive feedback:
    - **Strong** if all criteria are met.
    - **Moderate** if one criterion is missing.
    - **Weak** if multiple criteria are missing.

- **OTP-Based Multi-Factor Authentication (MFA)**
  - Generates a 6-digit one-time password (OTP).
  - OTP is valid for 60 seconds.
  - Prompts the user to input the OTP, verifying:
    - The correctness of the OTP.
    - That the OTP is entered within the allowed time.
  - Simulates a simple MFA flow for user authentication.

  ## Code Overview

- **`generate_password` Function**
  - Raises an error if the requested length is less than 12.
  - Ensures the generated password includes at least one character from each required category.
  - Completes the password with random characters from a combined set and shuffles them.

- **`verify_password` Function**
  - Checks if a given password meets secure criteria.
  - Returns feedback indicating which criteria are met or missing.

- **`mfa_otp` Function**
  - Generates a random 6-digit OTP.
  - Displays the OTP and tracks the response time.
  - Validates that the OTP is correct and the input is received within 60 seconds.

- **`main` Function**
  - Provides an interactive menu to access the different functionalities.
  - Runs continuously until the user opts to exit.


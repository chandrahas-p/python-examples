"""Criteria
At least 8 characters
Contains both uppercase and lowercase letters
Contains at least one digit
Contains at least one special character (like !@#$%^&*()_+)"""


def check_password_strength(password):
    # Criteria flags
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    # Count met criteria
    score = sum([length, has_upper, has_lower, has_digit, has_special])

    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Print results
    print(f"Password Strength: {strength}")
    print(f"- Length >= 8: {length}")
    print(f"- Has uppercase: {has_upper}")
    print(f"- Has lowercase: {has_lower}")
    print(f"- Has digit: {has_digit}")
    print(f"- Has special character: {has_special}")


user_password = input("Enter your password: ")
check_password_strength(user_password)

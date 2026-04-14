import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&+=!]", password):
        strength += 1

    if strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium"
    else:
        return """Weak
        Suggestion: Use uppercase, numbers, and special characters"""


password = input("Enter password: ")
print("Strength:", check_password_strength(password))

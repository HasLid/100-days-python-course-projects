import random

print("Welcome to password generator!")

import string
import secrets

def generate_password(length=16, use_digits=True, use_symbols=True):
    # Base character set always includes lowercase and uppercase letters
    chars = string.ascii_letters 
    
    # Optionally add numbers and punctuation
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    # Guard against an empty character pool
    if not chars:
        raise ValueError("No character types selected.")

    # Generate a cryptographically secure password
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    
    # Generate a default 16-character strong password
    default_pwd = generate_password()
    print(f"Default Password: {default_pwd}")
    
    # Generate a custom 12-character alphanumeric password (no symbols)
    custom_pwd = generate_password(length=12, use_symbols=False)
    print(f"Custom Password:  {custom_pwd}")
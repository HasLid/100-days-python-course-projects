
import random

print("Welcome to password generator!")
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
password = ""

for _ in range(12):
    password += random.choice(alphabet)

print("Generated password: ", password)
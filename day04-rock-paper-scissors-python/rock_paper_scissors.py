import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
User_choice = int(input("What do you chose?, type 0 for rock, 1 for paper, 2 for scissors. \n"))
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if User_choice == computer_choice:
    print("it's a draw.")

elif (User_choice == 0 and computer_choice == 2) or\
    (User_choice == 2 and computer_choice == 1) or\
    (User_choice == 1 and computer_choice == 0):
    print("You win!")
elif User_choice >= 0 and computer_choice <= 2:
    print("You win!")

elif User_choice > computer_choice:
    print("You win!")

elif computer_choice > User_choice:
    print("You lose!")

    print(game_images[User_choice])
elif User_choice not in [0, 1, 2]:
    print("Invalid input!")

else:
    print("You lose!")
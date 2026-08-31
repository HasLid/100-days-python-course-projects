print("Welcome to Treasure Island.")
print("Your mission is to find the missing treasure.")

choice1 = input('You\'re at a crossroad. Where do you want to go? ' 'Type "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to lake. There is a boat coming to pick you up.\n Type "wait" to wait for a boat, or "swim" to swim across: ').lower()
    
    if choice2 == "wait":
        choice3 = input('There are 3 doors available here to choose one.\nType "green" for green door, "red" for red door, or "yellow" for yellow door: ').lower()

        if choice3 == "green":
            print("You're welcome to the treasure room.")
            print("congratulations, you win!")
            print("You have found the treasure, here is the golden chest.")

        elif choice3 == "red":
            print("You have entered a room filled with fire, Game over!.")

        else:
            print("Wrong decision, Game over!.")
    else:
        print("You have been attaced by trout, Game over!.")
else:
    print("You have fallen into a whole, Game over!.")
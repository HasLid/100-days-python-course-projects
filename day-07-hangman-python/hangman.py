import random
word_list = ["come", "come", "love", "lack", "line", "load", "long", "look", "make", "many", "more", "most", "move", "much", "must", "name", "need", "next", "nice", "nine"]
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
        display.append("_")
lives = 6
end_of_game = False
print("Welcome to Hangman!")
print(f"{' '.join(display)}")

while not end_of_game:
        guess = input("Guess a letter: ").lower()

        for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                        display[position] = letter

        if guess not in chosen_word:
                lives -= 1
                print(f"Wrong! Lives left {lives}")
                if lives == 0:
                        end_of_game = True
                        print("You lose!")
                        print(f"The word was {chosen_word}!")
                
        print(" ".join(display))
        if "_" not in display:
                end_of_game = True
                print("You win!")
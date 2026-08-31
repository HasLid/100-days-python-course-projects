# 🎮 Hangman Game

A classic, text-based Hangman game built to play right in your terminal. Challenge your vocabulary and guess the hidden word before you run out of chances!

---

## 🚀 How to Play

The objective of the game is to guess the secret word letter by letter before the hangman drawing is complete.

1. **Start the Game**: Run the game script in your terminal.
2. **See the Hidden Word**: The secret word is represented by a row of underscores (`_ _ _ _`), showing the number of letters.
3. **Guess a Letter**: Type a single letter on your keyboard and press `Enter`.
   - **Correct Guess**: The letter fills in the blanks where it belongs in the word.
   - **Incorrect Guess**: You lose one life, and a new part of the hangman visual appears.
4. **Win or Lose**:
   - **Win**: Correctly guess all the letters in the word before running out of lives.
   - **Lose**: Run out of lives (usually 6 attempts) before revealing the word.

---

## 🛠️ Installation & Setup

Follow these simple steps to get the game running on your local machine.

### Prerequisites

Make sure you have **Python 3.x** installed on your system.

### Steps

1. **Clone the repository** (or download the source code):
   ```bash
   git clone https://github.com/HasLid/100-days-python-course-projects.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd hangman-game
   ```
3. **Run the game**:
   ```bash
   python hangman.py
   ```

---

## ⚙️ Game Rules & Features

- 🛑 **6 Lives Total**: You can make up to 6 wrong guesses before the game ends.
- 🔠 **Case Insensitive**: The game accepts both upper and lowercase letters.
- ⚠️ **Input Validation**: The game warns you if you enter numbers, symbols, or multiple letters, without costing you a life.
- 🔄 **No Penalty for Duplicates**: Guessing a letter you already tried won't take away a life.

---

## 📦 Project Structure

````text
hangman-game/
│
├── hangman.py        # Main game loop and logic
├── words.py          # List of random secret words
└── README.md         # Game documentation and instructions
```.
````

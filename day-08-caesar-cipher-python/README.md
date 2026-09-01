# Caesar Cipher Tool

A lightweight Python command-line application that encrypts and decrypts text using the classic Caesar Cipher algorithm. It supports shifts of any size and preserves spaces, numbers, and symbols.

## 🚀 Features

- **Bi-directional:** Easily **encode** (encrypt) or **decode** (decrypt) messages.
- **Smart Shifting:** Handles shift numbers larger than 26 automatically.
- **Character Protection:** Keeps non-alphabet characters (spaces, punctuation, numbers) exactly as they are.
- **Replayable:** Loop the program to process multiple messages without restarting the script.

## 🛠️ How It Works

The Caesar Cipher shifts each letter in a message by a fixed number of positions down the alphabet.

- **Encryption (Shift = 3):** `hello` becomes `khoor`
- **Decryption (Shift = 3):** `khoor` becomes `hello`

## 📋 Prerequisites

- **Python 3.x** installed on your system.

## 💻 Usage

1. **Clone or download** this repository.
2. Run the script from your terminal:
   ```bash
   python main.py
   ```
3. Follow the interactive command-line prompts:

   ```text
   Type 'encode' to encrypt, type 'decode' to decrypt:
   encode
   Type your message:
   hello world!
   Type the shift number:
   5
   Here is the encoded text: mjqqt btwqi!

   Type 'yes' if you want to go again, otherwise 'no':
   no
   Goodbye
   ```

## 📂 File Structure

- `main.py` - The complete execution script containing the user loop, ASCII art logo, and cipher logic.

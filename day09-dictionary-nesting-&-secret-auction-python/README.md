# 🤫 Secret Auction Program

A Python command-line application that runs a blind, silent auction. Bidders can secretly input their names and bid amounts, and the program will automatically calculate and declare the winner once all bids are collected.

To ensure fairness, the screen clears after each entry so that bidders cannot see previous bids.

---

## ✨ Features

- **Blind Bids:** Clears the console interface after every entry to keep pricing hidden.
- **Dynamic Bidders:** Supports an unlimited number of participants.
- **Auto-Evaluation:** Instant calculation and announcement of the highest bidder at the end.
- **Data Validation:** Basic type handling for financial bid inputs.

---

## 🛠️ Project Structure

```text
├── art.py          # Contains the ASCII art logo
├── main.py         # The primary auction program logic
└── README.md       # Project documentation
```

---

## 🚀 How to Run

### Prerequisites

- Python 3 installed on your machine.

### Installation & Execution

1. Clone or download this repository.
2. Open your terminal, command prompt, or terminal inside your IDE.
3. Navigate to the folder containing the project files.
4. Run the application using the following command:

```bash
python main.py
```

---

## 📝 Usage Example

1. The program starts and displays the **Secret Auction** ASCII logo.
2. Participant 1 enters their name and bid amount (e.g., `Alice`, `$150`).
3. The program asks: `Are there any other bidders? Type 'yes' or 'no'.`
4. If `yes` is entered, the screen clears completely, and Participant 2 can bid without seeing Alice's offer.
5. Once `no` is entered, the program finishes and prints: `The winner is Alice with a bid of $150!`.

---

## ⚙️ How it Works Behind the Scenes

The program utilizes a Python **dictionary** data structure where:

- **Keys** represent the bidder names.
- **Values** store the respective numeric bids.

A custom looping function iterates through the dictionary values at completion to locate the maximum integer/float value, mapping it back to its corresponding key.

By Dev Hassan Halidu.

logo = '''
                         ___________
                        /           \\
                       /             \\

                      |   _   _       |
                      |  | | | |      |
                      |  |_| |_|      |
                      |   _   _       |
                      |  | | | |      |
   ___________________|__|_|_|_|______|___________________

  |                                                       |
  |                    SECRET AUCTION                     |
  |_______________________________________________________|
  |                                                       |
  |     _______                   _______                 |
  |    /       \\                 /       \\                |
  |   /   ___   \\               /   ___   \\               |
  |  |   /   \\   |             |   /   \\   |              |
  |  |  |  O  |  |  _______  |  |  O  |  |              |
  |  |   \\___/   | /       \\ |   \\___/   |              |
  |   \\         / /   ___   \\ \\         /               |
  |    \\_______/ |   /   \\   | \\_______/                |
  |               |  |  O  |  |                           |
  |               |   \\___/   |                           |
  |                \\         /                            |
  |                 \\_______/                             |
  |_______________________________________________________|
'''

import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

print(logo)
print("Welcome to secret auction program.")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid if {highest_bid}")
    
    
while not bidding_finished:
    name = input("What is your name?: ").upper()
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

    should_continue = input("Are there other bidders? Type 'yes' to continue, 'no' to end the program: ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
# Day 9
# Project

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

def find_highest_bidder(bidding_dic):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bidders = {}
keep_running = True
while keep_running:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        keep_running = False
        find_highest_bidder(bidders)
    else:
        print("\n" * 100)


'''
Notes - Day 9
-> Dictionaries
-> Nesting
'''

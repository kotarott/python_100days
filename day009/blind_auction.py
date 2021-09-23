import os

bidders = {}

def add_member(name, bid_price):
    bidders[name] = bid_price

def get_winner(bidders_dict):
    winner = ""
    winner_price = 0
    for bidder in bidders_dict:
        if bidders_dict[bidder] > winner_price:
            winner = bidder
            winner_price = bidders_dict[bidder]
    return winner

loop_flg = True

while loop_flg:
    name = str(input("What is your name?: "))
    price = int(input("What's your bid?: $"))
    add_member(name, price)
    isend = str(input("Are there any other bidders? Type 'yes' or 'no': ").lower())
    os.system("cls")
    if isend == "no":
        loop_flg = False
        winner = get_winner(bidders)
        print(f"The winner is {winner} with a bid of ${bidders[winner]}.")
    


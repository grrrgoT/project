import auction_logo

print(auction_logo.logo)

bid_amount = {}

auction_over = False

while not auction_over:
    greetings = input("What is your name?")
    price = int(input("What is your bid?: $ "))
    bid_amount[greetings] = price

    people = input("Are there any other bidders? Type 'yes' or 'no' .\n")
    if people == "no":
        auction_over = True

highest_bid = 0
winner = ""
for bidder in bid_amount:
    bid_money = bid_amount[bidder]
    if bid_money > highest_bid:
        highest_bid = bid_money
        winner = bidder


print(f"The winner is {winner} with a bid of ${highest_bid}")
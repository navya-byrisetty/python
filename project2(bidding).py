
def highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if(bid_amount>highest_bid):
            highest_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}")
bids={}
continue_bidding=True
while continue_bidding:
    name=input("enter the user name: ")
    price=int(input("enter the bid:$"))
    bids[name]=price
    should_continue=input("are there any oher bidders type 'yes' or 'no' :")
    if(should_continue=='no'):
        continue_bidding=False
        highest_bidder(bids)
    elif(should_continue=='yes'):
        print("\n"*20)

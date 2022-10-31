from turtle import clear
from logo_proiect10 import logo
print(logo)

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
  print(f"Castigatorul este {winner} cu oferta de ${highest_bid}")

while not bidding_finished:
  name = input("Care este numele dumneavoastra?: ")
  price = int(input("Care este oferta dumneavoastra: $"))
  bids[name] = price
  should_continue = input("Mai sunt alte oferte? Scrie 'da' sau 'nu'.\n")
  if should_continue == "nu":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "da":
    clear()
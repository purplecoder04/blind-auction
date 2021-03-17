from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo


bidders= {}
def bidding(dict_bidders):
    highest_bidder_name=""
    highest_bidder_bid = 0
    for key, value in bidders.items():
        if highest_bidder_bid < value:
          highest_bidder_name = key
          highest_bidder_bid = value
    print(f"hightest bidder {highest_bidder_name} is with bid of ${highest_bidder_bid}")
      
      


print(logo)
print("welcome to the secret auction program.")
done_bidding = False

while not done_bidding:
  bidder_name = input("What is your name?:")
  bid =int(input(f"{bidder_name} whats's your bid?:$"))
  other_bidder= input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  bidders[bidder_name] = bid
 

  if other_bidder == "no":
    done_bidding = True
  else:
    clear()


bidding(bidders)
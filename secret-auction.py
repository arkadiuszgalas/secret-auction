continue_bids = True

bids_table = dict()
print("Welcome to the secret auction program.")
while continue_bids:
   name_player = input("What is your name ?: ")
   bid = input("What's your bid ?: $")
   bid_dec = round(float(bid),2)
   bids_table[name_player] = bid_dec
   other = input("Are there any other bidders ? Type 'yes' or 'no' \n")

   if other == 'yes':
      print("\n" * 30)
   else:
      continue_bids = False

max_bid = 0
winner_name = ''
for key in bids_table:
   if bids_table[key] > max_bid:
      max_bid = bids_table[key]
      winner_name = key

print("\n" * 30)
print(f"The winner is {winner_name} with a bid of ${max_bid}.")

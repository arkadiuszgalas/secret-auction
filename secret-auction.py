continue_bids = True

bids_table = dict()
while continue_bids:
   print("Welcome to the secret auction program.")
   name_player = input("What is your name ?: ")
   bid = input("What's your bid ?: $")
   bids_table[name_player] = bid
   other = input("Are there any other bidders ? Type 'yes' or 'no'.")

   if other == 'yes':
      print("\n" * 5)
   else:
      continue_bids = False

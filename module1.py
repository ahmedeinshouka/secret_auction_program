
import os
from pickle import TRUE
print("                                            welcome to the secret auction program".title())
line="_______________________________________________________________________________________________________________________"

tittle='''
  _     _ _           _                        _   _                                             _      _           _ 
 | |__ | (_)_ __   __| |       __ _ _   _  ___| |_(_) ___  _ __         ___ ___  _ __ ___  _ __ | | ___| |_ ___  __| |
 | '_ \| | | '_ \ / _` |_____ / _` | | | |/ __| __| |/ _ \| '_ \ _____ / __/ _ \| '_ ` _ \| '_ \| |/ _ | __/ _ \/ _` |
 | |_) | | | | | | (_| |_____| (_| | |_| | (__| |_| | (_) | | | |_____| (_| (_) | | | | | | |_) | |  __| ||  __| (_| |
 |_.__/|_|_|_| |_|\__,_|      \__,_|\__,_|\___|\__|_|\___/|_| |_|      \___\___/|_| |_| |_| .__/|_|\___|\__\___|\__,_|
                                                                                          |_|                         
'''


logo = ('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
bids={}
bidding=False
def find_highest_price(bids):
    highestbid=0
    winner=''
    for bidder in bids:
        bid_amount =bids[bidder]
        if highestbid<bigamount:
            bigamount=bidder
    print(f"{tittle}\n{line}\n{line}\n{logo}\n{line}") 
    print(f"The winner is {winner} with a bid of ${highestbid}")
while not bidding:
    print(f"{tittle}\n{line}\n{line}\n{logo}\n{line}") 
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    os.system('cls')
    if should_continue=='yes':
        pass
    elif should_continue=='no':
        bidding==True

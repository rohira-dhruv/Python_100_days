#Silent Auction Program - Day 9
import art
import os

print(art.logo)

print("Welcome to the silent auction program!")
auction = {}
cont = "yes"
while cont == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    cont = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system("cls")

highest_bid = 0
winner = ""
for name in auction:
    if auction[name] > highest_bid:
        highest_bid = auction[name]
        winner = name

print(f"The winner is {winner}, with a bid of ${highest_bid}.")
    
    
    
    

from art import logo, vs
from game_data import data
from os import system
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


print(logo)

option_a = random.choice(data)
data.remove(option_a)

shouldContinue = True
current_score = 0

while shouldContinue:
    
    option_b = random.choice(data)
    data.remove(option_b)

    print(f"Compare A: {format_data(option_a)}")
    print(vs)
    print(f"Against B: {format_data(option_b)}")

    winner = option_a if option_a["follower_count"] > option_b["follower_count"] else option_b

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    system("cls")
    if (guess == "a" and winner == option_a) or (guess == "b" and winner == option_b):
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        option_a = option_b
        
    elif (guess == "a" and winner == option_b) or (guess == "b" and winner == option_a):
        print(f"Sorry, that's wrong. Final score: {current_score}")
        shouldContinue = False
        
    else:
        print("Invalid input")
        shouldContinue = False

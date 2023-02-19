from art import logo
import random
import os

user_cards = []
computer_cards =[]

def deal_card():
    """This function returns a randomly drawn card from a deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(card_list):
    """This function returns the score of the hand dealt"""
    if sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def check_winner(user_score, computer_score):
    """This function compares the score between two set of cards and prints the result"""
    if computer_score == 21 and len(computer_cards) == 2:
        print("BLACKjACK! You lose! 😭")
    elif user_score == 21 and len(user_cards) == 2:
        print("BLACKJACK! You Win! 🎉")
    elif user_score <= 21:
        if computer_score > 21:
            print("The Computer went over. You Win 😁")
        elif computer_score < user_score:
            print("You Win 😃")
        elif computer_score == user_score:
            print("It is a Draw!")
        else:
            print("You Lose 😭")
    else:
        print("You went over. You Lose 😤")

def game():
    
    print(logo)
    
    decision = 'y'
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_score = user_cards[0]
    while decision == 'y' and user_score <= 21:
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"\tYour cards: {user_cards}, current score is: {user_score}")
        print(f"\tDealer's first card is: {computer_cards[0]}")
        
        if user_score <= 21:
            decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            
    computer_score = computer_cards[0]
    while computer_score <= 16:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"\tYour final hand is {user_cards} and the final score is: {user_score}")
    print(f"\tComputer's final hand is {computer_cards} and the final score is {computer_score}")
    
    check_winner(user_score, computer_score)
        

while(input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower() == 'y'):
    os.system('cls')
    game()
    user_cards = []
    computer_cards =[]
print("Thanks for playing!")
    
    
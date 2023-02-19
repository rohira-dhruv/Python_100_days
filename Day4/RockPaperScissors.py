import art
import random
print("Welcome to Rock Paper Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if (user_choice < 0) or (user_choice > 2):
    print("You typed an invalid number, you lose!")

else:
    computer_choice = random.randint(0, 2)

    choices = [art.rock, art.paper, art.scissors]

    print(choices[user_choice])
    print("Computer chose:")
    print(choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    else:
        print("You win!")

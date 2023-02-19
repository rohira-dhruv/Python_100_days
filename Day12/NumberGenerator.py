import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = EASY_LEVEL_TURNS
else:
    attempts = HARD_LEVEL_TURNS

target = random.randint(1, 100)

while(attempts != 0):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > target:
        print("Too high.")
    elif guess < target:
        print("Too low.")
    else:
        print(f"You got it! The answer was {target}.")
        break
    attempts -= 1

if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"The number was {target}.")
    
    

import random
import art
import words

chosen_word = words.word_list[random.randint(0, len(words.word_list) - 1)]

length = len(chosen_word)

print()
display_list = []
for _ in chosen_word:
    display_list.append("_")

num_lives = 6

while "_" in display_list and num_lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        num_lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"You have {num_lives} lives left.")
    else:
        print(f"You guessed {guess}, that's in the word.")

    for num in range(0, length):
        if guess == chosen_word[num]:
            display_list[num] = guess
    print(art.stages[num_lives])
    print(display_list)
    print()


if num_lives == 0:
    print("You lose!")
else:
    print("You win!")


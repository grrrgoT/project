import random
import os
from hangman_arts import logo, stages
from hangman_words import word_list

lives = 6
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

chosen_word = random.choice(word_list)
lives = 6
gameover = False
correct_letters = []
guessed_letters = []

print(logo)

placeholder = ""
for position in range(0, len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)


while not gameover:
    print("****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            gameover = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        gameover = True
        print("****************************YOU WIN****************************")

    print(stages[lives])


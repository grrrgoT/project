import random
import day12number_logo

def game():
    print(day12number_logo.logo)
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100. ")

    number = random.randint(1, 100)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        life = 10
        
    else:
        life = 5

    is_game_over = False
    while not is_game_over:
        print(f"You have {life} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high")
            life -= 1
        elif guess < number:
            print("Too low")
            life -= 1
        elif guess == number:
            print(f"You win! You got it! The answer was {number}")
            is_game_over = True


        if life == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {number}.")
            is_game_over = True

        elif not is_game_over:
            print("Guess again. ")

game()

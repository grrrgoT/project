import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_over = False

user_cards = []
for _ in range(2):
    user_cards.append(random.choice(cards))
print(f"Your cards: {user_cards}")

computer_cards = []
computer_cards.append(random.choice(cards))
first_cop_cards = print(f"Computer's first card: {computer_cards}")


while not game_over:
    pick = input("Type 'y' to get another card, type 'n' to pass: ")
    if pick == "y":
        user_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards}")
        if sum(user_cards) > 21:
            print("You went over. You lose!")
            game_over = True
            break
    else:
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
        game_over = True


print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")

if sum(user_cards) > 21:
    print("You lose....")       
elif sum(computer_cards) > 21:
    print("Opponent went over. You win!")  
elif sum(user_cards) > sum(computer_cards):
    print("You win!")
elif sum(user_cards) < sum(computer_cards):
    print("You lose....")
else:
    print("Draw!")




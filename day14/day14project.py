import high_or_low_logo
import game_data
import random

print(high_or_low_logo.logo)
game_over = False
score = 0

compare2 = random.choice(game_data.data)

while not game_over:
    compare1 = compare2
    compare2 = random.choice(game_data.data)

    while compare1 == compare2:
        compare2 = random.choice(game_data.data)

    print(f"Compare A: {compare1['name']}, a {compare1['description']}, from {compare1['country']}.")
    print(high_or_low_logo.vs)
    print(f"Compare B: {compare2['name']}, a {compare2['description']}, from {compare2['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_followers = compare1['follower_count']
    b_followers = compare2['follower_count']

    if (guess == "A" and a_followers > b_followers) or (guess == "B" and b_followers > a_followers):
        score += 1
        print(f"correct! You score is: {score}")
    else:
        print(f"sorry. Your final score is: {score}")
        game_over = True


    


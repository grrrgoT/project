import high_or_low_logo
import game_data
import random

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"
def play_game():
    print(high_or_low_logo.logo)
    game_over = True
    score = 0

    compare2 = random.choice(game_data.data)

while not game_over:
    compare1 = compare2
    compare2 = random.choice(game_data.data)

    while compare1 == compare2:
        compare2 = random.choice(game_data.data)

    print(f"Compare A: {format_data(account_a)}")
    print(high_or_low_logo.vs)
    print(f"Compare B:{format_data(account_b)} ")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_followers = compare1['follower_count']
    b_followers = compare2['follower_count']

    if (guess == "A" and a_followers > b_followers) or (guess == "B" and b_followers > a_followers):
        score += 1
        print(f"correct! You score is: {score}")
    else:
        print(f"sorry. Your final score is: {score}")
        game_over = True


    


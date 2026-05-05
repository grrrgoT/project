print(f"Welcome to Tresure Island\n" "Your mission is to find the tresure.\n")
place = input("You're at a cross road. Where do you want to go?\n Type left or right ").lower()
if place == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake.\n Type wait to wait for a boat. Type swim to swim across. ").lower()
    if lake == "wait":
        colour = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose? ").lower()
        if colour == "red":
            print("Burned by fire.\nGame over.")
        elif colour == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif colour == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole. Game Over.")


        

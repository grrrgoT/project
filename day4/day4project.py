import random
greetings = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

list = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""", """
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)      
"""
]


#if greetings == 0:
    #print(list[0])
#elif greetings == 1:
    #print(list[1])
#elif greetings == 2:
    #print(list[2])

print(list[greetings])
computer = random.randint(0,2)
print("Computer chose: ")
print(list[computer])


#if (greetings == list[0] and computer == list[2]) and (greetings == list[1] and computer == list[0]) and (greetings == list[2] and computer == list[1]):
    #print("You Win!")
if greetings == computer:
    print("It's draw")

#elif (greetings == list[0] and computer == list[0]) and (greetings == list[1] and computer == list[1]) and (greetings == list[2] and computer == list[2]):
    #print("It's draw")
elif (greetings == 0 and computer == 2) or \
    (greetings == 1 and computer == 0) or \
    (greetings == 2 and computer == 1):
    print("You win!")

#elif (greetings == list[0] and computer == list[1]) and (greetings == list[1] and computer == list[2]) and (greetings == list[2] and computer == list[0]):
    #print("You lose")
else:
    print("You lose")


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill = 17
    else:
        bill = 15

elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill = 23
    else:
        bill = 20

elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill = 28
    else:
        bill = 25

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your final bill is: ${bill}.")
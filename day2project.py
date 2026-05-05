print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip

pay = (float(total_bill)) / int(people)

print(f"Each person should pay: ${pay:.2f}")
print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill ? \n $"))
percentage_tip = int(input("What percentage tip would you like to give ? 10, 12, or 15\n"))
people = int(input("How many people to split the bill ?\n"))

formula = (total_bill + (total_bill * (percentage_tip/100))) / people

print(f"Each person should pay: ${formula}")
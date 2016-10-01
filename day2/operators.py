mealCost = float(input())
tipPercent = float(input())
taxPercent = float(input())

tip = mealCost*(tipPercent/100)
tax = mealCost*(taxPercent/100)
total = mealCost + tip + tax

print("The total meal cost is {0} dollars.".format(round(total)))

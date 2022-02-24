budget = float(input())
category = str(input())
people = int(input())
travel_costs = 0
ticket_price = 0

if 1 <= people <= 4:
    travel_costs = budget * 0.75

if 5 <= people <= 9:
    travel_costs = budget * 0.60

if 10 <= people <= 24:
    travel_costs = budget * 0.50

if 25 <= people <= 49:
    travel_costs = budget * 0.40

if 50 <= people:
    travel_costs = budget * 0.25

if category == "VIP":
    ticket_price = 499.99

if category == "Normal":
    ticket_price = 249.99

total_expense = travel_costs + people * ticket_price
if total_expense <= budget:
    print(f"Yes! You have {budget - total_expense :.2f} leva left.")

if total_expense > budget:
    print(f"Not enough money! You need {total_expense - budget :.2f} leva.")
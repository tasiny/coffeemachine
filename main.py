import data
from data import MENU

water = 300
milk = 200
coffee = 100
profit = 0
machine_on = True


def print_report(w, m, c, p):
    print(f"Water: {w}ml")
    print(f"Milk: {m}ml")
    print(f"Coffee: {c}g")
    print(f"Money: ${p}")


def calculate_change(q, d, n, p, c):
    total = (q * 25/100) + (d * 10/100) + (n * 5/100) + (p * 1/100)
    change = total - c
    format_change = format(change, '.2f')
    print(f"Here is ${format_change} in change")
    print("Here is your latte, enjoy!")


def insufficient_funds(q, d, n, p, c):
    total = (q * 25 / 100) + (d * 10 / 100) + (n * 5 / 100) + (p * 1 / 100)
    if total < c:
        print("Sorry, that is not enough money. Money refunded. ")


while machine_on == True:
    coffee_choice = input("What would you like?(espresso/ latte/ cappuccino): ").lower()
    if coffee_choice == "report":
        print_report(water, milk, coffee, profit)
    elif coffee_choice == "espresso":
        print("Please insert coins. ")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickels = float(input("How many nickels?: "))
        pennies = float(input("How many pennies?: "))
        if (quarters * 25 / 100) + (dimes * 10 / 100) + (nickels * 5 / 100) + (pennies * 1 / 100) < 1.5:
            insufficient_funds(quarters, dimes, nickels, pennies, 1.5)
        elif water < 50:
            print("Sorry, there is not enough water")
        elif coffee < 18:
            print("Sorry, there is not enough coffee")
        else:
            calculate_change(quarters, dimes, nickels, pennies, 1.5)
            coffee -= 18
            water -= 50
            profit += 1.5
    elif coffee_choice == "latte":
        print("Please insert coins. ")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickels = float(input("How many nickels?: "))
        pennies = float(input("How many pennies?: "))
        if (quarters * 25 / 100) + (dimes * 10 / 100) + (nickels * 5 / 100) + (pennies * 1 / 100) < 2.5:
            insufficient_funds(quarters, dimes, nickels, pennies, 2.5)
        elif water < 200:
            print("Sorry, there is not enough water")
        elif milk < 150:
            print("Sorry, there is not enough milk")
        elif coffee < 24:
            print("Sorry, there is not enough coffee")
        else:
            calculate_change(quarters, dimes, nickels, pennies, 2.5)
            coffee -= 24
            water -= 200
            milk -= 150
            profit += 2.5
    elif coffee_choice == "cappuccino":
        print("Please insert coins. ")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickels = float(input("How many nickels?: "))
        pennies = float(input("How many pennies?: "))
        if (quarters * 25 / 100) + (dimes * 10 / 100) + (nickels * 5 / 100) + (pennies * 1 / 100) < 3.0:
            insufficient_funds(quarters, dimes, nickels, pennies, 3.0)
        elif water < 250:
            print("Sorry, there is not enough water")
        elif milk < 100:
            print("Sorry, there is not enough milk")
        elif coffee < 24:
            print("Sorry, there is not enough coffee")
        else:
            calculate_change(quarters, dimes, nickels, pennies, 3.0)
            coffee -= 24
            water -= 250
            milk -= 100
            profit += 3.0
    else:
        machine_on = False
        print("Thank you for using the coffee machine!")






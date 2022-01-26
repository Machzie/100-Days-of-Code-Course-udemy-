#Day 16 Project - Coffee Machine using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user_choice = input(f"Please pick a drink: {Menu().get_items()} ")
user_drink = Menu().find_drink(user_choice)

# Print report
if user_choice.lower() == 'report':
    print(CoffeeMaker().report())
    print(MoneyMachine().report())
else:
    print(f"You chose: {user_choice}")
    print(f"Please pay {MoneyMachine().CURRENCY}{user_drink.cost:.2f}")

# Check resources sufficient?
if CoffeeMaker().is_resource_sufficient(user_drink):

    # Process coins
    # Check transaction successful?
    if MoneyMachine().make_payment(user_drink.cost):

        # Make coffee
        print("Making coffee...")
        CoffeeMaker().make_coffee(user_drink)

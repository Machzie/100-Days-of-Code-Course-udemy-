import coffee_data

menu = coffee_data.MENU
resources = coffee_data.resources


def sum_total(c1, c2, c3, c4, c5):
    """Takes an input of number of coins and returns the summed value"""
    return (c1 * 2.0) + (c2 * 1.0) + (c3 * 0.5) + (c4 * 0.2) + (c5 * 0.1)


def check_resources(ingredients):
    """Checks resources and returns False if there aren't enough left"""
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Insufficient {i} remaining")
            return False
    return True


coffee_machine_on = True

while coffee_machine_on:

    print("What would you like?")
    print("1: Espresso")
    print("2: Latte")
    print("3: Cappuccino")
    user_choice = input("")

    # print(resources)

    # Print report of resources if the user types 'report'
    # Assign the user choice to the dictionary key
    if user_choice.lower() == 'off':
        print("Shutting down...")
        coffee_machine_on = False
        break
    elif user_choice.lower() == 'report':
        for resource in resources:
            print(f"Remaining {resource}: {resources[resource]}")
        continue
    elif user_choice == '1':
        coffee = 'espresso'
    elif user_choice == '2':
        coffee = 'latte'
    elif user_choice == '3':
        coffee = 'cappuccino'
    else:
        print("Invalid input")
        coffee_machine_on = False
        break

    # Check resources are sufficient when a user orders a drink
    if check_resources(menu[coffee]["ingredients"]):

        # Process different types of coin (£2, £1, 50p, 20p, 10p)
        cost = menu[coffee]["cost"]
        print(f"Please pay £{cost:.2f}. Insert coins:")
        two_pounds = int(input("Number of £2 coins: "))
        one_pounds = int(input("Number of £1 coins: "))
        fifty_pences = int(input("Number of 50p coins: "))
        twenty_pences = int(input("Number of 20p coins: "))
        ten_pences = int(input("Number of 10p coins: "))

        money_paid = sum_total(two_pounds, one_pounds, fifty_pences, twenty_pences, ten_pences)
        print(f"Total paid: £{money_paid:.2f}")

        # Check if there is enough money
        # Deplete resources while making coffee
        if money_paid >= menu[coffee]["cost"]:
            print("Making coffee...")
            print(f"Here is your {coffee} ☕. Enjoy!")
            for resource in resources:
                if resource in menu[coffee]["ingredients"]:
                    resources[resource] -= menu[coffee]["ingredients"][resource]
            print(f'Your change: £{money_paid - menu[coffee]["cost"]:.2f}')
        else:
            print("Not enough money.")
            continue

    else:
        coffee_machine_on = False

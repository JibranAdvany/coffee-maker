MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Report generation


def ingredients_report():
    for menu_item in MENU:
        print(f"Resources needed for {menu_item.title()}:")
        for ingredient in MENU[menu_item]["ingredients"]:
            print(f"{ingredient}:", MENU[menu_item]["ingredients"][ingredient])


def resources_report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}ml")


# Money Collection


def money_collection():
    pennies = int(input("Please put penny: "))
    nickels = int(input("Please put nickel: "))
    dimes = int(input("Please put dime: "))
    quarters = int(input("Please put quarter: "))
    return round(pennies / 100 + nickels / 20 + dimes / 10 + quarters / 4, 2)


# Resource Checker


def resource_checker(coffee, amount):
    resources_needed = MENU[coffee]["ingredients"]

    for resource_needed in resources_needed:
        if resources[resource_needed] < resources_needed[resource_needed]:
            print(f"Not enough {resource_needed}. Your money ${amount} is now refunded.")
            return False
        else:
            # Code for updating resources
            resources[resource_needed] = resources[resource_needed] - resources_needed[resource_needed]

    return True


print("The Coffee Maker")

machine_on = True

while machine_on:
    user_action = input("What would you like to do with the machine? (ingredients report / resources report / make "
                        "coffee) ")

    if user_action == "ingredients report":
        ingredients_report()
    elif user_action == "resources report":
        resources_report()
    elif user_action == "make coffee":
        amount_received = money_collection()
        print(f"You have given ${amount_received}.")
        if amount_received < 1.5:
            print(f"You can not purchase anything. Your amount ${amount_received} deposited is not refunded.")
        else:
            coffee_type = input("Which coffee do you want? (espresso / latte / cappuccino) ")
            can_proceed = resource_checker(coffee_type, amount_received)
            if can_proceed:
                if amount_received >= MENU[coffee_type]["cost"]:
                    print(f"Here is your {coffee_type}.")
                else:
                    print(f"Sorry the cost of {coffee_type} is ${MENU[coffee_type]['cost']} and you have provided "
                          "${amount_received}. So, you can not purchase the coffee. Here is your refund of "
                          "${amount_received}.")

    turn_off = input("Would you like to turn off the machine? (y / n) ")
    if turn_off == "y":
        machine_on = False

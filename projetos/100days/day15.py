# Day 15
# Coffee Machine - Project Day 15

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
    "money": 0,
}

def get_coins(drink):
    print(f"Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    price = MENU[drink]["cost"]
    if total > price:
        change = round(total - price, 2)
        print(f"Here is $ {change} in change.")
        return price
    elif total == price:
        return price
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return 0

def make_coffee(drink):
    """Deduct the ingredients from the resources."""
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink} ☕️. Enjoy!")

def get_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"

def check_resources(drink):
    """Returns True when an order can be made and False otherwise."""
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]['ingredients'][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

machine_online = True
while machine_online:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        machine_online = False

    elif choice == "report":
        print(get_report())

    if choice in MENU:
        if check_resources(choice):
            coins = get_coins(choice)
            if coins > 0:
                resources["money"] += coins
                make_coffee(choice)

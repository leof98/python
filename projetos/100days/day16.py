# Day 16
# Coffee Machine (OOP Version) - Day 16

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_online = True
while machine_online:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    # Exit the program
    if choice == "off":
        machine_online = False
    # Shows the report for the user
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

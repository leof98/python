"""
Prompts for items, until ctrl-d. After each item, display the total cost of all thus far prefixed with a ($) and formatted to two decimal places.
06.05, 11.22
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:
        item = input('Item: ')
        item = item.title()
        menu[item]
        
        if item in menu:
            total += menu[item]
            print('Total: $%.2f' % (total))
            pass

    except EOFError:
        break
    except KeyError:
        pass

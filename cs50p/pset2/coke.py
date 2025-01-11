"""
A program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
04.22, 11.22, 00.00
"""

amount = 0
change = 50
values = [5, 10, 25, 50]

while amount < 50:
    coin = int(input('Insert Coin: '))
    if coin in values:
        amount += coin
        change -= coin
        if change < 0:
            print('Change owed: ' + str(abs(change)))
        else:
            print(f'Amount due: {change}')
    else:
            print(f'Amount due: {change}')

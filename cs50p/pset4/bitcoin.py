'''
Expects the user to specify as a command-line argument the number of Bitcoins n
Outputs the current cost of n Bitcoins in USD
11.22
'''
import sys
import requests

try:
    n = float(sys.argv[1])
except IndexError:
        sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')

try:
    coin = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    coin = coin.json()
    coin = coin['bpi']
    coin = coin['USD']
    amount = coin['rate_float'] * n
except:
    sys.exit()
print(f'${amount:,.4f}')

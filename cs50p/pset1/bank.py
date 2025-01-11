"""
Implement a program that prompts the user for a greeting
If the greeting starts with “hello”, output $0
If the greeting starts with an “h”, output $20
Otherwise, output $100
"""

greeting = str(input('Greeting: '))

if greeting.lower().strip().startswith('hello'):
    print('$0')
elif greeting.lower().startswith('h'):
    print('$20')
else:
    print('$100')

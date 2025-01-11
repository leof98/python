"""
Prompts for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
x is an integer; y is +, -, *, or /; z is an integer
"""
exp = input('Expression: ')
x, y, z = exp.split(' ')
x = float(x)
z = float(z)

if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
elif y == '/':
    print(x / z)
else:
    print(x)

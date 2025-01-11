"""
A program that prompts for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the input will indeed be in camel case.
04.22, 11.22, 00.00
"""

name = str(input('camelCase: '))
snake = ''

for letter in name:
    if letter.islower() == False:
        letter = letter.lower()
        letter = letter.replace(letter, '_' + letter)
        snake += letter
    elif letter.islower() == True:
        snake += letter
    else:
        pass

print(snake)

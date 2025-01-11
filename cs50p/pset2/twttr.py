"""
Implement a program that prompts the user for a str of text and then outputs that same text but
with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
04.22, 11.22, 00.00
"""

text = str(input('Input: '))
txt = ''
vogals = ['a','A','e','E','i','I','o','O', 'u', 'U']

for l in text:
    if l in vogals:
        pass
    else:
        txt += l
print(txt)

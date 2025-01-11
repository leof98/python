"""
Prompts for items, until ctrl-d. Then output the grocery list in all uppercase,
sorted alphabetically by item, prefixing each line with the number of times.
05.11, 11.22
"""

list = {}

while True:
    try:
        item = input()
        if item not in list:
            list[item] = 0
        if item in list:
            list[item] += 1

    except KeyError:
        pass
    except EOFError:
        break

for i in sorted(list):
    print(list[i], i.upper())

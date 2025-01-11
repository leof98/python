import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = str(input('Name: '))
        names = p.join(name)
    except EOFError:
        break

print('Adieu, adieu to ' + names)

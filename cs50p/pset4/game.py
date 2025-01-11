'''
Guessing Game
11.22
'''
import random

while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            break
    except:
        pass

while True:
    n = random.randint(1, level)
    try:
        guess = int(input('Guess: '))
        if guess < n:
            print('Too small!')
        if guess > n:
            print('Too large!')
        if guess == n:
            print('Just right!')
            break
    except:
        pass

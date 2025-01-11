'''
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with igits.
Prompts the user to solve each of those problem. If an answer is not correct the program should output EEE and prompt the user again, allowing the user up to three tries in total.
After three tries, the program should output the correct answer. The program should ultimately output the score, a number out of 10.
'''
import random

def main():
    level = get_level()
    score = gen_problems(level)
    print(f'Score: {score}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in range(1,4):
                return level
        except:
                pass

def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    else:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
    return a, b

def round(a, b):
    tries = 0
    while tries < 3:
        try:
            answer = int(input(f'{a} + {b} = '))
            if answer == (a + b):
                return True
            else:
                print('EEE')
                tries += 1
                pass
        except:
            print('EEE')
            tries +=1
            pass
    print(f'{a} + {b} = {a + b}')
    return False

def gen_problems(level):
    rounds = 0
    score = 0
    while rounds < 10:
        a, b = generate_integer(level)
        answer = round(a, b)
        if answer == True:
            score += 1
            rounds += 1
        else:
            rounds += 1
    return score

if __name__ == '__main__':
    main()

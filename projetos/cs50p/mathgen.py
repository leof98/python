  '''
A program that generates random math problems.
Last modified: 30/01
'''
import random

#
def main():
    rounds = 0
    user_chances = 4
    level = get_level()
    while user_chances >= 1:
        math_problem = MathProblem(level)
        user_answer = math_problem.get_user_answer()
        correct = math_problem.check_answer(user_answer)
        # TODO: melhorar a interface com o usuário, como os problemas e as chances são exibidos
        if not correct:
            print(f'{math_problem.problem} = {math_problem.answer} <-')
            user_chances -= 1
            lifes = '*' * user_chances
            if user_chances == 0:
                print('Game Over')
                break
            print(f'Life: {lifes}')
        else:
            rounds += 1
            print(f'Score: ({rounds * 100})')

            
# Loop until user enters a valid level
def get_level():
    print('--------------------------------------')
    print('           Random Math')
    print('--------------------------------------')
    while True:
        level = input('Enter level (1, 2, or 3): ')
        if level in ['1', '2', '3']:
            break
    return level

# Class to generate math problems, takes a level (1, 2 or 3) as input
class MathProblem:
    def __init__(self, level):
        self.level = level
        self.problem = self.generate_problem()
        self.answer = eval(self.problem)
        
    # Generate math problem based on level
    # TODO: Repensar a dificuldade dos problemas de cada nível
    # TODO: Adicionar rounds
    def generate_problem(self):
        # round += 1
        if self.level == '1':
            operation = random.choice(['+', '-'])
            a, b = random.randint(1, 10), random.randint(1, 10)
        elif self.level == '2':
            operation = random.choice(['+', '-', '*', '/'])
            a, b = random.randint(1, 10), random.randint(1, 10)
        else:
            operation = random.choice(['+', '-', '*', '/'])
            a, b = random.randint(1, 20), random.randint(1, 20)
        return f'{a} {operation} {b}'

    # Get user answer
    def get_user_answer(self):
        print('--------------------------------------')
        return input(f'{self.problem} = ')

    # Take an answer and check if it is correct
    def check_answer(self, user_answer):
        try:
            return int(user_answer) == self.answer
        except:
            return False
    

if __name__ == '__main__':
    main()

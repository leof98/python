'''
A program that generates random math problems.
Last modified: 01/02
'''
import random

def main():
    game = Game()
    game.play()


# Class to generate math problems, takes a level (1, 2 or 3) as input
class Game:
    def __init__(self):
        self.rounds = 0
        self.user_chances = 4
        self.level = self.get_level()
        
    def play(self):
        while self.user_chances > 0:
            self.play_round()
            self.display_chances()
    
    def play_round(self):
        math = Problem(self.level)
        user_answer = math.get_user_answer()
        correct = math.check_answer(user_answer)
        
        if not correct:
            math.display_incorrect()
            self.user_chances -= 1
    
    def display_chances(self):
        if self.user_chances == 0:
            print('Game over')
        else:
            lifes = '*' * self.user_chances
            print(f'Chances: {lifes}')
        
# Loop until user enters a valid level
    def get_level(self):
        print('--------------------------------------')
        print('           Random Math')
        print('--------------------------------------')
        while True:
            level = input('Enter level (1, 2, or 3): ')
            if level in ['1', '2', '3']:
                break
        return level
    
    
    def display_score(self, rounds):
        print(f'Score: {rounds * 100}')
        
class Problem:
    def __init__(self, level):
        self.level = level
        self.problem = self.generate_problem()
        self.answer = eval(self.problem)
    
    def generate_problem(self):
        # round += 1
        # Usando list comprehension para separar os operadores de acordo com o nível
        operations = {'1': ['+', '-'], '2': ['+', '-', '*', '/'], '3': ['+', '-', '*', '/', '**']}
        operation = random.choice(operations[self.level])
        # List comprehension novamente
        numbers = {'1': list(range(0,11)), '2': list(range(0,21)), '3': list(range(0,31))}
        a, b = random.choice(numbers[self.level]), random.choice(numbers[self.level])
        if operation == '**':
            a, b = random.randint(1, 5), random.randint(1, 3)
        elif operation == '*' or operation == '/':
            a, b = random.randint(1, 20), random.randint(1, 5)
        return f'{a} {operation} {b}'
        
    # Get user's answer
    def get_user_answer(self):
        print('--------------------------------------')
        return input(f'{self.problem} = ')
    
    # check if the answer is correct
    def check_answer(self, user_answer):
        try:
            return float(user_answer) == float(self.answer)
        except:
            return False
    
    def display_incorrect(self):
        print(f'{self.problem} = {self.answer} <-')
    

if __name__ == '__main__':
    main()

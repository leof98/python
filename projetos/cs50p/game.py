'''
A program that generates random math problems.
Last modified: 02/02
'''
import random
import operator

def main():
    game = Game()
    game.play()

# Constants
MAX_ROUNDS = 10
MAX_LEVEL = '3'

OPERATIONS = {
    '1': ['+', '-'], 
    '2': ['+', '-', '*', '/'], 
    '3': ['+', '-', '*', '/', '**']

}

NUMBERS = {
    '1': list(range(0,11)),
    '2': list(range(0,21)),
    '3': list(range(0,31))
}

class Game:
    def __init__(self):
        self.score = 0
        self.rounds = 0
        self.user_chances = 3
        self.level = self.get_level()
        
    def play(self):
        while self.user_chances > 0:
            self.play_round()
    
    def play_round(self):
        self.rounds += 1
        if self.rounds > MAX_ROUNDS and self.level != MAX_LEVEL:
            self.level_up()
        self.display_level()
        math = Problem(self.level)
        user_answer = math.get_user_answer()
        correct = math.check_answer(user_answer)
        
        if not correct:
            math.display_incorrect()
            self.user_chances -= 1
            self.display_chances()
        else:
            self.update_score()
            self.display_score()
        
    def level_up(self):
        levelup = input('Level up? (y/n): ')
        if levelup == 'y':
            self.level = str(int(self.level) + 1)
        self.rounds = 0    
        
    def display_level(self):
        if self.rounds == 0:
            print('--------------------------------------')
            print(f'Level {self.level}')
    
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
    
    def update_score(self):
        self.score += 100
        return self.score
    
    def display_score(self):
        print(f'Score: {self.score}')
        if self.score in [500, 1000, 1500, 2000]:
            print('+1 chance!')
            self.user_chances += 1
        
class Problem:
    def __init__(self, level):
        self.level = level
        self.problem, self.answer = self.generate_problem()
    
    def generate_problem(self):
        operation = random.choice(OPERATIONS[self.level])
        operation_func = {
            '+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul, 
            '/': operator.truediv, 
            '**': operator.pow
        }[operation]

        a, b = random.choice(NUMBERS[self.level]), random.choice(NUMBERS[self.level])
        
        if operation == '**':
            a, b = random.randint(1, 5), random.randint(1, 3)
        elif operation == '/' and b == 0:
            b = 1
            
        answer = operation_func(a, b)
        return f'{a} {operation} {b}', answer
    
        
    # Get user's answer
    def get_user_answer(self):
        print('--------------------------------------')
        return input(f'{self.problem} = ')
    
    # check if the answer is right
    def check_answer(self, user_answer):
        try:
            return float(user_answer) == float(self.answer)
        except:
            return False
        
    # display the correct answer
    def display_incorrect(self):
        if type(self.answer) == int:
            print(f'{self.problem} = {self.answer} <-')
        else:
            print(f'{self.problem} = {self.answer:.1f} <-')
    

if __name__ == '__main__':
    main()

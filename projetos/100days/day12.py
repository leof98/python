# Day 12
# Guessing Game - Day 12 Project
import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_guess(user_guess, answer, chances):
    """Checks the user's guess, returns the turns remaining."""
    if user_guess > answer:
        print("Too high.")
        return chances - 1
    elif user_guess < answer:
        print("Too low.")
        return chances - 1
    else:
        print(f"You got it! The answer was {answer}")

def game():
    print(logo)
    print(f"Welcome!")
    print(f"I'm thinking of a number between 1 and 100.")
    actual_number = random.randint(1, 100)
    print(f"-> {actual_number}")

    chances = set_level()
    guess = 0
    while guess != actual_number:
        print(f"You have {chances} attempts remaining.")
        guess = int(input("Make a guess: "))
        chances = check_guess(guess, actual_number, chances)
        if chances == 0:
            print("You've run out of guesses. You lose.")
            return
game()

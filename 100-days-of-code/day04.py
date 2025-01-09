# Day 4
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice < 3:
    print(options[user_choice])
computer_choice = random.randint(0, 2)
print(options[computer_choice])

#Invalid
if user_choice >= 3:
    print("Invalid number.")

# Rock
if user_choice == 0:
    if computer_choice == 0:
        print("Tie")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")

# Paper
if user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    if computer_choice == 1:
        print("Tie")
    else:
        print("You lose!")

# Scissors
if user_choice == 2:
    if computer_choice == 0:
        print("You lose!")
    if computer_choice == 1:
        print("You win!")
    else:
        print("It's a draw")

'''
Notes - Day 4
- Modules
- Random
- Lists
- IndexError
'''

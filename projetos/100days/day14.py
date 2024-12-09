# Day 14
# Higher or Lower - Day 14 Project

import random
import art
from game_data import data

def get_person_info(person):
    return f"{person["name"]}, a {person["description"]}, from {person["country"]}."

def get_new_person():
    new_person = random.choice(data)
    data.remove(new_person)
    return new_person

def check_answer(user_guess, a_followers, b_followers):
    """Check the user's answer against the actual answer."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
# Start of the game
print(art.logo)
second_person = get_new_person()
score = 0
is_game_running = True

while is_game_running:
    first_person = second_person
    second_person = get_new_person()
    print(f"Compare A: {get_person_info(first_person)}")
    print(art.vs)
    print(f"Against B: {get_person_info(second_person)}")
    a_answer = first_person["follower_count"]
    b_answer = second_person["follower_count"]

    # Get input from the user
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(art.logo)

    # Check the answer
    is_correct = check_answer(guess, a_answer, b_answer)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_running = False

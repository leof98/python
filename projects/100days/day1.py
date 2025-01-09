# Day 1
'''
Task 1
We have 2 variables glass1 and glass2. 
glass1 contains milk and glass2 contains juice. 
Write 3 lines of code to switch the contents of the variables. 
You are not allowed to type the words "milk" or "juice". 
You are only allowed to use variables to solve this exercise.
'''

glass1 = "milk"
glass2 = "juice"
glass3 = glass1
glass1 = glass2
glass2 = glass3

'''
Day 1 Project: Band Name Generator <
- Create a greeting for your program.
- Ask the user for the city that they grew up in and store it in a variable.
- Ask the user for the name of a pet and store it in a variable.
- Combine the name of their city and pet and show them their band name.
'''

print("Welcome to the Band Name Generator!")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print("Your band name could be " + city_name + " " + pet_name)



# Notes
'''
Notes - Day 1
-> Print
-> String Manipulation
-> Variables
-> Debugging (NameError, SyntaxError)
* Thonny (Debbuging env)
'''

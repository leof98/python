"""
A program that prompts for a vanity plate and then output
Valid if meets all of the requirements or Invalid if it does not.
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
# - Max of 6 and a min of 2
    if len(s) > 6 or len(s) < 2:
        return False
# - Must start with at least two letters
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False
# - The first number used cannot be a 0
    elif s[2] == '0':
        return False
# - Numbers cannot be used in the middle of a plate
    elif s[2].isnumeric() and s[-1].isalpha():
        return False
    elif s[3].isnumeric() and s[-1].isalpha():
        return False
    elif s[-1].isnumeric() and s[-2].isalpha():
        return False
# - No periods, spaces, or punctuation marks are allowed
    elif '.' in s or '!' in s:
        return False
    else:
        return True

main()

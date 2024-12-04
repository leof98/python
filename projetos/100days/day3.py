# Day 3

'''
Day 3 Project: Treasure Island <
'''
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?")
first_choice = input('Type "left" or "right"\n').lower()

if first_choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    print("Do you want to go to the island?")
    second_choice = input('Type "Go" or "Wait"\n').lower()
    if second_choice == "go":
        print("You've found three boxes: one red, one blue and one yellow")
        print("Each one do you want to open?")
        third_choice = input('Type "red", "blue" or "yellow"\n').lower()
        if third_choice == 'red':
            print("You've found the right box.\nCongratulations, You've won!")
        if third_choice == 'blue':
            print("The blue box had a bear inside, you're dead\nGame Over!")
        elif third_choice == 'yellow':
            print("The blue box was empty.\nGame Over!")
        else:
            print("Not a valid box. Game Over!")
    else:
        print("You died of boredom.\nGame Over!")
else:
    print("Wrong path.\nGame Over!")


# Notes
'''
Notes - Day 3
- If / Else / Elif
- Comparison Operators
- Logical Operators
-
-
- Identation Error
'''

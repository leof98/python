"""
A program that prompts consumers users to input a fruit and then
outputs the number of calories in one portion of that fruit.
04.22, 11.22
"""
def main ():
    fruits = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "90",
        "melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80"
    }

    fruit = str(input('Item: ')).lower()
    if fruit in fruits:
        print('Calories:',fruits[fruit])

main()

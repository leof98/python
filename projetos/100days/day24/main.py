# Day 24
PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for name in names_list:
    fixed_name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, fixed_name)
    with open(f"./output/ReadyToSend/letter_for_{fixed_name}.docx", mode="w") as file:
        file.write(new_letter)

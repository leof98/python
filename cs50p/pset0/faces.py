# Implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂.

def main():
    txt = str(input())
    txt = txt.replace(":)", "🙂")
    txt = txt.replace(":(", "🙁")
    print(txt)

main()

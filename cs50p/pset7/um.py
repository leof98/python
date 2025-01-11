import re

def main():
    print(count(input('Text: ')))

def count(s):
    x = 0
    n_um = re.findall(r'\b\W*um\W*\b', s, re.IGNORECASE)
    for _ in n_um:
        x += 1
    return(x)


if __name__ == '__main__':
    main()

from validator_collection import checkers

def main():
    txt = input('What\'s your email address? ')
    if checkers.is_email(txt):
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()

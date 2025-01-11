from datetime import date
import sys
import inflect

def validate(date_string):
    year, month, day = date_string.split('-')
    converted_date = date(int(year), int(month), int(day))
    return converted_date

def main():
    word_converter = inflect.engine()
    today_date = date.today()
    user_input = input('Date of birth: ')
    try:
        birth_date = validate(user_input)
    except:
        sys.exit('Invalid date')

    date_dif = today_date - birth_date
    date_in_words = word_converter.number_to_words(int(date_dif.total_seconds() / 60), andword='')
    print(f'{date_in_words.capitalize()} minutes')


if __name__ == '__main__':
    main()

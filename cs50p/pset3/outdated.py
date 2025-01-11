"""
Prompts for a date, in month-day-year order, formatted like 9/8/1636 or September 8, 1636
then output that same date in YYYY-MM-DD format. If the input is not a valid date in either format, prompt again.
11.22
"""

def main():

    list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

# 2 formatos possiveis: 01/02/1900 ou January 2, 1900

    while True:
# Primeiro formato: separa (pela /) a data em mes dia e ano depois verifica os dois.
        try:
            date = input('Date: ')
            month, day, year = date.split('/')
            if month.isalpha():
                main()
            elif int(month) > 12 or int(day) > 31:
                main()
# Segundo formato: separa pelo espaco a data, verifica se ha virgula no dia e depois remove
        except:
                month, day, year = date.split(' ')
                if ',' not in day:
                    main()
                day = day.replace(',','')
                if day.isalpha():
                    main()
                elif int(day) > 31:
                    main()
# Verifica se o mes por extenso esta na lista, se estiver, acrescenta 1 para bater com a data
                if month in list:
                    month = list.index(month) + 1
# Remove o espaco do ano e imprime a data formatada em YYYY-MM-DD
        year = year.strip()
        print(f'{year}-{int(month):02}-{int(day):02}')
        break

main()

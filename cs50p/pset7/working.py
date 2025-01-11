import re

def main():
    print(convert(input('Hours: ')))

def convert(s):
    if hours := re.search(r'^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$', s):
        f_hours = hours.groups()
        if int(f_hours[1]) > 12 or int(f_hours[5]) > 12:
            raise ValueError
        a_final = n_convert(f_hours[3], f_hours[1], f_hours[2])
        b_final = n_convert(f_hours[7], f_hours[5], f_hours[6])
        return a_final + ' to ' + b_final
    else:
        raise ValueError

def n_convert(am, hour, minute):
    if am == 'PM':
        if int(hour) == 12:
            n_hour = 12
        else:
            n_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            n_hour = 0
        else:
            n_hour = int(hour)
    if minute == None:
        z_minute = ':00'
        converted = f'{n_hour:02}' + z_minute
    else:
        converted = f'{n_hour:02}' + ':' + minute
    return converted


if __name__ == '__main__':
    main()

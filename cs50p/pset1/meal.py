def main():
    time = input('What time is it? ')
    convert(time)

def convert(time):
    hours, minutes = time.split(':')
    hours = int(hours) * 60
    minutes = int(minutes)
    t = hours + minutes
    if t >= 420 and t <= 480:
        print('breakfast time')
    elif t >= 720 and t <= 790:
        print('lunch time')
    elif t >= 1080 and t <= 1140:
        print('dinner time')

if __name__ == '__main__':
    main()

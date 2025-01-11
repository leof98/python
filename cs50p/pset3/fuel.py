def main():

    while True:
        try:
            fraction = input('Fraction: ')
            fraction = fraction.split('/')
            x,y = int(fraction[0]),int(fraction[1])
            fuel = (x / y) * 100

            if x > y:
                pass
            elif fuel <= 1:
                print('E')
                break
            elif fuel > 75:
                print('F')
                break
            else:
                fuel = round(fuel)
                print(f'{fuel}%')
                break

        except (ValueError, ZeroDivisionError):
            pass

main()

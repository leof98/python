import re

def main():
    print(validate(input('IPv4 Address: ')))

def validate(ip):
    if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
        ip_numbers = ip.split('.')
        for number in ip_numbers:
            if int(number) > 255:
                return False
            else:
                pass
        return True
    else:
        return False

if __name__ == '__main__':
    main()

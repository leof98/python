import re

def main():
    print(parse(input('HTML: ')))

def parse(s):
    if re.search(r'<iframe(.)*><\/iframe>', s):
        url = re.search(r'(http(s)*:\/\/(www.)?youtube\.com\/embed\/)([a-zA-Z0-9_]+)', s)
        if url:
            new_url = url.groups()
            f_url = 'https://youtu.be/' + new_url[3]
            return (f_url)

if __name__ == '__main__':
    main()

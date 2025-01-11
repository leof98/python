import sys

def main():
        check_command_line()
        try:
            file = open(sys.argv[1], 'r')
            lines = file.readlines()
        except FileNotFoundError:
            print('File does not exist')
        num_lines = 0
        for line in lines:
            if check_line(line) == False:
                num_lines += 1
        print(num_lines)

# Função para verificar argumentos de linha de comando
def check_command_line():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if '.py' not in sys.argv[1]:
        sys.exit('Not a Python file')


# Função para verificar espaços em branco e comentários
def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == '__main__':
    main()

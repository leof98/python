import sys
import csv
from tabulate import tabulate

"""
Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio's format, and outputs a table
formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library's grid format.
If the user does not specify exactly one command-line argument, or if the specified file's name does not end in .csv,
or if the specified file does not exist, the program should instead exit via sys.exit.
"""

def main():
    check_command_line_argument()
    # Variavel para armazenar a tabela
    table = []
    # Tenta abrir o arquivo
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    # Se o arquivo nao abrir, ele nao existe. Logo, um erro e exibido e o programa encerrado
    except FileNotFoundError:
        sys.exit('File does not exist')
    # Formata a tabela para o formato grid e imprime a tabela
    print(tabulate(table[1:], headers=table[0], tablefmt='grid'))

# Verifica argumentos de linha de commando
def check_command_line_argument():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')

if __name__ == '__main__':
    main()

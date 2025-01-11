import sys
import csv

def main():
    check_cl_arguments()

    # Cria a variável output que irá armazenar a lista alterada
    output = []

    # Tenta abrir o arquivo csv
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            # Loop por cada linha do 'reader'
            for row in reader:
                # Separa a lista pela vírgula
                n_name = row['name'].split(',')
                # Acrescenta o nome e o sobronome (na ordem desejada, agora), depois a casa
                output.append({'first': n_name[1].lstrip(), 'last': n_name[0], 'house': row['house']})
    # Caso o arquivo fornecido não exista, o programa é encerrado
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')  # Informa qual arquivo não abriu

    # Escreve o novo arquivo csv
    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first','last', 'house'])
        writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        for row in output:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})

# Função para verificar os parâmetros da linha de comando
def check_cl_arguments():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a csv file')

if __name__ == '__main__':
    main()

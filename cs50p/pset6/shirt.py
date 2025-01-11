import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_cl_arg()
    # Separa os arquivos no '.', o nome da extensão fica no [1] da lista
    input_file = splitext(sys.argv[1])
    output_file = splitext(sys.argv[2])

    if check_file_ext(input_file[1]) == False:
        sys.exit('Invalid Input')
    if check_file_ext(output_file[1]) == False:
        sys.exit('Invalid Input')
    if check_diff_ext(input_file[1], output_file[1]) == False:
        sys.exit('Input and ouput have different extensions')

    # Tenta abrir a imagem, se não conseguir, exibe o erro encerra o programa
    try:
        image_input = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    shirt = Image.open('shirt.png')
    size = shirt.size
    muppet = ImageOps.fit(image_input, size)
    # Edita a imagem com a foto da camiseta
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2]) # Salva a imagem editada em um novo arquivo

# Função para verificar os 'inputs' fornecidos
def check_cl_arg():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

# Função para verificar a extensão dos arquivos
def check_file_ext(file):
    if file in ['.jpg', '.jpeg', '.png']:
        return True
    return False

# Função para verificar se as extensões dos arquivos são iguais
def check_diff_ext(input, output):
    if input == output:
        return True
    return False

if __name__ == '__main__':
    main()

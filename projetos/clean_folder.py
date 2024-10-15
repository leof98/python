import os
import datetime
import shutil

# caminhos para a pasta
downloads_folder = r'\Users\Leo\Downloads'
old_downloads_folder = r'\Users\Leo\Downloads\old_downloads' # pasta para arquivos antigos
pdf_downloads_folder = r'\Users\Leo\Downloads\pdf_downloads'  # pasta para PDFs
exe_downloads_folder = r'\Users\Leo\Downloads\installer_downloads'  # pasta para arquivos .exe
zip_downloads_folder = r'\Users\Leo\Downloads\zip_downloads'  # pasta para arquivos .zip

# Arquivo a ser excluído da organização
excluded_file = 'clean_folder.py'

# Calcula a data três meses atrás
three_months_ago = datetime.datetime.now() - datetime.timedelta(days=0)

# Cria as pastas se elas não existirem
if not os.path.exists(old_downloads_folder):
    os.makedirs(old_downloads_folder)
if not os.path.exists(pdf_downloads_folder):
    os.makedirs(pdf_downloads_folder)
if not os.path.exists(exe_downloads_folder):
    os.makedirs(exe_downloads_folder)
if not os.path.exists(zip_downloads_folder):
    os.makedirs(zip_downloads_folder)

# MAIN CODE
# Itera pelos arquivos na pasta de Downloads
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # Verifica se o arquivo é um arquivo regular (não um diretório)
    if os.path.isfile(file_path):
        # Verifica se o arquivo é o arquivo a ser excluído
        if filename == excluded_file:
            continue
        # Verifica se o arquivo é um PDF
        if filename.lower().endswith('.pdf'):
            # Move o arquivo PDF para a pasta pdf
            shutil.move(file_path, os.path.join(pdf_downloads_folder, filename))
            print(f"Moved {filename} to the pdf_downloads folder.")
        # Verifica se o arquivo é um executável
        elif filename.lower().endswith('.exe'):
            # Move o arquivo .exe para a pasta installer
            shutil.move(file_path, os.path.join(exe_downloads_folder, filename))
            print(f"Moved {filename} to the installer_downloads folder.")
        elif filename.lower().endswith('.zip') or filename.lower().endswith('.rar'):
            # Move o arquivo .zip para a pasta zip
            shutil.move(file_path, os.path.join(zip_downloads_folder, filename))
            print(f"Moved {filename} to the zip_downloads folder.")
        else:
            # Obtém o tempo de modificação do arquivo
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

            # Compara o tempo de modificação com três meses atrás
            if modification_time < three_months_ago:
                # Move o arquivo para a pasta old_downloads
                shutil.move(file_path, os.path.join(old_downloads_folder, filename))
                print(f"Moved {filename} to the old_downloads folder.")

print("Cleanup completed.")

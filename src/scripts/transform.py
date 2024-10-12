import zipfile
import os
caminho_arq_zzip = 'src/database/archive.zip'
caminho_extrair = 'src/database/'

if os.path.exists(caminho_extrair):
    with zipfile.ZipFile(caminho_arq_zzip, 'r') as zip_obj:
        zip_obj.extractall(caminho_extrair)

    print('Extraido com sucesso')
else:
    print('Erro')

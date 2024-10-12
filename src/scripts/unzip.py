import zipfile
import os
from PATHS import CAMINHO_ZIP, CAMINHO_DATABASE

if os.path.exists(CAMINHO_DATABASE):
    with zipfile.ZipFile(CAMINHO_ZIP, 'r') as zip_obj:
        zip_obj.extractall(CAMINHO_DATABASE)

    print('Extraido com sucesso')
else:
    print('Erro')

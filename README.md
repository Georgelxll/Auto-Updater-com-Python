# Arquivo Copy.py é uma atualização de um script meu para realizar atualizações em arquivos com base em data, basicamente um auto updater.

* Para deixar ele rodando de forma funcional, é necessário instalar algumas bibliotecas.

--< *INSTALAÇÃO DE BIBLIOTECAS* >--
Bom, as bibliotecas utilizadas neste código são:

psutil
subprocess
tkinter
requests
zipfile
os
time

siga estas etapas:

Abra o terminal ou prompt de comando:

No Windows, você pode usar o cmd ou o PowerShell.
No macOS ou Linux, você pode usar o terminal.
Atualize o pip (opcional, mas recomendado):

python -m pip install --upgrade pip
Instale as bibliotecas usando pip:

Para instalar as bibliotecas que estão disponíveis no PyPI (Python Package Index), use o comando:

pip install psutil requests
As bibliotecas subprocess, tkinter, zipfile, os, e time já fazem parte da biblioteca padrão do Python, então não é necessário instalá-las separadamente.

*Verifique a instalação:*

Para garantir que as bibliotecas foram instaladas corretamente, você pode tentar importá-las em um script Python:

import psutil
import subprocess
import tkinter
import requests
import zipfile
import os
import time

print("Todas as bibliotecas foram importadas com sucesso!")
Solução de problemas:

Caso enfrente algum problema durante a instalação, verifique se está usando a versão correta do pip correspondente à versão do Python que você está utilizando (por exemplo, pip3 para Python 3).

--< *COMPILANDO O SCRIPT PARA EXE* >--

Instale o PyInstaller:
Abra o terminal ou prompt de comando e execute o seguinte comando para instalar o PyInstaller:

pip install pyinstaller
Compile o Script:
Navegue até o diretório onde está o seu script Python e execute o seguinte comando:

pyinstaller --onefile --noconsole seu_script.py
Substitua seu_script.py pelo nome do seu script Python. As opções usadas são:

--onefile: Gera um único arquivo .exe.
--noconsole: Remove a janela de console ao executar o executável (útil para aplicativos com GUI).

*Localize o Arquivo Executável:*
Após a compilação, o executável será criado na pasta dist, dentro do diretório onde você rodou o comando. O arquivo será chamado seu_script.exe.

*Execute o Executável:*
Navegue até a pasta dist e execute o arquivo .exe gerado.

--< *CONFIGURAÇÃO DO CÓDIGO* >--
 

def start_otclient():
    return subprocess.Popen(["path/to/otclient.exe"])

path/to/otclient.exe--> Altere pelo caminho onde fica o exe do seu cliente
 

url = "http://exemplo.com/arquivo.zip"  # URL fixa
 

url =  --> Caminho do seu site onde contém os arquivos que serão upados.

import psutil as ps
import subprocess
import tkinter as tk
from tkinter import ttk
from threading import Thread
import requests
import zipfile
import os
import time

def start_otclient():
    return subprocess.Popen(["path/to/otclient.exe"])

def stop_process(proc):
    for p in ps.process_iter(attrs=['pid', 'name']):
        if p.info['pid'] == proc.pid:
            p.suspend()
            return True
    return False

def resume_process(proc):
    for p in ps.process_iter(attrs=['pid', 'name']):
        if p.info['pid'] == proc.pid:
            p.resume()
            return True
    return False

def download_and_extract(progress_var, status_label, proc):
    if not stop_process(proc):
        status_label.config(text="Não foi possível parar o processo otclient.exe.")
        return

    url = "http://exemplo.com/arquivo.zip"  # URL fixa

    try:
        status_label.config(text="Baixando arquivo...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Verifica se houve erro no download
        total_length = int(response.headers.get('content-length', 0))
        bytes_downloaded = 0
        with open("arquivo.zip", 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progress_var.set(int((bytes_downloaded / total_length) * 100))
    except requests.exceptions.RequestException as e:
        status_label.config(text="Erro ao baixar o arquivo: " + str(e))
        resume_process(proc)
        return

    status_label.config(text="Arquivo baixado com sucesso.")

    try:
        status_label.config(text="Extraindo arquivos...")
        with zipfile.ZipFile("arquivo.zip", 'r') as zip_ref:
            zip_ref.extractall()
    except Exception as e:
        status_label.config(text="Erro ao extrair os arquivos: " + str(e))
        resume_process(proc)
        return

    status_label.config(text="Arquivos extraídos com sucesso.")
    os.remove("arquivo.zip")
    status_label.config(text="Arquivo zip removido.")

    resume_process(proc)
    status_label.config(text="Processo otclient.exe retomado.")

def start_download(progress_var, status_label, proc):
    progress_var.set(0)
    download_thread = Thread(target=download_and_extract, args=(progress_var, status_label, proc))
    download_thread.start()

def main():
    proc = start_otclient()
    time.sleep(5)  # Espera o otclient.exe iniciar

    root = tk.Tk()
    root.title("Download e Extração de Arquivos")

    progress_var = tk.IntVar()
    progress_bar = ttk.Progressbar(root, mode='determinate', variable=progress_var)
    progress_bar.pack(pady=10)

    status_label = tk.Label(root, text="")
    status_label.pack(pady=10)

    start_button = tk.Button(root, text="Start", command=lambda: start_download(progress_var, status_label, proc))
    start_button.pack(pady=10)

    root.mainloop()

    proc.terminate()

if __name__ == "__main__":
    main()

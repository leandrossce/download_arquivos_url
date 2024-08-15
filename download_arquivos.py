import os
import requests
from urllib.parse import urlparse

def download_file(url, directory):
    # Extrai o nome do arquivo da URL
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # Verifica se o diretório existe, se não, cria o diretório
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Caminho completo onde o arquivo será salvo
    file_path = os.path.join(directory, filename)
    
    # Realiza o download do arquivo
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo salvo em: {file_path}")
    else:
        print(f"Falha ao fazer o download. Status do código HTTP: {response.status_code}")

if __name__ == "__main__":
    while True:
        # Solicita a URL e o diretório
        url = input("Informe a URL do arquivo: ")
        directory = input("Informe o diretório onde o arquivo será salvo (exemplo: C:\\Users\\leandro\\Desktop): ")
        
        # Chama a função de download
        download_file(url, directory)
        
        # Pergunta se o usuário deseja continuar ou sair
        continuar = input("Deseja baixar outro arquivo? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa.")
            break

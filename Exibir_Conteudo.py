import os
os.system('cls')

def exibir_conteudo_arquivo_txt():
    try:
        nome_arquivo = input("Digite o nome do arquivo: ")

        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {str(e)}")
exibir_conteudo_arquivo_txt()
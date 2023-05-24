import os
os.system('cls')

def gravar_arquivo_txt():
    try:
        nome_arquivo = input("Digite o nome do arquivo: ")
        conteudo = input("Digite o conteúdo a ser gravado: ")

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
        print("Arquivo gravado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao gravar o arquivo: {str(e)}")
gravar_arquivo_txt()
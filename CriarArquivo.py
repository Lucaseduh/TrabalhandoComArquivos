import os
os.system('cls')

def gravar_arquivo_txt(nome_arquivo, conteudo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
        print("Arquivo gravado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao gravar o arquivo: {str(e)}")

conteudo = "Ensinando a criar um arquivo txt."
nome_arquivo = "aula22_05.txt"
gravar_arquivo_txt(nome_arquivo, conteudo)
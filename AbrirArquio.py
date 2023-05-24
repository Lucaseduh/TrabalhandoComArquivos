import os
os.system('cls')

def exibir_conteudo_arquivo_txt(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        print("Conteúdo do arquivo")
        print(conteudo)
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {str(e)}")
nome_arquivo = "novo_arquivo"
exibir_conteudo_arquivo_txt(nome_arquivo)
import os
os.system('cls')

def exibir_e_alterar_conteudo_arquivo_txt(nome_arquivo):
    try:
        with open(nome_arquivo, 'w+') as arquivo:
            arquivo.seek(0)
            conteudo =arquivo.read()
            print("Conteúdo atual do arquivo:")
            print(conteudo)
            novo_conteudo = input("Digite o novo conteúdo a ser adicionado: ")
            arquivo.write(novo_conteudo)
        print("Conteúdo adicionado ao arquivo com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao ler/alterar o arquivo: {str(e)}")
nome_arquivo = "aula22_05.txt"
exibir_e_alterar_conteudo_arquivo_txt(nome_arquivo)
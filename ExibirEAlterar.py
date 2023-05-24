import os
os.system('cls')

def exibir_e_alterar_conteudo_arquivo_txt():
    try:
        nome_arquivo = input("Digite o nome do arquivo: ")
        with open(nome_arquivo, 'a+') as arquivo:
            arquivo.seek(0)
            conteudo = arquivo.read()
            print("Conteúdo atual do arquivo: ")
            print(conteudo)
            novo_conteudo = input("Digite o novo conteúdo a ser adicionado: ")
            arquivo.write(novo_conteudo)
        print("Conteúdo adicionado ao arquivo com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao ler/alterar o arquivo: {str(e)}")
exibir_e_alterar_conteudo_arquivo_txt()
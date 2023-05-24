import os
os.system('cls')

from docx import Document

def exibir_alterar_docx(nome_arquivo):
    #Abre o arquivo .docx
    doc = Document (nome_arquivo)

    #Exibie o conteudo atual do documento
    print("Conteúdo atual: ")
    for paragraph in doc.paragraphs:
        print(paragraph.text)

    #altera o conteúdo do documento
    novo_conteudo = input("Digite o novo conteúdo: ")

    #Limpa o conteúdo existente
    for paragraph in doc.paragraphs:
        paragraph.clear()
import os
os.system('cls')

from docx import Document

def exibir_docx(nome_arquivo):
    #Abre o arquivo .docx
    doc = Document(nome_arquivo)

    #Exibe o conteúdo do documento
    for paragraph in doc.paragraphs:
        print(paragraph.text)

#Exemplo de uso da função
nome_arquivo = 'euCriei.docx'
exibir_docx(nome_arquivo)
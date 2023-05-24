import os
os.system('cls')

from docx import Document

def criar_docx(nome_arquivo, conteudo):
    #Cria um objeto Document
    doc = Document()

    # Adiciona o conteúdo ao documento
    doc.add_paragraph(conteudo)

    # Salva o arquivo .docx
    doc.save(nome_arquivo)

#Exemplo de uso da função
nome_arquivo = 'EuCriei.docx'
conteudo = 'Olá, mundo!'
criar_docx(nome_arquivo, conteudo)
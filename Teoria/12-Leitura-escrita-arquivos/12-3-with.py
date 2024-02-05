"""
O bloco with

passo para se trabalhar com arquivos:

#1- Abrir o arquivo
#2- Manipular o arquvio
#3- Fechar o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with



"""
#O bloco with - Forma Pythonica de se manipular arquivos

with open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\texto.txt') as arquivo:
    print(arquivo.readlines())



"""
Sistema de Arquivos - Manipulação

import os

#Verificar se um arquivo ou diretório existe
#arquivo
print(os.path.exists('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\arquivo.txt')) #False
print(os.path.exists('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\novo_texto.txt')) #True

#diretório
print(os.path.exists('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos')) #True
print(os.path.exists('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\outro')) #False


#Criando arquivos

#forma1
open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\arquivo-teste1.txt', 'w').close()

#forma2
with open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\arquivo-teste2.txt', 'w') as arquivo:
    pass
   
#renomear os arquivos
os.rename()

#deletar arquivos
os.remote()


#Criando diretório
os.mkdir('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\diretorio-teste1')

#criar varios diretórios
os.makedirs()

#deletar diretórios vazios
os.rmdir()

"""



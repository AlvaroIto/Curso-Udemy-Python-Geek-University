"""
Sistema de arquivos e navegação

Para fazer o uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer o uso do módulo os.

os = Operating System - Sistema operacional
 

"""
#import
import os


#getcwd() - pegar o current work directory - diretório de trabalho corrente
#retorna o path(caminho) absoluto
print(os.getcwd())

#chdir() - mudar o diretório
os.chdir('..')
print(os.getcwd())

#path.isabs - verificar se o diretório é absoluto ou relativo
print(os.path.isabs('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University'))

#os.name - identificar o sistema operacional 
print(os.name)

#os.uname() - mais detalhes do sistema operacional para Linux
#print(os.uname())

#listdir() - listar os arquivos e diretórios
print(os.listdir())


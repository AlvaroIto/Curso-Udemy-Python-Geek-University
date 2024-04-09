'''
CSV - Comma Separeted Values - Valores separados por vírgula

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader = Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader = Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

########READER#######

from csv import reader

with open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\17-Arquivos-CSV-e-JSON\\lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #Pular o cabeçalho
    for linha in leitor_csv:
       print(f'{linha[0]} nasceu no[a] {linha[1]} e mede {linha[2]} centímetros')


#########DICTREADER################
from csv import DictReader

with open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\17-Arquivos-CSV-e-JSON\\lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")


'''

#Outro separador
from csv import DictReader

with open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\17-Arquivos-CSV-e-JSON\\lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter= ',')
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")

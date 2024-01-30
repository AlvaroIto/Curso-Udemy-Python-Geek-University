"""
Seek e Cursors

seek() -> É utilizada para mover o cursor pelo arquivo


"""
arquivo = open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\texto.txt')
print(arquivo.read()) 

#movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)
print(arquivo.read()) 

#realine() -> Função que lê o arquivo linha a linha
print(arquivo.readline())

#readlines() -> Função que lê as linhas do arquivo
print(arquivo.readlines())


#Passos para se trabalhar com um arquivo
#1- abrir o arquivo
arquivo = open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\texto.txt')
#2- Trabalhar com arquivo
print(arquivo.read())
#3- Fechar o arquivo
arquivo.close()

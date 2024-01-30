"""
Leitura de Arquivos

Para ler o conteudo de um arquivo em Python, utilizamos a função integrada open()

open() -> Na forma mais simples passamos apenas um parâmetro de entrada que neste caso é o nome do arquivo a ser lido, essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos

#Exemplo
arquivo = open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\texto.txt')
print(arquivo) # <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
print(type(arquivo)) # <class '_io.TextIOWrapper'>
#mode r -> Modo leitura. r-> read() -> ler
#Para ler o conteúdo de um arquivo após sua abertura, devemos utilizar a função read()
print(arquivo.read())
#OBS: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor, funciona como o cursos quando estamos escrevendo.

"""

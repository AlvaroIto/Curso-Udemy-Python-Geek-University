"""
Escrever em arquivos

 Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler. Da mesma forma se abrirmos parar escrita, não podemos le-lo, somente escrever

#OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional
Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write()
Esta função recebe uma string como parâmetro
Abrindo um arquivo para escrita com o modo 'w' se o arquivo não existir será criado, caso ele ja exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo anterior será perdido

"""
#Exemplo de escrita - modo 'w' - write (escrita)
with open('C:\\Users\\j4p4_\\Documentos\\Projetos\\Curso-Udemy-Python-Geek-University\\Teoria\\12-Leitura-escrita-arquivos\\novo_texto.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a ultima linha.')


"""
StringIO

Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de leitura para ler o arquivo
    - Permissãao de escrita para escrever no arquivo

StringIO é utilizado para ler e criar arquivos em memória
Passos de utilização:
Import
from io import stringIO
mensagem = 'Este é apenas uma string normal'
arquivo = StringIO(mensagem)
print(arquivo.read())
arquivo.write('Outro texto')

"""
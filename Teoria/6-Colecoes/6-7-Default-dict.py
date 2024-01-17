"""
Módulo Collections - Default Dict

Ao criar um dicionário utilizando o default dict, nós informamos um valor padrão, podeendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor defautl será atribuido

"""
#Fazendo import
from collections import defaultdict

dicionario  = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python'
print(dicionario)
print(dicionario['outro'])
print(dicionario)


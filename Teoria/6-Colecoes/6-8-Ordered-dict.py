"""
Módulo Collections: Ordered dict

Em um dicionario a ordem de inserção dos elementos não é garantida


"""

#Fazendo o import
from collections import OrderedDict

dicionario  = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave{chave}: valor{valor}')

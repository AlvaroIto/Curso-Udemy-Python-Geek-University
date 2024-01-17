"""
Módulo Collections - Named Tuple

São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros
"""
#Fazendo o import
from collections import namedtuple

#Precisamos definir o nome e parâmetros

#forma1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

#forma2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

#forma3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#Usando
ray = cachorro(idade=2, raca='Chow-chow', nome='Ray')
print(ray)

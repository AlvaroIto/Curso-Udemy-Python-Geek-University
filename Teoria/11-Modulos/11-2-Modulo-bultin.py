"""
Módulos builtin (módulos integrados)

#Importando todo o módulo
importa random
print(random.random())

#Podemos importar todas as funções de um módulo utilizando o *
from random import *
print(random())

#Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())

#Importando mais de 1 função
from random import (
    random,
    randint,
    shuffle,
    choice
)


#

"""
from random import (
    random,
    randint,
    shuffle,
    choice
)
print(random())
print(randint(3, 6))
print(choice(range(10)))
lista = [1, 2, 3, 4, 5, 6, 7]
shuffle(lista)
print(lista)
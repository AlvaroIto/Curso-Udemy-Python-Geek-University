"""
Módulo Random e o que são módulos?

Em Pythonm módulos nada mais são do que outros arquivos Python
 
Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

Existem 2 formas de se utilizar módulos:

Forma 1 (não recomendada)
import random
print(rando.random())
#Ao realizar o import de todo o módulo, funções, atributos, classe e propriedades que estiverem dentro do módulo ficaram disponíveis.

Forma 2 (recomendada)
from random import random
for i in range(10):
    print(random())

uniform() -> gera um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform
print(uniform(3, 5))

randint() -> gera valor pseudo-aleatório entre os valores estabelecidos
from random import randint
print(randint(0, 19))

choice() -> Mostra um valor aleatório entre um iterável
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

shuffle() -> Função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(f'Cartas embaralhadas: {cartas}')

"""

"""
Funções de maior grandeza - higher order functions - HOF

Quando uma linguagem de programação suporta HOF indica que podemos ter funções que retornam outra funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções e até mesmo criar variáveis do tipo de funções nos nossos programas

#Exemplos
def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


#Nested functions - Funções Aninhadas
Em, PYthon, podemos ter funções dentro de funções (nested functions ou Inner functions)

#Exemplo
from random import choice
def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de vc '))
    return humor() + pessoa

print(cumprimento('Geek'))


#Retornando funções de outras funções
#Exemplo
from random import choice

def faz_me_rir():
    def rir():
        return choice(('kkkkkkkkk', 'ahahahhahahha', 'yayayayayyaya'))
    return rir

rindo = faz_me_rir()
print(rindo())


Inner Functions podem acessar o escopo de funções mais externas 

"""





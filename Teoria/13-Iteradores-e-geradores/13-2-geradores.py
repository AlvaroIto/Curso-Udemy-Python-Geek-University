"""
Geradores

- Geradores (generators) são iteradores (iterators), mas nem todo iterator é um generator
- Generators podem ser criados com funções geradoras.
- Funções geradoras utilizam a palavra reservada yield
- Generator podem ser criados com Expressões Geradoras

Diferenças entre Funções e Generator Functions

funções:
    Utilizam return
    retorna uma vez
    quando executada retorna um valor

generator functions:
    Utilizam yield
    pode utilizar yield multiplas vezes
    quando executada retorna um generator

"""

#Exemplo de generator function
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = conta_ate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) 
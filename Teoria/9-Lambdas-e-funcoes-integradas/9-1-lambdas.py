"""
Utilizando lambdas

Conhecidas por expressões lambdas, ou simplesmente lambdas, são funções sem nome, ou seja, funções anônimas

#Função em Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))


#Expressão Lambda
lambda x: 3 * x + 1

#Utilizando
calc = lambda x: 3 * x + 1
print(calc(4))


# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('angelina', 'JOLIE'))
print(nome_completo('  FELICITY            ', ' jones '))


# Em funções Python podemos ter nenhuma ou várias entradas, em lambdas também

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar)
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))


#Outro exemplo (ordenar a lista de autores pelo sobrenome):
autores = [ 'Isaac Asimov', 'Ray Bradburry', 'Rober Heinlein', 'Arthur C. Clarke', 'Frank Hebert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


"""


"""
Generators

Tuple Comprehension se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))


Generator ocupa menos espaço em memória

from sys import getsizeof

#Gerando uma lista de número com List comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
#Gerando uma lista de número com Set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
#Gerando uma lista de número com Dictionary comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
#Gerando uma lista de número com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

"""


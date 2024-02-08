"""
Entendendo Iterators e Iterables

Iterator:
    - Um objeto que pode ter iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada

 numeros = [1, 2, 3, 4, 5, 6] #É um iterable mas não um iterator

it = iter(numeros)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
"""

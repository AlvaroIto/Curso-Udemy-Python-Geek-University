"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance


"""
#Fazendo import
from collections import deque

#Criando deques
deq = deque('geek')
print(deq)

#Adionando elementos
deq.append('y')
print(deq)

deq.appendleft('k') #adicona no começo
print(deq)

#remover elementos
print(deq.pop())
print(deq)

print(deq.popleft()) #remove e retorna o primeiro elemento
print(deq)


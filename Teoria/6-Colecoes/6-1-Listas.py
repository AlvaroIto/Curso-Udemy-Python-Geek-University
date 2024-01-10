"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras lingaugems, com a diferença de serem DINÂMICO e também de podermos colocar QUALQUER tipo dado

- Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos.
- Qualquer tipo dedado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado

As listas em Python são representadas por: []

"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#Podemos checar se determinado valor está na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

#Podemos ordenar uma lista
lista1.sort()
print(lista1)

#Podemos contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#Podemos adicionar elementos em listas, utilizamos a função append
#Obs: com append só conseguimos adicionar 1 elemento por vez
print(lista1)
lista1.append(42)
print(lista1)

#Para adicionar mais de 1 elemento em uma lista, devemos usar o extend
lista1.extend([123, 44, 67])
print(lista1)

#Podemos inserir um novo elemento na lista informando a posição do índice
lista1.insert(2, 'Novo valor')
print(lista1)

#Podemos juntar 2 listas
lista6 = lista1 + lista2
print(lista6)

#Podemos reverter a lista
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

#Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#Podemos remover o último elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

#Remover um elemento pelo índice
lista5.pop(2)
print(lista5)

#Remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

#Converter uma string para uma lista
curso = 'Programação em Python essencial'
print(curso)
curso = curso.split()
print(curso)

#Converter uma lista em um string
lista7 = ['Programação', 'em', 'Python', 'Essencial']
print(lista7)
curso = ' '.join(lista7)
print(curso)

# Colocar qualquer tipo de dado
lista8 = [1, 2.45, True, 'Geek', 'd', [1, 2, 3], 2343254325]

#Iterando sobre listas
#Exemplo1
for elemento in lista1:
    print(elemento)

#Acessar lista de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

#Soma, valor maximo, valo minimo, tamanho
listanum = [1, 2, 3, 4, 5, 6]
print(sum(listanum))
print(max(listanum))
print(min(listanum))
print(len(listanum))

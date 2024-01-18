"""
Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em Python nós temos as listas

numeros = [1, 'b', 3.13, True, 5]


"""
#Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #matriz 3x3
print(listas)

#Acessando os dados
print(listas[0]) #[1, 2, 3]
print(listas[0][1]) #2 (linha 0 coluna 1)
print(listas[2][1]) #9 (linha 2 coluna 1)

#Iterando com loops em uma lista aninhada
for lista in listas:
    print(lista)
    for num in lista:
        print(num)

#List Comprehension

[[print(valor) for valor in lista] for lista in listas] # para cada lista em lista, e cada valor na lista, imprima valor



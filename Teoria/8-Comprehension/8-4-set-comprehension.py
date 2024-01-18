"""
Set Comprehension

Set = {1, 2, 3, 4, 5}


"""

#Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

#outro
numeros = {x ** 2 for x in range(10)}
print(numeros)

letras = {letra for letra in 'Geek University'}
print(letras)

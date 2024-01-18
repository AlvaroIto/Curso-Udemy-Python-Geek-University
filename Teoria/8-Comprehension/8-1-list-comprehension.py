"""
List Comprehension

- Utilizando list comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável

#Sintaxe:
[dado for dado in iteravel]

#Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros] # para cada número in numeros, multiplique numero vezes 10
print(res)

res = [numero / 2 for numero in numeros] # para cada número in numeros, divide numero por 2
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros] # para cada numero in numeros, aplique a função
print(res)


#List comprehension X loop

#loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

#List comprehension
print([numero * 2 for numero in numeros])

#Exemplo
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.title() for amigo in amigos])


Podemos adicionar estruturas condicionais lógicas

numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)


res = [nuemro * 2 if numero % 2 == 0 else numero / 2 for numero in numeros] # Para cada numero in numeros, multiplique numero por 2 se for para senão divida numero por 2

"""

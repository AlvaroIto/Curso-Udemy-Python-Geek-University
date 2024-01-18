"""
Dictionary Comprehension

#Sintaxe
{chave:valor for valor in iteravel}

#Exemplos

"""

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave:valor ** 2 for chave, valor in numeros.items()} #para cada chave e valor, eleve o valor ao quadrado dos itens de numeros
print(quadrado)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mix = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mix)

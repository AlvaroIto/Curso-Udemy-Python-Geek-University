"""
Loop for

Loop é uma estrutura de repetição.
For é uma dessas estruturas

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplo itarável:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in list(numeros):
    print(numero)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
for n in range(1, qtd):
    print(f'Impriminando {n}')

qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')

"""

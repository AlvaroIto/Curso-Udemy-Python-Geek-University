"""
Zip

zip() - Cria um iterável (Zip object) que agrega elemento de cada um dos iteráveis passados como entrada em pares

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip = zip(lista1, lista2, 'abc')
print(list(zip))

#O zip() utilizad como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando com iteráveis de tamanhos diferentes, irá apra quando os elementos do menor iterável acabar
lista3 = [7, 8, 9, 10, 11]
zip = zip(lista1, lista2, lista3)
print(list(zip))

"""
 
"""
Map

Com Map fazemos mapeamento de valores para a função
Map é uma função que recebe dois parametros: O primeiro a função e o segundo um interável
Apos utilizar a função map() depois da primeira utilização do resultado ele zera


import math
def area(r):
    #Calcula a área de um círculo com raio 'r'
    return math.pi * (r ** 2)

print(area(2))


raios = [2, 5, 7.1, 0.3, 10, 44]

#forma comum
areas = []
for r in raios:
    areas.append(area(r))
print(areas)


#Forma Map
areas = map(area, raios)
print(list(areas))


#Forma Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

"""

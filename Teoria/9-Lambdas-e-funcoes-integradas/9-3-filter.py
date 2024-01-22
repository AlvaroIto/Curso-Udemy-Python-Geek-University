"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção
Assim como Map, a filter() recebe dois parâmetros, sendo uma função e um iterável
E apos serem utilizados os dados, eles são excluidos da memória

"""
import statistics

# dados colelatod de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

res = filter(lambda x: x > media, dados)
print(media)
print(list(res))


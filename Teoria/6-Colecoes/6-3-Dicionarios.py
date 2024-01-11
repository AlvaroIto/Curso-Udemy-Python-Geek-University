"""
Dicionários

OBS: EM algumas linguagens de programação, os dicionários Python são conhecidos por mapas

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.
Obs:
    - CHave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados

#Forma 1
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

#Forma 2
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#Acessando elementos

#Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

#Forma 2 - Acessando via get (recomendado)
print(paises.get('br'))
print(paises.get('py'))
print(paises.get('ru')) # None

#Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário, como chaves de dicioários
#Adicionar elementos
localidades = {
    (35.7634, 14.5436): 'Escritório em Tókio',
    (23.4234, 23.1234): 'Escritório em Nova York',
    (43.2344, 65.2344): 'Escritório em São Paulo'
}
print(localidades)

#Forma 1
localidades[(43.2344, 43.3424)] = 'Escritório em Dubai'
print(localidades)

#Forma 2
localidades.update({(65.3452, 78.4325): 'Escritório em Madri'})
print(localidades)

#A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
#Em dicionários, NÃO podemos ter chaves repetidas.

#Remover dados
localidades = {
    (35.7634, 14.5436): 'Escritório em Tókio',
    (23.4234, 23.1234): 'Escritório em Nova York',
    (43.2344, 65.2344): 'Escritório em São Paulo'
}
print(localidades)

#Forma 1 - Recomendado
localidades.pop((43.2344, 65.2344))
#Precisamos informar a chave

#Forma 2
del localidades[(35.7634, 14.5436)]
print(localidades)

"""


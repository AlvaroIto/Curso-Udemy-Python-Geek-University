"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a Teoria dos Conjuntos da Matemática

- No Python os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:
- Sets não possuem valores duplicados
- Sets não possuem valores ordenados
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles, quando não precisamos se preocupar com chaves, valores e itens duplicados

Os conjuntos são referenciados em Python com chaves {}

Diferenção entre conjuntos e mapas em Python
    - Um dicionario tem chave/valor

    - Um conjuntos tem apenas valor


#Definindo um conjunto:
#Forma1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #valores repetidos
print(s)
print(type(s))

#OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro e não fará parte do conjunto

#Forma2 mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

#Assim como todo outro conjunto em Python, podemos colocar tipos de dados misturados
s = {1, 'b', True, 34.22, 23}
print(s)
print(type(s))

#Podemos iterar em um set
for valor in s:
    print(valor)

#Exemplo de uso em Sets:

#Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam manualmente a cidade de onde vieram
#Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiabá']

#Agora precisamos saber quantas cidades distintas temos.
print(len(set(cidades)))

"""

#Métodos matemáticos de conjuntos

#imagine que temos dois conjuntos: Um de estudantes de Python e outro de estudantes de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#Veja que alguns alunos que estudam Python também estudam Java

#Precisamos gerar um conjunto com onmes de estudantes unicos
#Forma1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

#Forma2 - Utilizando pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

#Precisamos gerar um conjunto de estudantes que estão em ambos os cursos
#Forma1 - Utilziando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#Forma2 - Utilizando &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

#Precisamos gerarm um conjuntos que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)


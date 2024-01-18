"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece com astrisco
Exemplo:
*xis
Mas por convenção, utilizamos *args para defini-lo

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em um tupla. Então desde já lembre-se que tuplas são imutáveis
"""

#Exemplos

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros(4, 6, 9, 3, 2, 1, 4, 5, 4))



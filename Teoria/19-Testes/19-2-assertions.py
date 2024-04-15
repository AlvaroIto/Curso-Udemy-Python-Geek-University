'''
Assertions (Checagens/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes

Utilizamos o assert em uma expressão que queremos checar se é válida ou não
Se a expressão for verdadeira o assert retorna None e caso seja falsa levanta um erro do tipo AssertionError

OBS: Se um programa Python for exectuado com um parametro -O, nenhum assertion será validado, ou seja, todas suas validações já eram.

'''

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b

print(soma_numeros_positivos(2, 4))
#print(soma_numeros_positivos(0, 4)) #AssertionError: Ambos os números precisam ser positivos
#print(soma_numeros_positivos(2, 0)) #AssertionError: Ambos os números precisam ser positivos


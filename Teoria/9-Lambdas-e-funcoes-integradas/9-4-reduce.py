"""
Reduce

A partir da versão 3+ a função reduce() não é mais uma função integrada (bult-in)
Agora devemos que importar e utilizar essa função a partir do módulo functool

Gui van ROssum: Utilize a função reduce() se você realemnte precisa, Em todo caso, 99% das vezes um loop for é mais legível

Para entender o reduce()
#Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3, ..., an]
#Você tem uma função que recebe dois parametros
def funcao(x, y):
    return x * y
#Assim como o map() e filter(), a função reduce() recebe dois parametros: função e o iterável
reduce(funcao, dados)
#Afunção reduce(), funciona da seguinte forma:
    Passo1: res1 = f(a1, a2) #Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo2: res2 = f(res1, a3) #Aplica a função passando o resultado do passo1 mais o terceiro elemento e guardo o res
    Isso é repetido até o final
    Passon: resn = f(resm, an)


"""
#Prática
from functools import reduce
#Função reduce() para multiplicar todos os números de uma lista
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
#Para utilizar o reduce() nós precisamos de uma função que recebe dois parametros
mult = lambda x, y: x * y
res = reduce(mult, dados)
print(res)


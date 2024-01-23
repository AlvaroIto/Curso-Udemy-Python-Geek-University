"""

Len, abs, sum, round

#LEN
len() - Retorna o tamanho, ou seja, o número de itens de um iterável
print(len('Geek University'))
print(len([1, 2, 3, 4, 5]))

#ABS
abs() - Retorna o valor absoluto de um número inteiro ou real, ou seja, retorna o valor real sem o sinal
print(abs(-5))
print(abs(5))
print(abs(-3.14))
print(abs(3.14))

#SUM
sum() -  Recebe como parâmetro um interável, podendo receber um valor inicial e retorna a soma total dos elementos, incluindo o valor inicial
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

#ROUND
round() - Retorna um número arredondado para n digito de precisão apos a casa decima. Se a precisão não for informada retorna o inteiro mais próximo da entrada
print(round(10.2))
print(round(1.2121212, 2))
print(round(1.2199999, 2))

"""
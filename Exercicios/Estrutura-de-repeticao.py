#1. Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0. 
'''
mult = 0
for num in range(1, 6):
    mult += 3
    print(mult, end=' ')
'''


#2. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar a estrutura de repeticao for, a segunda while, e a terceira do while. 
'''
print('Estrutura for')
for n in range(1, 101):
    print(n, end=' ')

print('\nEstrutura while')
num = 1
while num <= 100:
    print(num, end=' ')
    num += 1
'''

#3. Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” após a contagem. 
'''
num = 10
while num >= 0:
    print(num)
    num -= 1
print('FIM!')
'''


#4. Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil). 
'''
num = int(input('Digite um número: '))
while num <= 100000:
    print(num)
    num += 1000
'''


#5. Faça um programa que peça ao usuario para digitar 10 valores e some-os. 
'''
lista_num = []
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    lista_num.append(num)

print(f'Números digitados: {lista_num}\n'
      f'Soma: {sum(lista_num)}')
'''


#6. Faça um programa que leia 10 inteiros e imprima sua média. 
'''
lista_num = []
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    lista_num.append(num)

print(f'Números digitados: {lista_num}\n'
      f'Médida: {sum(lista_num) / len(lista_num)}')
'''


#7. Faça um programa que leia 10 inteiros positivos, ignorando nao positivos, e imprima sua média. 
'''
lista_num = []
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    lista_num.append(abs(num))

print(f'Números digitados: {lista_num}\n'
      f'Médida: {sum(lista_num) / len(lista_num)}')
'''


#8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido. 
'''

lista_num = []
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    lista_num.append(num)

print(f'Menor número digitado: {min(lista_num)}')
print(f'Maior número digitado: {max(lista_num)}')
'''


#9. Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais impares. 
'''
cont = 1
num = int(input('Digite um número: '))
print(f'Os primeiros {num} números ímpares:')

for n in range(num):
    print(f'{cont}')
    cont += 2
'''


#10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
'''
num = 0
while num < 100:
    print(num)
    num += 2
'''


#11. Faga um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente. 
'''
num = int(input('Digite um número: '))
for n in range(num):
    print(n)
'''


#12. Faca um programa que leia um número inteiro positivo V e imprima todos os números naturais de 0 até N em ordem decrescente. 
'''
num = int(input('Digite um número: '))
while num >= 0:
    print(num)
    num -= 1
'''


#13. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até V em ordem crescente. 
'''
num = int(input("Digite um número par: "))
if num % 2 != 0:
    print(f'Número {num} não é par!')
else:
    cont = 0
    while cont <= num:
        print(cont)
        cont += 2
'''
 

#14. Faga um programa que leia um número inteiro positivo par V e imprima todos os números pares de 0 até V em ordem decrescente. 
'''
num = int(input("Digite um número par: "))
#lista_num = list(range(num))
if num % 2 != 0:
    print(f'Número {num} não é par!')
else:
    cont = 0
    while num >= cont:
        print(num)
        num -= 2
'''

#15. Faca um programa que leia um número inteiro positivo impar N e imprima todos os numeros impares de 1 até V em ordem crescente. 
'''
num = int(input("Digite um número ímpar: "))
if num % 3 != 0:
    print(f'Número {num} não é ímpar!')
else:
    cont = 0
    while cont <= num:
        print(cont)
        cont += 3
'''

#16. Faça um programa que leia um número inteiro positivo impar N e imprima todos os números impares de 1 até NV em ordem decrescente. 
'''
num = int(input("Digite um número ímpar: "))
if num % 3 != 0:
    print(f'Número {num} não é ímpar!')
else:
    cont = 1
    while num >= cont:
        print(num)
        num -= 3
'''

#17. Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais. 
'''
num = int(input('Digite um número: '))
soma = 0
for n in range(num):
    soma += n

print(f'Soma dos números {list(range(num))} = {soma}')
'''


#18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de numeros a serem lidos deve ser fornecida pelo usuario. 
'''
lidos = int(input('Quantos números serão lidos?: '))
cont = 1
maior = 0
cont_maior = 0
while cont <= lidos:
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
        cont_maior += 1
    cont += 1

print(f'Quantidade de números inseridos: {lidos}\n'
      f'Maior número: {maior}\n'
      f'Quantidade de vezes que o maior número foi lido: {cont_maior}')
'''        


#19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saida cada um dos algarismos que compõem o número 
'''
num = int(input('Digite um número: '))
if num < 100 and num >= 1000:
    print('O número precisa ser entre 100 e 999!')
else:
    print(f'Unidade: {num % 10}') 
    print(f'Dezena: {(num % 100) // 10}')
    print(f'Centena: {(num // 100)}')
'''


#20. Ler uma sequência de números inteiros e determinar se eles sao pares ou não. Devera ser informado o número de dados lidos e número de valores pares. O processo termina quando for digitado o nimero 1000.
'''
lista_num = []
lista_par = []
num = 0
while num != 1000:
    num = int(input('Digite um número ou 1000 para sair: '))
    lista_num.append(num)
    if num % 2 == 0:
        lista_par.append(num)
lista_num.remove(1000)
lista_par.remove(1000)

print(f'Lista de números digitados: {lista_num}\n'
      f'Lista de números pares digitados: {lista_par}')
'''


#21. Faça um programa que receba dois nimeros. Calcule e mostre: e a soma dos nimeros pares desse intervalo de nimeros, incluindo os nimeros digitados; e a multiplicagao dos nimeros impares desse intervalo, incluindo os digitados; 

#22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequéncia arbitraria de notas (validas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética. O número de notas com que o aluno pretenda efetuar o célculo nao será fornecido ao programa, o qual terminara quando for introduzido um valor que não seja valido como nota de aprovação. 

#23. Faca um algoritmo que leia um número positivo e imprima seus divisores. 

#24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com excecao dele proprio. Ex: a soma dos divisores do número 66 é 1+42+3+6+11+22+33=78 

#25. Faga um programa que some todos os nimeros naturais abaixo de 1000 que sao múltiplos de 3ou 5. 

#26. Faca um algoritmo que encontre o primeiro maltiplo de 11, 13 ou 17 apés um número dado. 

#27. Em Matematica, o nimero harménico designado por H (n) define-se como sendo a soma da série harménica: H(n)=1+1/2+1/34+1/4+...4+1/n 
#Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H (n).

#28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor £, conforme a fórmula a seguir E=1+1/14+1/2141/314+..+1/N! 

#29. Escreva um programa para calcular o valor da série, para 5 termos. S=0+1/214+2/41+3/6!+... 

#30. Faça programas para calcular as seguintes sequências: 1+2+3+4+5+..+m 

#31. Faça um programa que calcule e escreva o valor de S. S = (1/3) + (3/2) + (5/3) + (7/4) + ... + (99/50)

#32. Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado e a relação entre eles (>,<,=) de cada lançamento. 

#33. Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. Exemplo: Paran=6,i=2ej=3asaída deverá ser: 0,2,3,4,6,8.

#34. Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20? Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto. 

#35. Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números impares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela, “Intervalo de valores invalido” e o programa termina. Exemplo de tela de saída: Digite o valor inicial e valor final: 5 10 
#Soma dos impares neste intervalo: 21 

#36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números naturais é, (1**2) + (2**2) + ... + (10 ** 2) = 385 O quadrado da soma dos dez primeiros números naturais é, (1+2+..+10)**2 = 552 = 3025 
#A diferenca entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025-385 = 2640.


#37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte: a soma dos dois digitos de mais baixa ordem com os dois digitos de mais alta ordem elevada ao quadrado é igual ao próprio numero. Por exemplo, para o inteiro 3025, temos que: 30 + 25 = 55 55 ** 2 = 3025 

#38. Faça um programa que calcule o terno pitagorico a, b, c, para o qual a+ b+ c = 1000. Um terno pitagdrico é um conjunto de trés nimeros naturais, a, b, c, para a qual, (a ** 2) + (b ** 2) + (c ** 2) Por exemplo, (3**2) + (4**2) = 9 + 16 = 25 = 5**2

#39. Faga um programa que calcule a area de um tridngulo, cuja base e altura são fornecidas pelo usuério. Esse programa nao pode permitir a entrada de dados invalidos, ou seja, medidas menores ou iguais a 0. 

#40. Elabore um programa que faca leitura de varios nimeros inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor namero lido. 

#41. Faça um programa que calcula a associacao em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuario entre com um valor para resisténcia igual a zero. R = (R1 * R2) / (R1 + R2)

#42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero. 

#43. Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0), e calcule a idade média desse grupo. 

#44. Leia um número positivo do usuário, entao, calcule e imprima a sequência Fibonacci até o primeiro namero superior ao numero lido. Exemplo: se o usuário informou o número 30, a sequéncia a ser impressasera0 1123581321 34. 

#45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa. Vocé deve criar um menu com as duas opções de conversdo e com uma opção para finalizar o programa. O usuário podera fazer quantas conversoes desejar, sendo que o programa só sera finalizado quando a opção de finalizar for escolhida. 

#46. Faça um programa que gera um número aleatério de 1 a 1000. O usuário deve tentar acertar qual o nimero foi gerado, a cada tentativa o programa devera informar se o chute é menor ou maior que o nimero gerado. O programa acaba quando o usuario acerta o numero gerado. O programa deve informar em quantas tentativas o numero foi descoberto.
 
#47. Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números: 
#   adição (opção 1) 
#   subtração (opção 2) 
#   multiplicação (opção 3) 
#   divisão (opção 4)
#   saída (opção 5) 
#O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5). 

#48. Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores não ultrapassem quatro milhões. 

#49. O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.


#50. Chico tem 1.50 metro e cresce 2 centimetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centimetros por ano. Escreva um programa que calcule e imprima quantos anos serdo necessarios para que Zé seja maior que Chico. 

#51. Um funcionario recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faga programa que determine o salario atual do funcionario. 

#52. Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serao necessarias para atender ao saque com a menor quantidade de notas possivel. Serao utilizadas notas de 100, 50, 20, 10,5,2e 1real 

#53. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de Floyd. Para n = 6, temos: 
#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15 
#16 17 18 19 20 21 

#54. Faça um programa que receba um número inteiro maior do que 1, e verifique se o nimero fornecido é primo ou nao.

#55. Escreva um programa que leia um inteiro nao negativo n e imprima a soma dos n primeiros nimeros primos. 

#56. Faca um programa que calcule a soma de todos os nimeros primos abaixo de dois milhões. 

#57. Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo usuário. 

#58. Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário. 

#59. Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para cada habitante entre com os seguintes dados: consumo do mês e o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial). No final imprima o maior, o menor e a média do consumo dos habitantes; e por fim o total do consumo de cada categoria de consumidor. 

#60. Faça um programa que leia vários números, calcule e mostre: 
#(a) A soma dos números digitados 
#(b) A quantidade de números digitados 
#(c) A média dos números digitados 
#(d) O maior número digitado 
#(e) O menor número digitado 
#(f) A média dos números pares 
#Finalize a entrada de dados caso o usuario informe o valor 0.

#61. Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números de 3 dígitos. Ex: O maior palíndromo feito a partir do produto de dois números de dois digitos é 9009 = 91*99. 

#62. Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco, então há 2+4+4+6+5=22 letras usadas no total. Faça um programa que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 (mil) fossem escritos em palavras. OBS: Não conte espaços ou hifens.

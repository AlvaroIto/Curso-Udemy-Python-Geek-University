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


#21. Faça um programa que receba dois números. Calcule e mostre: 
#   a soma dos números pares desse intervalo de números, incluindo os números digitados; 
#   a multiplicação dos números impares desse intervalo, incluindo os digitados; 
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
lista_numeros = []
lista_par = []
lista_impar = []
if n1 == n2:
    print(f'Números são iguais: {n1} e {n2}')
elif n1 > n2:
    for n in range(n2, n1+1):
        lista_numeros.append(n)
else:
    for n in range(n1, n2+1):
        lista_numeros.append(n)

for n in lista_numeros:
    if n % 2 == 0:
        lista_par.append(n)

    else:
        lista_impar.append(n)
        mult = 1
        for num in lista_impar:
            mult *= num

print(f'Lista dos números no intervalo digitado: {lista_numeros}\n'
        f'Lista dos números pares: {lista_par}\n'
        f'Soma dos números pares: {sum(lista_par)}\n'
        f'Lista dos números ímpares: {lista_impar}\n'
        f'Multiplicação dos números pares: {(mult)}')
'''


#22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequéncia arbitraria de notas (validas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo nao será fornecido ao programa, o qual terminara quando for introduzido um valor que não seja valido como nota de aprovação. 
'''
nota = 10
lista_notas = []
while True:
    nota = int(input('Digite a nota: '))
    if nota < 10 or nota > 20:
        break
    else:
        lista_notas.append(nota)    

media  = sum(lista_notas) / (len(lista_notas))
print(f'Notas digitadas: {lista_notas}\n'
      f'Média aritmética: {media:.2f}')
'''


#23. Faca um algoritmo que leia um número positivo e imprima seus divisores. 
'''
num = int(input('Digite um número: '))
lista_numeros = []
lista_divisor = []
for n in range(1, num+1):
        if num % n == 0:
            lista_divisor.append(n)

print(f'Divisores de {n}: {lista_divisor}')
'''


#24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com excecao dele proprio. Ex: a soma dos divisores do número 66 é 1+2+3+6+11+22+33=78 
'''
num = int(input('Digite um número: '))
lista_numeros = []
lista_divisor = []
for n in range(1, num+1):
        if num % n == 0:
            if num == n:
                  break
            else:
                  lista_divisor.append(n)

print(f'Divisores de {n}: {lista_divisor}. Soma dos divisores: {sum(lista_divisor)}')
'''


#25. Faga um programa que some todos os números naturais abaixo de 1000 que sao múltiplos de 3 ou 5. 
'''
lista = []

for n in range(1000):
    if n % 3 == 0:
        lista.append(n)
    elif n % 5 == 0:
        lista.append(n)

print(f'Lista dos números múltiplos de 3 e 5: {lista}\n'
      f'Soma da lista acima: {sum(lista)}')
'''


#26. Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado. 
'''
num = int(input('Digite um número: '))
for n in range(1, num):
    if n % 11 == 0 or n % 13 == 0 or n % 17 == 0:
        print(n)
        break
'''

#27. Em Matematica, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica: H(n)=1+1/2+1/34+1/4+...4+1/n 
#Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H (n).
'''
num = int(input('Digite o valor: '))
for n in range(1, num+1):
    const = 1
    calc_const = 0
    calc_const += (const / n)

print(f'Resultado do número harmônico de {num} = {1 + calc_const}')
'''

#28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E, conforme a fórmula a seguir E=1+1/1!+1/2!+1/3!+..+1/N! 
'''
num = int(input('Digite um número: '))
cont = 1
fat = 1
calc_const = 0
while cont <= num:
    fat *= cont
    cont += 1
    calc_const += (1 / fat)
res = print(f'Valor de E do número {num} é: {1 + calc_const:.2f}')
'''

#29. Escreva um programa para calcular o valor da série, para 5 termos. S=0+1/2!+2/4!+3/6!+...
'''
for n in range(1, 6):
    fat = 1
    cont = 1
    calc = 0
    while cont <= 6:
        fat *= n
        cont += 1
        calc += 1/fat

print(f'{calc:.2f}')
'''

#31. Faça um programa que calcule e escreva o valor de S. S = (1/1) + (3/2) + (5/3) + (7/4) + ... + (99/50)
'''
num = []
for n in range(1, 100):
    if n % 2 != 0:
        num.append(n)

div = []
for n in range(1, 51):
    div.append(n)

for n in range(50):
    soma = sum({num[n] / div[n]})
    print(f'{num[n]} / {div[n]}')

print(f'= {soma}')
'''

#32. Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado e a relação entre eles (>,<,=) de cada lançamento. 
'''
from random import choice
from time import sleep
dado1 = range(1, 7)
dado2 = range(1, 7)
vezes = int(input('Serão quantas rodadas?: '))

for n in range(1, vezes+1):
    res1 = choice(dado1)
    res2 = choice(dado2)
    sleep(1)
    print('Jogando dados:')
    sleep(0.5)
    print(f'Dado 1: {res1}')
    sleep(1)
    print(f'Dado 2: {res2}')
    sleep(1)
    if res1 > res2:
        print(f'{res1} > {res2}')
    elif res1 < res2:
        print(f'{res1} < {res2}')
    else:
        print(f'{res1} = {res2}')
'''


#33. Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. Exemplo: Para n=6, i=2 e j=3 a saída deverá ser: 0,2,3,4,6,8.
'''
num = int(input('Digite o valor de n: ')) 
i = int(input('Digite o valor de i: '))
j = int(input('Digite o valor de j: '))
mult = []

for n in range(num):
    if len(mult) < num:
        mult_i = n * i
        if mult_i not in mult:    
            mult.append(mult_i)
            if len(mult) < num:
                mult_j = n * j
                if mult_j not in mult:
                    mult.append(mult_j)

print(f'{num} primeiros multiplos de {i} ou {j}: {sorted(mult)}')
'''

#34. Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20? Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto. 

#35. Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números impares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela, “Intervalo de valores invalido” e o programa termina. Exemplo de tela de saída: Digite o valor inicial e valor final: 5 10 
#Soma dos impares neste intervalo: 21 
'''
vi = int(input('Digite o valor inicial: '))
vf = int(input('Digite o valor final: '))
soma = 0

for n in range(vi, vf):
    if vi > vf:
        print(f'Valor inicial ({vi}) não pode ser maior que valor final ({vf})')
    else:
        if n % 2 != 0:
            soma += n

print(f'Valor inicial: {vi}')
print(f'Valor final: {vf}')
print(f'Soma dos valores ímpares no intervalo: {soma}')
'''


#36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números naturais é, (1**2) + (2**2) + ... + (10 ** 2) = 385 O quadrado da soma dos dez primeiros números naturais é, (1+2+..+10)**2 = 552 = 3025 
#A diferenca entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025-385 = 2640.
'''
soma_quadrado_100 = 0
quadrado_soma_100 = 0
diferenca = 0

for n in range(1, 101):
    soma_quadrado_100 += n ** 2

for n in range(1, 101):
    quadrado_soma_100 += n
quadrado_soma_100 = quadrado_soma_100 * quadrado_soma_100

diferenca =  quadrado_soma_100 - soma_quadrado_100
print(diferenca)
'''


#37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte: a soma dos dois digitos de mais baixa ordem com os dois digitos de mais alta ordem elevada ao quadrado é igual ao próprio numero. Por exemplo, para o inteiro 3025, temos que: 30 + 25 = 55 55 ** 2 = 3025 
'''
lista = []
for n in range(1000, 10000):    
    alta = n // 100
    baixa = n % 100
    soma_ao_quadrado = (baixa + alta) * (baixa + alta)

    if soma_ao_quadrado == n:
        lista.append(soma_ao_quadrado)

print(lista)   
'''

#38. Faça um programa que calcule o terno pitagorico a, b, c, para o qual a+ b+ c = 1000. Um terno pitagdrico é um conjunto de trés nimeros naturais, a, b, c, para a qual, (a ** 2) + (b ** 2) + (c ** 2) Por exemplo, (3**2) + (4**2) = 9 + 16 = 25 = 5**2
'''
from math import sqrt
valor_a = int(input('Digite o valor de a: '))
valor_b = int(input('Digite o valor de b: '))
soma_a_b = (valor_a ** 2) + (valor_b ** 2)
valor_c = sqrt(soma_a_b)

print(f'({valor_a} ** 2) + ({valor_b} ** 2) = {soma_a_b} = {valor_c:.0f} ** 2 ')
'''


#39. Faga um programa que calcule a area de um triângulo, cuja base e altura são fornecidas pelo usuário. Esse programa nao pode permitir a entrada de dados invalidos, ou seja, medidas menores ou iguais a 0.
'''
base = 0
altura = 0
while True:
    base = float(input('Digite o valor da base do triângulo: '))
    altura = float(input('Digite o valor da altura do triângulo: '))
    if base <= 0:
        print(f'Base: {base} não pode ser menor ou igual a 0\n')
    elif altura <= 0:
        print(f'altura: {altura} não pode ser menor ou igual a 0\n')
    else:
        break

area = (base * altura) / 2
print(f'A área do triângulo de base: {base} e altura: {altura} é: {area:.2f}')
'''
    
#40. Elabore um programa que faça leitura de varios números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido. 
'''
numeros = []
while True:
    num = int(input('Digite um número positivo ou um número negativo para sair: '))
    if num < 0:
        break
    else:
        numeros.append(num)

print(f'Números digitados: {numeros}\n'
      f'Maior número digitado: {max(numeros)}')
'''

#41. Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuario entre com um valor para resisténcia igual a zero. R = (R1 * R2) / (R1 + R2)
'''
while True:
    r1 = float(input('Digite o valor do resistor R1: '))
    r2 = float(input('Digite o valor do resistor R2: '))
    if r1 == 0:
        print(f'Resistor 1 = {r1} ')
        print('Fim')
        break

    elif r2 == 0:
        print(f'Resistor 2 = {r2} ')
        print('Fim')
        break
        
    else:
        res = (r1 * r2) / (r1 + r2)
        print(f'{res:.2f}')
'''

#42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero. 
'''
from math import sqrt
while True:
    num = int(input('Digite um valor diferente de 0: '))
    if num <= 0:
        print('Fim')
        break
    else:
        print(f'Quadrado de {num} = {num ** 2}\n'
              f'Cubo de {num} = {num ** 3}\n'
              f'Raiz quadrada de {num} = {sqrt(num):.2f}')
'''

#43. Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0), e calcule a idade média desse grupo. 
'''
idade = []
while True:
    num = int(input('Digite uma idade válida ou 0 para sair: '))
    if num <= 0:
        break
    else:
        idade.append(num)

print(f'Idades digitadas: {idade}\n'
      f'Média das idades digitadas: {sum(idade) / len(idade):.2f}')
'''

#44. Leia um número positivo do usuário, entao, calcule e imprima a sequência Fibonacci até o primeiro namero superior ao numero lido. Exemplo: se o usuário informou o número 30, a sequéncia a ser impressão sera 0 1 1 2 3 5 8 13 21 34. 
'''
num = int(input('Digite um número positivo: '))
n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end='')
cont = 3
while cont <= num:
    n3 = n1 + n2
    print(f' -> {n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1
'''

#45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa. Vocé deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa. O usuário podera fazer quantas conversoes desejar, sendo que o programa só sera finalizado quando a opção de finalizar for escolhida. 
'''
while True:    
    vel = float(input('Digite uma velocidade: '))
    print('Digite uma das opções abaixo: \n'
        '1- Converter a velocidade para km/h\n'
        '2- Converter a velocidade para m/s\n'
        '3- Sair do programa')
    op = int(input())
    if op == 1:
        km = vel * 3.6
        print(f'Velocidade em m/s: {vel}\n'
            f'Velocidade convertida para Km/h: {km:.2f}\n')
    elif op == 2:
        ms = vel / 3.6
        print(f'Velocidade em km/h: {vel}\n'
            f'Velocidade convertida para Km/h: {ms:.2f}\n')
    else:
        print('Fim do programa')
        break
'''

#46. Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número foi gerado, a cada tentativa o programa devera informar se o chute é menor ou maior que o número gerado. O programa acaba quando o usuario acerta o numero gerado. O programa deve informar em quantas tentativas o numero foi descoberto.
'''
from random import randint
num_gerado = randint(1, 1000)
#print(num_gerado)
chute = 0
while True:
    print('Tente adivinhar o número gerado de 1 a 1000!')
    palpite = int(input('Digite o número: '))
    if palpite == num_gerado:
        chute += 1
        print(f'Ganhou! Número de tentativas: {chute}')
        break
    elif palpite > num_gerado:
        print(f'Palpite ({palpite}) é MAIOR que numero gerado. Tente novamente')
        chute += 1
    else:
        print(f'Papite ({palpite}) é MENOR que número gerado')
        chute += 1
'''

#47. Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números: 
#   adição (opção 1) 
#   subtração (opção 2) 
#   multiplicação (opção 3) 
#   divisão (opção 4)
#   saída (opção 5) 
#O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5). 
'''
while True:   
    print('Digite um número das opções abaixo: \n'
        '1- Adição\n'
        '2- Subtração\n'
        '3- Multiplicação\n'
        '4- Divistão\n'
        '5- Sair')
    op = int(input())

    if str(op) not in '1234':
        print('FIM')
        break

    n1 =int(input('Digite o primeiro número: '))
    n2 =int(input('Digite o segundo número: '))
    
    if op == 1:
        print(f'{n1} + {n2} = {n1 + n2}\n')
    elif op == 2:
        print(f'{n1} - {n2} = {n1 - n2}\n')
    elif op == 3:
        print(f'{n1} * {n2} = {n1 * n2}\n')
    elif op == 4:
        if n2 == 0:
            print(f'ERRO! Divisão por 0!\n')
        else:
            print(f'{n1} / {n2} = {n1 / n2:.2f}\n')
'''

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

#1. Crie uma função que recebe como parametro um nimero inteiro e devolve o seu dobro. 
'''
def dobro(n):
    return n ** 2

num = int(input('Digite um número: '))
print(f'Número digitaddo: {num}\n'
      f'Dobro do número: {dobro(num)}')
'''

#2. Faca uma funcao que receba a data atual (dia, més e ano em inteiro) e exiba-a na tela no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000. 
'''
def extenso(mes):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return meses[mes-1]

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
print(f'{dia} de {extenso(mes)} de {ano}')
'''

#3. Faça uma função para verificar se um nimero é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0. 
'''
def verifica_num():
    num = int(input('Digite um número: '))
    if num > 0:
        return(f'Número: {num} é positivo')
    else:
        return(f'Número: {num} é negativo')


verifica_num()
'''

#4. Faça uma funcao para verificar se um número é um quadrado perfeito. Um quadrado perfeito é um número inteiro nao negativo que pode ser expresso como o quadrado de outro nimero inteiro. Ex: 1, 4, 9... 
'''
def quadrado():
    num = int(input('Digite um número: '))
    raiz_q = int(num ** (1/2))
    if (raiz_q ** 2) == num:
        print(f'O número {num} é um quadrado perfeito!')
    else:
        print(f'O número {num} não é um quadrado perfeito!')

quadrado()
'''

#5. Faga uma função e um programa de teste para o calculo do volume de uma esfera. Sendo que o raio é passado por parametro. V = (4 / 3) * 3.14 * (R ** 3) 
'''
def volume_esfera():
    raio = float(input('Digite o valor do raio: '))
    v = (4 * 3.14 * (raio ** 3)) / 3
    print(f'O volume de uma esfera de raio {raio} é: {v:.2f}')

volume_esfera()
'''

#6. Faca uma funcao que receba 3 nimeros inteiros como parametro, representando horas, minutos e segundos, e os converta em segundos. 
'''
def conversor_tempo_segundo(hora, min, seg):
    hora_seg = hora * 3600
    min_seg = min * 60
    tempo_tot = hora_seg + min_seg + seg
    print(f'Tempo digitado: {hora}:{min}:{seg}\n'
          f'Tempo total em segundos: {tempo_tot}')

hora = int(input('Digite as hora: '))
min = int(input('Digite os minutos: '))
seg = int(input('Digite os segundos: '))
conversor_tempo_segundo(hora, min, seg)
'''
#7. Faga uma fungao que receba uma temperatura em graus Celsius e retorne-a convertida em graus Fahrenheit. A férmula de conversao é: F = C = (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. 
'''
def conversor_c_f():
    temp_c = float(input('Digite a temperatura em graus Celsius: '))
    temp_f = temp_c * ( 9 / 5) + 32
    print(f'A temperatura {temp_c} graus Celsius convertida para Fahrenheit é: {temp_f:.2f}')

conversor_c_f()
'''

#8. Sejam a e b os catetos de um tridngulo, onde a hipotenusa é obtida pela equacao: hipotenusa = raiz quadrada((a ** 2) + (b ** 2)). Faga uma função que receba os valores de a e b e calcule o valor da hipotenusa através da equação. 
'''
from math import sqrt
def hipotenusa(a, b):
    calc = sqrt((a ** 2) + (b ** 2))
    print(f'Dados os catetos: A {a} e B {b}, o valor da hipotenusa é:{calc:.2f}')

a = float(input('Digite o valor do cateto A: '))
b = float(input('Digite o valor do cateto B: '))
hipotenusa(a, b)
'''

#9. Faça uma funcao que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro. O volume de um cilindro circular é calculado por meio da seguinte formula: V = 3.14 * (raio ** 2) * altura.
'''
def vol_cilindro(alt, raio):
    calc = 3.14 * (raio  ** 2) * alt
    print(f'O cilindro com altura {alt} e raio {raio} tem o volume de: {calc:.2f}')

alt = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))
vol_cilindro(alt, raio)
'''

#10. Faça uma função que receba dois nimeros e retorne qual deles é o maior
'''
def maior_menor(n1, n2):
    if n1 < n2:
        return f'{n1} é menor que {n2}'
    elif n2 < n1:
        return f'{n1} é maior que {n2}'
    else:
        return f'{n1} e {n2} tem o mesmo valor'

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segunddo número: '))
print(maior_menor(n1, n2))
'''

#11. Elabore uma função que receba trés notas de um aluno como parametros e uma letra. Se a letra for A, a função devera calcular a média aritmética das notas do aluno; se for P, devera calcular a média ponderada, com pesos 5, 3 e 2. 
'''
def media():
    if op == 'A':
        print('Media Aritmética:')
        media = sum(notas) / 3
        print(f'({notas[0]} + {notas[1]} + {notas[2]}) / 3 = {media:.2f}')
    elif op == 'P':
        print('Média Ponderada:')
        for n in range(0, 3):
            peso = [5, 3, 2]
            n = notas[n] * peso[n]
            notas_peso.append(n)
        media = sum(notas_peso) / sum(peso)
        print(f'({notas[0]} * {peso[0]}) + ({notas[1]} * {peso[1]}) + ({notas[2]} * {peso[2]}) / ({notas[0]} + {notas[1]} + {notas[2]}) = {media:.2f}')



notas = []
notas_peso = []
for n in range(1, 4):
    notas.append(int(input(f'Digite a {n}ª nota: ')))
print('Digite a opção desejada: \n'
      'A: Média aritmética\n'
      'P: Méddia Ponderada')
op = input().upper()

media()
'''

#12. Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos. Por exemplo, ao nimero 251 corresponderé o valor 8 (2 + 5+ 1). Se o número lido não for maior do que zero, o programa terminara com a mensagem “Numero invalido". 

#13. Faca uma função que receba dois valores numéricos e um simbolo. Este simbolo representara a operagao que se deseja efetuar com os nimeros. Se o simbolo for + devera ser realizada uma adicao, se for — uma subtração, se for / uma divisao e se for = sera efetuada uma multiplicacao. 
#   CONSUMO         | (Km/) MENSAGEM 
#menor que 8           Venda o carro! 
#entre 8el4            Econémico! 
#maior que 12          Super econdmico!

#14. Faga uma fungao que receba a distancia em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km /I e escreva uma mensagem de acordo com a tabela abaixo: 

#15. Crie um programa que receba trés valores (obrigatoriamente maiores que zero), representando as medidas dos trés lados de um triangulo. Elabore funções para: 
#(a) Determinar se eles lados formam um triangulo, sabendo que: 
#     O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados. 
#(b) Determinar e mostrar o tipo de triangulo, caso as medidas formem um triangulo. Sendo que: 
#    Chama-se equilatero o triangulo que tem trés lados iguais. 
#    Denominam-se isésceles o tridngulo que tem o comprimento de dois lados iguais. 
#    Recebe o nome de escaleno o tridngulo que tem os trés lados diferentes. 

#16. Faca uma função chamada Desenhalinha. Ele deve desenhar uma linha na tela usando varios simbolos de igual (Ex: = ). A fungao recebe por parametro quantos sinais de igual serao mostrados. 

#17. Faça uma funcao que receba dois nimeros inteiros positivos por parametro e retorne a soma dos N números inteiros existentes entre eles

#18. Faca uma função que receba por parametro dois valores X e Z. Calcule e retorne o resultado de X7 para o programa principal. Atenção não utilize nenhuma função pronta de exponenciacao. 

#19. Faga uma função que retorne o maior fator primo de um número. 

#20. Faça um algoritmo que receba um numero inteiro positivo n e calcule o seu fatorial, n!. 

#21. Escreva uma fungao para determinar a quantidade de nimeros primos abaixo N. 

#22. Crie uma funcao que receba como parametro um valor inteiro e gere como saida n linhas com pontos de exclamagao, conforme o exemplo abaixo (para n = 5): 
#!
#!!
#!!!
#!!!!
#!!!!!


#23. Escreva uma fungao que gera um tridngulo lateral de altura 2*n-1 e n largura. Por exemplo, a saida para n = 4 seria:
#*
#**
#***
#****
#***
#**
#*

#24. Escreva uma função que gera um triangulo de altura e lados n e base 2*n-1. Por exemplo, a saida para n = 6 seria: 

#25. Faga uma função que receba um inteiro N como parametro, calcule e retorne o resultado da seguinte série: 
#S = 2 / 4 + 5 / 5 + 10 / 6 + ... + ( (N  ** 2) + 1) / (N + 3) 

#26. Faça um algoritmo que receba um número inteiro positivo n e calcule o somatério de 1 até n. 

#32. Faca uma função chamada ‘simplifica’ que recebe como parametro o numerador e o denominador de uma fragdo. Esta função deve simplificar a fragao recebida dividindo o numerador e o denominador pelo maior fator possivel. Por exemplo, a fragao 36/60 simplifica para 3/5 dividindo o numerador e o denominador por 12. A função deve modificar as variaveis passadas como parametro. 

#33. Faça uma fungao que receba um nimero N e retorne a soma dos algarismos de N!. Ex: se N = 4, N! = 24. Logo, a soma de seus algarismos é 2 + 4 =6. 

#34. Faca uma funcao nao-recursiva que receba um nimero inteiro positivo impar N e retorne o fatorial duplo desse numero. O fatorial duplo é definido como o produto de todos os números naturais impares de 1 até algum número natural impar N. Assim, o fatorial duplo de 5 é: 5!! = 1 * 3 * 5 = 15 

#35. Faga uma fungao nao-recursiva que receba um número inteiro positivo n e retorne o fatorial quadruplo desse namero. O fatorial quadruplo de um número n é dado por: (2n)! / n!

#36. Faça uma fungao nao-recursiva que receba um número inteiro positivo N e retorne o superfatorial desse nimero. O superfatorial de um número N é definida pelo produto dos N primeiros fatoriais de N. Assim, o superfatorial de 4 é sf(4) = 11 * 21 * 3! * 4! = 288. 

#37. Faça uma fungao nao-recursiva que receba um número inteiro positivo n e retorne o hiperfatorial desse nimero. O hiperfatorial de um número n, escrito H (n), é definido por: 
# H(n) =[[io KF=11.22.3%. .. (n=1)"'.n" 

#38. Faça uma fungao nao-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número. Um fatorial exponencial é um inteiro positivo n elevado a poténcia de n — 1, que por sua vez é elevado a poténcia de n — 2 e assim em diante. Ou seja: 
#n (n=2)"" 1) 

#39. Faça uma função ‘Troque’, que recebe duas variaveis reais A e B e troca o valor delas (i.e., A recebe o valor de B e B recebe o valor de A). 

#40. Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele possui

#41. Faça uma fungao que receba um vetor de inteiros e retorne o maior valor. 

#42. Faça uma funcao que receba um vetor de reais e retorne a média dele. 

#43. Faga uma função que receba um vetor de inteiros e o preencha com nimeros aleatorios sem repeticao. 

#44. Faça uma função que receba como parametro um vetor X de 30 elementos inteiros e retorne, também por parametro, dois vetores A e B. O vetor A deve conter os elementos pares de X e o vetor B, os elementos impares. 

#45. Faça uma função que calcule o desvio padrao de um vetor v contendo n nimeros 
#Desvio Padrdo: |/ a Y, (vli] - m)? 
#onde m é a media do vetor. 

#46. Crie um programa contendo as seguintes funções que recebem um vetor V números reais como parametro: 
#    Impressão normal do vetor. 
#    Impressao inversa. 
#    Função que retorna a média aritmética dos elementos do vetor. 

#47. Faça uma função que receba uma matriz 4 x 4 e retorne quantos valores maiores do que 10 ela possui.


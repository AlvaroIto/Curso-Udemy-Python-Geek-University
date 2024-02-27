#1. Faga um programa que receba dois números e mostre qual deles é o maior. 
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 == n2:
    print(f'{n1} e {n2} são iguais')
else:
    print(f'{n2} é maior que {n1}')
'''

#2. Leia um numero fornecido pelo usuário. Se esse número for positivo, calcule a raiz  quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é invalido. 
'''
from math import sqrt
num = int(input('Digite um número: '))
if num > 0:
    print(f'A raiz quadrada de {num} é {sqrt(num):.2f}')
else:
    print(f'Número inválido!')
'''

#3. Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrario, imprima o numero ao quadrado. 
'''
from math import sqrt
num = int(input('Digite um número: '))
if num > 0:
    print(f'A raiz quadrada de {num} é {sqrt(num):.2f}')
else:
    print(f'O quadrado de {num} é {num ** 2}')
'''

#4. Faga um programa que leia um número e, caso ele seja positivo, calcule e mostre: 
# O número digitado ao quadrado 
# A raiz quadrada do número digitado 
'''
from math import sqrt
num = int(input('Digite um número: '))
if num > 0:
    print(f'A raiz quadrada de {num} é {sqrt(num):.2f}')
    print(f'O quadrado de {num} é {num ** 2}')
else:
    print(f'Número inválido!')
'''

#5. Faça um programa que receba um número inteiro e verifique se este nimero é par ou impar. 
'''
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é ímpar')
'''

#6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferenca existente entre ambos. 
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
    print(f'{n1} - {n2} = {n1 - n2}')
elif n1 == n2:
    print(f'{n1} e {n2} são iguais')
    print(f'{n1} - {n2} = {n1 - n2}')
else:
    print(f'{n2} é maior que {n1}')
    print(f'{n2} - {n1} = {n2 - n1}')
'''
#7. Faga um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem Números iguais. 
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 == n2:
    print(f'{n1} e {n2} são iguais')
else:
    print(f'{n2} é maior que {n1}')
'''

#8. Faga um programa que leia 2 notas de um aluno, verifique se as notas sao validas e exiba na tela a média destas notas. Uma nota valida deve ser,  obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota nao possua um valor valido, este fato deve ser informado ao usuario e o programa termina.
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
    print(f'Nota inválida')
else:
    print(f'Média: {(n1 + n2) / 2}')
'''

#9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salario imprima: Empréstimo não concedido, caso contrério imprima: Empréstimo concedido.
'''
salario = float(input('Digite o salário: R$'))
prestacao = float(input('Digite o valor da prestação: R$'))
limite = salario * 0.2
if prestacao > limite:
    print(f'Salário: R${salario}')
    print(f'Prestação solicitada: R${prestacao}')
    print(f'Limite  para prestação: R${limite}')
    print('Empréstimo não concedido, prestação acima de 20% do salário')
else:
    print(f'Salário: R${salario}')
    print(f'Prestação solicitada: R${prestacao}')
    print(f'Limite  para prestação: R${limite}')
    print('Empréstimo concedido!')
'''

#10. Faga um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde a altura):
#Homens: (72.7 * h) — 58 
#Mulheres: (62.1 * h) — 44.7
'''
h = float(input('Digite a altura em metros: '))
#verificar se sexo foi digitado corretamente
while True:
    s = str(input('Digite o sexo (M/F): ')).lower()
    if s not in 'MmFf':
        print('Sexo incorreto, tente novamente')
    else:
        break

if s == 'm':
    peso_ideal = (72.6 * h) - 58
else:
    peso_ideal = (62.1 * h) - 44.7

print(f'Sexo = {s}')
print(f'Altura = {h:.2f}mts')
print(f'Peso ideal = {peso_ideal:.2f}kg')
'''


#11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8(2+5+1). Se o número lido não for maior do que zero, o programa terminara com a mensagem “Número inválido”. 
'''
num = int(input('Digite um número maior que 0: '))
soma = 0
#verificar se número é maior que 0
if num <= 0:
    print(f'Número {num} inválido!')
else:
    #transformar numeros em lista para iterar
    lista_num = list(str(num))
    for n in lista_num:
        soma += (int(n))

print(f'A soma dos algarismos digitados ({num}) é: {soma}')
'''


#12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número invalido”. Se o número for positivo, calcular o logaritmo deste numero. 
'''
from math import log
num = int(input('Digite um número inteiro: '))
if num < 0:
    print(f'Número {num} inválido')
else:
    logaritmo = log(num)
    print(f'O logaritmo de {num} é: {logaritmo:.2f}')
'''


#13. Faga um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova tém peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovagao deve ser igual ou superior a 60 pontos. 
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = ((n1 + n2 + (n3 * 2)) / 4)

print(f'A média ponderada das notas {n1} + {n2} + {n3} = {media}')
'''


#14. A nota final de um estudante é calculada a partir de trés notas atribuidas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratério, a uma avalição semestral e a um exame final. A média das trés notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratério: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno esta reprovado (média entre 0 e 2,9), de recuperacao (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificagoes necessarias. 
'''
lab = float(input('Digite a primeira nota: '))
ava = float(input('Digite a segunda nota: '))
exa = float(input('Digite a terceira nota: '))
peso_lab = 2
peso_ava = 3
peso_exa = 5

media = (lab * peso_lab + ava * peso_ava + exa * peso_exa) / (peso_lab + peso_ava + peso_exa)

if media <= 2.9:
    print(f'Média:{media}. Reprovado!')
elif media >= 3 and media <= 4.9:
    print(f'Média:{media}. Recuperação!')
else:
    print(f'Média:{media}. Aprovado')
'''


#15. Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este numero. Isto é, domingo se 1, segunda -feira se 2, e assim por diante. 
'''
num = int(input('Digite um número de 1 a 7: '))
if num not in range(1,8,1):
    print(f'Número {num} precisa estar entre 1 e 7')
else:
    if num == 1:
        print('Domingo')
    elif num == 2:
        print('Segunda-feira')
    elif num == 3:
        print('Terça-feira')
    elif num == 4:
        print('Quarta-feira')
    elif num == 5:
        print('Quinta-feira')
    elif num == 6:
        print('Sexta-feira')
    else:
        print('Sábado')
'''


#16. Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante. 
'''
num = int(input('Digite um número de 1 a 12: '))
if num not in range(1,12,1):
    print(f'Número {num} precisa estar entre 1 e 12')
else:
    if num == 1:
        print('Janeiro')
    elif num == 2:
        print('Fevereiro')
    elif num == 3:
        print('Março')
    elif num == 4:
        print('Abril')
    elif num == 5:
        print('Maio')
    elif num == 6:
        print('Junho')
    elif num == 7:
        print('Julho')
    elif num == 8:
        print('Agosto')
    elif num == 9:
        print('Setembro')
    elif num == 10:
        print('Outubro')
    elif num == 11:
        print('Novembro')
    else:
        print('Dezembro')
'''

#17. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: 
#A = (basemaior + basemenor) * altura / 2
#Lembre-se a base maior e a base menor devem ser números maiores que zero.
'''
base_menor = float(input('Digite o valor da base menor: '))
base_maior = float(input('Digite o valor da base maior: '))
altura = float(input('Digite a altura do trapézio: '))
area = ((base_maior + base_menor) * altura) / 2
if base_maior <= 0  or base_menor <= 0:
    print('Bases devem ser maior que 0')
else:
    print(f'área do trapézio é: {area}')

'''


#18. Faga um programa que mostre ao usuario um menu com 4 opgoes de operagoes matematicas (as basicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo. 
'''
print(
    'OPERAÇÕES MATEMÁTICAS:\n'
    'SOMA: +\n'
    'SUBRATRAÇÃO: -\n'
    'MULTIPLICAÇÃO: *\n'
    'DIVISÃO: /\n'
    'ESCOLHA UMA OPÇÃO:'
)
op = input()
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if op == '+':
    print(f'{n1} {op} {n2} = {n1 + n2}')
elif op == '-':
    print(f'{n1} {op} {n2} = {n1 - n2}')
elif op == '*':
    print(f'{n1} {op} {n2} = {n1 * n2}')
else:
    print(f'{n1} {op} {n2} = {n1 / n2:.2f}')
'''

#19. Faga um programa para verificar se um determinado número inteiro e divisivel por 3 ou 5, mas nao simultaneamente pelos dois. 
'''
num = int(input('digite um número: '))
div3 = num % 3 == 0
div5 = num % 5 == 0

if div3 and div5:
    print(f'ERRO! {num} é divisível por 3 e 5 simultaneamente')
else:
    if div3:
        print(f'{num} é divisível por 3')
    elif div5:
        print(f'{num} é divisível por 5')
'''


#20. Dados trés valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um tridngulo escaleno, equilatero ou iséscele, considerando os seguintes conceitos: 
# O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados. 
# Chama-se equilatero o triangulo que tem trés lados iguais. 
# Denominam-se isosceles o triangulo que tem o comprimento de dois lados iguais. 
# Recebe o nome de escaleno o tridngulo que tem os trés lados diferentes. 
'''
lado_a = int(input('Digite o primeiro lado do triângulo: '))
lado_b = int(input('Digite o segundo lado do triângulo: '))
lado_c = int(input('Digite o terceiro lado do triângulo: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print(f'Os lados {lado_a} {lado_b} e {lado_c} podem formar um triângulo')
else:
    print(f'Os lados {lado_a} {lado_b} e {lado_c} NÃO podem formar um triângulo')
'''
     

#21. Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for invalida. 
    #Escolha a opção: 
    #1- Soma de 2 números. 
    #2- Diferença entre 2 números (maior pelo menor). 
    #3- Produto entre 2 números. 
    #4- Divisão entre 2 números (o denominador não pode ser zero). 
    #Opção
'''
print('ESCOLHA UMA OPÇÃO:\n'
      '1- Soma de 2 números\n'
      '2- Diferença entre 2 números (maior pelo menor)\n'
      '3- Produto entre 2 números\n'
      '4- Divisão entre 2 números (o denomindador não pode ser 0)'
      )
op = input('Opção: ')

if op not in '1234':
    print('Opção inválida!')
else:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    if op == '1':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif op == '2':
        if num2 < num1:
            print(f'{num1} - {num2} = {num1 - num2}')
        elif num1 < num2:
            print(f'{num2} - {num1} = {num2 - num1}')
    elif op == '3':
        print(f'{num1} * {num2} = {num1 * num2}')
    else:
        if num2 == 0:
            print(f'Erro! O denominador não pode ser zero')
        else:
            print(f'{num1} / {num2} = {num1 / num2:.2f}')
'''


#22. Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são 
# Ter pelo menos 65 anos, 
# Ou ter trabalhado pelo menos 30 anos, 
# Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
'''
idade = int(input('Digite a idade: '))
tempo_servico = int(input('Digite o tempo de serviço em anos: '))

if idade > 60 and tempo_servico > 25:
    print(f'idade: {idade}')
    print(f'tempo de serviço: {tempo_servico}')
    print('Pode se aposentar')
elif idade >= 60:
    print(f'idade: {idade}')
    print('Pode se aposentar')
elif tempo_servico >= 30:
    print(f'tempo de serviço: {tempo_servico}')
    print('Pode se aposentar')
else:
    print('NÃO pode se aposentar')
'''


#23. Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisivel por 400 ou se for divisivel por 4 e nao for divisivel por 100. Por exemplo: 1988, 1992, 1996 
'''
ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'Ano: {ano} é bissexto')
else:
    print(f'Ano: {ano} NÃO é bissexto')
'''


#24. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faga um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preco final do produto acrescido do imposto do estado em que ele sera vendido. Se o estado digitado nao for valido, mostrar uma mensagem de erro. 
'''
valor_produto = float(input('Digite o valor do produto: R$'))
estado = str(input('Digite a sigla do estado(MG/MS/RJ/SP): ').upper())

if estado not in 'MGMSRJSP':
    print(f'Estado {estado} inválido')
else:
    if estado == 'MG':
        valor_produto = valor_produto + (valor_produto * 0.07)
    elif estado == 'MS':
        valor_produto = valor_produto + (valor_produto * 0.08)
    elif estado == 'RJ':
        valor_produto = valor_produto + (valor_produto * 0.15)
    else:
        valor_produto = valor_produto + (valor_produto * 0.12)

print(f'Valor do produto: R${valor_produto}')
print(f'Estado destino: R${estado}')
print(f'Valor do produto com imposto: R${valor_produto}')
'''


#25. Calcule as raizes da equação de 2° grau. 
#Lembrando que: 
#x = -b +- raiz de delta / 2*a
#Onde 
#Delta = b² - 4ac 
#E ax² + bx + c = 0 representa uma equação de 2° grau. 
#A variavel a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Nao é equacao de segundo grau”. 
# Se Delta = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única. 
# Se Delta < 0, nao existe real. Imprima a mensagem Não existe raiz. 
# Se Delta > 0, imprima as duas raizes reais.
'''
from math import sqrt
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = (b ** 2) - (( 4 * a) * c)
x1 = (-(b) + sqrt(delta)) / (2 * a)
x2 = (-(b) - sqrt(delta)) / (2 * a)

if a == 0:
    print(f'ERRO! Valor de {a} precisa ser difente de Zero. Não é equação de segundo grau!')
if delta < 0:
    print(f'ERRO! Valor de {delta} menor que Zero. Não existe raiz')
elif delta == 0:
    print(f'Raiz única {delta}')
else:
    print(f'Valor de a: {a}')
    print(f'Valor de b: {b}')
    print(f'Valor de c: {c}')
    print(f'Valor de delta: {delta}')
    print(f'Valor da raiz x1: {x1}')
    print(f'Valor da raiz x2: {x2}')
'''
#26. Leia a distancia em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km /I e escreva uma mensagem de acordo com a tabela abaixo: 
    #CONSUMO | (Km/) MENSAGEM 
    #menor que 8 Venda o carro! 
    #entre 8 e l4 Econômico! 
    #maior que 12 Super econômico! 
'''
distancia = float(input('Digite a distância em quilômetros: '))
consumo = float(input('Digite a quantidade de litros de gasolina consumido no percurso: '))
consumo_por_litro = distancia / consumo
if consumo_por_litro < 8:
    print(f'Consumo por litro: {consumo_por_litro} km/l. Venda o carro!')
elif consumo_por_litro >= 8 and consumo_por_litro <= 14:
    print(f'Consumo por litro: {consumo_por_litro} km/l. Econômico!')
else:
    print(f'Consumo por litro por litro: {consumo_por_litro} km/l. Super Econômico!')
'''

#27. Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias: 
    #Categoria  | Idade 
    #Infantil A | 5 a 7 
    #Infantil B | 8 a 10 
    #Juvenil A  | 11 a 13 
    #Juvenil B  | 14 a 17 
    #Sênior maiores de 18 anos 
'''
idade = int(input('Digite a idade: '))

if idade >= 5 and idade <= 7:
    print(f'Idade: {idade}. Categoria: Infantil A')
elif idade >= 8 and idade <= 10:
    print(f'Idade: {idade}. Categoria: Infantil B')
elif idade >= 11 and idade <= 13:
    print(f'Idade: {idade}. Categoria: Juvenil A')
elif idade >= 14 and idade <= 17:
    print(f'Idade: {idade}. Categoria: Juvenil B')
elif idade >= 18:
    print(f'Idade: {idade}. Sênior')
else:
    print(f'Idade: {idade} precisa ser maior que 4 anos')
'''

#28. Faça um programa que leia trés números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário: 
#(a) Geométrica: raiz cubica de x * y * z 
#(b) Ponderada: (x + 2*y+3*z) / 6
#(c) Harmônica: 1((1/x + 1/y + 1/z))
#(d) Aritmética: (x+y+z) / 3
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

print('Digite um número para obter a média relacionada:\n'
      '1- Geométrica\n'
      '2- Ponderada\n'
      '3- Harmônica\n'
      '4- Aritmética')
op = input()

if op not in '1234':
    print(f'Opção {op} inválida!')
else:
    if op == '1':
        media = (n1 * n2 * n3) ** (1/3)
        print(f'Média Geométrica dos valores: {n1}, {n2} e {n3} = {media:.2f}')
        
    elif op == '2':
        media = (n1 + (2 * n2) + (3 * n3)) / 6
        print(f'Média Ponderada dos valores: {n1}, {n2} e {n3} = {media:.2f}')
    
    elif op == '3':
        media = 1 / ((1 / n1) + (1 / n2) + (1 / n3))
        print(f'Média Harmônica dos valores: {n1}, {n2} e {n3} = {media:.2f}')
    else:
        media = (n1 + n2 + n3) / 3
        print(f'Média Aritmética dos valores: {n1}, {n2} e {n3} = {media:.2f}')

'''
#29. Faça uma prova de matematica para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolha números aleatérios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são os números aleatérios. Peça a resposta. Faca cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou. 
'''
from random import randint

cont_perguntas = 1
respostas = []
acertos = 0
respostas_certas = []

while cont_perguntas <= 5: 
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    print(f'Pergunta {cont_perguntas}:')
    print(f'Qual o resultado da soma: {n1} + {n2}?')
    resposta = int(input())
    respostas.append(resposta)
    cont_perguntas += 1
    if resposta == (n1 + n2):
        acertos += 1
        respostas_certas.append(resposta)
        print('Resposta correta!')
    else:
        print('Resposta errada!')
        print(f'Resposta correta: {n1 + n2}')
print(f'Das 5 perguntas você acertou {acertos}')
'''

#30. Faga um programa que receba trés números e mostre-os em ordem crescente. 
'''
lista_num = []
while len(lista_num) < 3:
    num = int(input('Digite um número: '))
    lista_num.append(num)

print(f'Números digitados: {lista_num}\n'
      f'Número em ordem crescente: {sorted(lista_num)}')
'''

#31. Fagaum programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa. 
    #Altura                              Peso 
                    #Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90 
    #Menor que 1,20     A               D                   G 
    #De 1,20 a 1,70     B               E                   H 
    #Maior que 1,70     c               F                   I
'''
h = float(input('Digite a altura em metros: '))
p = float(input('Digite o peso em kg: '))

if h < 1.20:
    if p <= 60:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: A')
    elif p > 60 and p <= 90:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: D')
    else:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: G')
elif h >= 1.20 and h <= 1.70:
    if p <= 60:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: B')
    elif p > 60 and p <= 90:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: E')
    else:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: H')
else:
    if p <= 60:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: C')
    elif p > 60 and p <= 90:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: F')
    else:
        print(f'Altura:{h}\n'
              f'Peso: {p}\n'
              f'Categoria: I')
'''

#32. Escrever um programa que leia o código do produto escolhido do cardapio de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente sera calculado um pedido. O cardapio da lanchonete segue o padrao abaixo: 
#Especificação      Código       Preço 
#Cachorro Quente    100          1.20 
#Bauru Simples      101          1.30 
#Bauru com Ovo      102          1.50 
#Hamburguer         103          1.20 
#Cheeseburguer      104          1.70 
#Suco               105          2.20 
#Refrigerante       106          1.00 
'''
print('Especificação      Código       Preço\n' 
'Cachorro Quente    100          1.20\n'
'Bauru Simples      101          1.30\n'
'Bauru com Ovo      102          1.50\n' 
'Hamburguer         103          1.20\n'
'Cheeseburguer      104          1.70\n' 
'Suco               105          2.20\n' 
'Refrigerante       106          1.00\n' )
cod_produto = int(input('Digite o código do produto: '))
qtd = int(input('Digite a quantidade: '))
if cod_produto == 100:
    valor_tot = qtd * 1.20
    print('Produto: Cachorro quente\n'
          f'Código: {cod_produto}\n'
          'Preço: R$1.20\n'
          f'Valor Total: R${valor_tot:.2f}')
elif cod_produto == 101:
    valor_tot = qtd * 1.30
    print('Produto: Bauru simples\n'
          f'Código: {cod_produto}\n'
          'Preço: R$1.30\n'
          f'Valor Total: R${valor_tot:.2f}')
elif cod_produto == 102:
    valor_tot = qtd * 1.50
    print('Produto: Bauru com ovo\n'
          f'Código: {cod_produto}\n'
          'Preço: R$1.50\n'
          f'Valor Total: R${valor_tot:.2f}')
elif cod_produto == 103:
    valor_tot = qtd * 1.20
    print('Produto: Hamburguer\n'
          f'Código: {cod_produto}\n'
          'Preço: R$1.20\n'
          f'Valor Total: R${valor_tot:.2f}')
elif cod_produto == 104:
    valor_tot = qtd * 1.70
    print('Produto: Cheeseburguer\n'
          f'Código: {cod_produto}\n'
          'Preço: R$1.70\n'
          f'Valor Total: R${valor_tot:.2f}')
elif cod_produto == 105:
    valor_tot = qtd * 2.20
    print('Produto: Suco\n'
          f'Código: {cod_produto}\n'
          'Preço: R$2.20\n'
          f'Valor Total: R${valor_tot:.2f}')
elif cod_produto == 106:
    valor_tot = qtd * 1.00
    print('Produto: Refrigerante\n'
          f'Código: {cod_produto}\n'
          'Preço: R$1.00\n'
          f'Valor Total: R${valor_tot:.2f}')
'''


#33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela). 
#PREÇO ANTIGO       PERCENTUAL DE AUMENTO         PREÇO NOVO                        MENSABEM 
#até R$ 50                  5%                    até R$ 80                         Barato 
#entre R$ 50 e R$ 100       10%                   entre R$ 80 e R$ 120 (inclusive)  Normal 
#acima de R$ 100            15%                   entre R$ 120 e R$ 200 (inclusive) Caro 
#                                                 acima de R$ 200                   Muito caro 
'''
valor_antigo = float(input('Digite o valor antigo: R$'))
if valor_antigo <= 50:
    valor_novo = valor_antigo + (valor_antigo * 0.05)
    print(f'Valor antigo: R${valor_antigo:.2f}\n'
          f'Valor novo: R${valor_novo:.2f}')
elif valor_antigo > 50  and valor_antigo <= 100:
    valor_novo = valor_antigo + (valor_antigo * 0.10)
    print(f'Valor antigo: R${valor_antigo:.2f}\n'
          f'Valor novo: R${valor_novo:.2f}')
else:
    valor_novo = valor_antigo + (valor_antigo * 0.15)
    print(f'Valor antigo: R${valor_antigo:.2f}\n'
          f'Valor novo: R${valor_novo:.2f}')

if valor_novo <= 80:
    print('Barato')
elif valor_novo > 80 and valor_novo <= 120:
    print('Normal')
elif valor_novo > 120 and valor_novo <= 200:
    print('Caro')
else:
    print('Muito caro')
'''


#34. Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito. 
#NOTA           CONCEITO (ATE 20 FALTAS)        CONCEITO (MAIS DE 20 FALTAS) 
#9.0 até 10.0               A                                 B
#7.5 até 8.9                B                                 C
#5.0 até 7.4                C                                 D
#4.0 até 4.9                D                                 E
#0.0 até 3.9                E                                 E
'''
nota =  float(input('Digite a nota: '))
faltas = int(input('Digite o número de faltas: '))

if faltas <= 20:
    if nota > 9:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: A')
    elif nota >= 7.5 and nota <= 8.9:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: B')
    elif nota >= 5.0 and nota <= 7.4:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: C')
    elif nota >= 4.0 and nota <= 4.9:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: D')
    elif nota >= 0 and nota <= 3.9:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: E')
else:
    if nota > 9:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: B')
    elif nota >= 7.5 and nota <= 8.9:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: C')
    elif nota >= 5.0 and nota <= 7.4:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: D')
    elif nota >= 4.0 and nota <= 4.9:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: E')
    elif nota >= 0 and nota <= 3.9:
        print(f'Nota: {nota}\n'
              f'Faltas: {faltas}\n'
              f'Conceito: E')
'''


#35. Leia uma data e determine se ela é valida. Ou seja, verifique se o més esta entre 1 e 12, e se o dia existe naquele més. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos nao bissextos. 
'''
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))
mes_30 = [4, 6, 9, 11]

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    if mes == 2:
        if dia > 29:
            print('Dia inválido! Fevereiro possui 29 dias!')
        else:
            print(f'{dia}/{mes}/{ano}') 
    else:
        if mes in mes_30:
            if dia > 30:
                print(f'Dia {dia} inválido. Mês {mes} só tem 30 dias!')
            else:
                print(f'{dia}/{mes}/{ano}')            

else:
    if mes == 2:
        if dia > 28:
            print('Dia inválido! Não é ano bissexto')
        else:
            print(f'{dia}/{mes}/{ano}') 
    else:
        if mes in mes_30:
            if dia > 30:
                print(f'Dia {dia} inválido. Mês {mes} só tem 30 dias!')
            else:
                    print(f'{dia}/{mes}/{ano}')                 
        else:
            if dia > 31:
                print(f'Dia {dia} inválido. Mês {mes} só tem 31 dias!')
            else:
                print(f'{dia}/{mes}/{ano}')                 
'''


#36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo: 
#Venda mensal                                               Comissão 
#Maior ou igual a R$100.000,00                              R$700,00 + 16% das vendas 
#Menor que R$100.000,00 e maior ou igual a R$80.000,00      R$650,00 + 14% das vendas 
#Menor que R$80.000,00 e maior ou igual a R$60.000,00       R$600,00 + 14% das vendas 
#Menor que R$60.000,00 e maior ou igual a R$40.000,00       R$550,00 + 14% das vendas 
#Menor que R$40.000,00 e maior ou igual a R$20.000,00       R$500,00 + 14% das vendas 
#Menor que R$20.000,00                                      R$400,00 + 14% das vendas 
'''
valor_mensal = float(input('Digite o valor da venda: R$'))
if valor_mensal >= 100000.00:
    comissao = 700 + (valor_mensal * 0.16)
    print(f'Valor mensal: R${valor_mensal}\n'
          f'Valor comissão: R${comissao:.2f}')
elif valor_mensal < 100000.00 and valor_mensal >= 80000.00:
    comissao = 650 + (valor_mensal * 0.14)
    print(f'Valor mensal: R${valor_mensal}\n'
          f'Valor comissão: R${comissao:.2f}')
elif valor_mensal < 80000.00 and valor_mensal >= 60000.00:
    comissao = 600 + (valor_mensal * 0.14)
    print(f'Valor mensal: R${valor_mensal}\n'
          f'Valor comissão: R${comissao:.2f}')    
elif valor_mensal < 60000.00 and valor_mensal >= 40000.00:
    comissao = 550 + (valor_mensal * 0.14)
    print(f'Valor mensal: R${valor_mensal}\n'
          f'Valor comissão: R${comissao:.2f}')
elif valor_mensal < 40000.00 and valor_mensal >= 20000.00:
    comissao = 500 + (valor_mensal * 0.14)
    print(f'Valor mensal: R${valor_mensal}\n'
          f'Valor comissão: R${comissao:.2f}')    
else:
    comissao = 400 + (valor_mensal * 0.14)
    print(f'Valor mensal: R${valor_mensal}\n'
          f'Valor comissão: R${comissao:.2f}')
'''


#37. As tarifas de certo parque de estacionamento são as seguintes: 
# 1º e 2º hora - R$ 1,00 cada 
# 3º e 4º hora - R$ 1,40 cada 
# 5º hora e seguintes - R$ 2,00 cada 
#O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará “dez para a uma da tarde”. Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada. 
'''
hora_chegada = int(input('Digite a hora de chegada: '))
minuto_chegada = int(input('Digite o minuto de chegada: '))
hora_saida = int(input('Digite a hora de saída: '))
minuto_saida = int(input('Digite o minuto de saída: '))
#arredonar minuto em hora
if minuto_chegada > 0:
    arredonda_hora_chegada = hora_chegada + 1
else:
    arredonda_hora_chegada = hora_chegada
if minuto_saida > 0:
    arredonda_hora_saida = hora_saida + 1
else:
    arredonda_hora_saida = hora_saida

#verificar tempo de permanência
if arredonda_hora_chegada > arredonda_hora_saida:
    permanencia = arredonda_hora_chegada - arredonda_hora_saida
else:
    permanencia = arredonda_hora_saida - arredonda_hora_chegada

#Calcular valor
if permanencia == 0:
    valor = 1
elif permanencia <= 2:
    valor = permanencia
elif permanencia > 2 and permanencia <= 4:
    valor = permanencia * 1.40
else:
    valor = permanencia * 2

print(f'Hora de chegada {hora_chegada}:{minuto_chegada}\n'
      f'Hora de saída {hora_saida}:{minuto_saida}\n'
      f'Tempo de permanência {permanencia} hora(s)\n'
      f'Valor R${valor:.2f}')
'''


#38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: 
#Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma data válida. Teste se o dia fornecido é um dia válido: dia > O, dia < 28 para o mês de fevereiro (29 se o ano for bissexto), dia < 30 em abril, junho, setembro e novembro, dia < 31 nos outros meses. Teste a validade do més: més > 0 e mês < 13. Teste a validade do ano: ano < ano atual (use uma constante definida com o valor igual a 2008). Imprimir: “data válida” ou “data inválida” no final da execução do programa.

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))
mes_30 = [4, 6, 9, 11]
data_atual = '2722024'

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    if mes == 2:
        if dia > 29:
            print('Dia inválido! Fevereiro possui 29 dias!')
        else:
            print(f'{dia}/{mes}/{ano}') 
    else:
        if mes in mes_30:
            if dia > 30:
                print(f'Dia {dia} inválido. Mês {mes} só tem 30 dias!')
            else:
                print(f'{dia}/{mes}/{ano}')            

else:
    if mes == 2:
        if dia > 28:
            print('Dia inválido! Não é ano bissexto')
        else:
            print(f'{dia}/{mes}/{ano}') 
    else:
        if mes in mes_30:
            if dia > 30:
                print(f'Dia {dia} inválido. Mês {mes} só tem 30 dias!')
            else:
                    print(f'{dia}/{mes}/{ano}')                 
        else:
            if dia > 31:
                print(f'Dia {dia} inválido. Mês {mes} só tem 31 dias!')
            else:
                print(f'{dia}/{mes}/{ano}')     

if ano > 2008:
    print('Ano inválido')
elif ano == 2008:
    if dia >= 28:
        if mes == 2:
            print('Data ')


#39. Uma empresa decide dar um aumento aos seus funcionarios de acordo com uma tabela que considera o salario atual e o tempo de servico de cada funcionario. Os funcionarios com menor salario terao um aumento proporcionalmente maior do que os funcionarios com um salario maior, e conforme o tempo de servi¢o na empresa, cada funcionario irá receber um bônus adicional de salario. Faça um programa que leia: 
# 0 valor do saldrio atual do funcionario; 
# 0 tempo de servigo desse funciondrio na empresa (número de anos de trabalho na empresa). 
#Use as tabelas abaixo para calcular o salario reajustado deste funcionario e imprima o valor do salério final reajustado, ou uma mensagem caso o funcionario nao tenha direito a nenhum aumento. 
#Salario Atual      Reajuste(%)    Tempo de Servico    Bonus 
#Até 500,00         25%            Abaixo de 1 ano     Sem bénus 
#Até 1000,00        20%            De 1 a 3 anos       100,00 
#Até 1500,00        15%            De 4 a 6 anos       200,00 
#Até 2000,00        10%            De 7 a 10 anos      300,00 
#Acima de 2000,00   Sem reajuste   Mais de 10 anos     500,00 


#40. O custo ao consumidor de um carro novo é a soma do custo de fabrica, da comissao do distribuidor, e dos impostos. A comissao e os impostos sao calculados sobre o custo de fabrica, de acordo com a tabela abaixo. Leia o custo de fabrica e escreva o custo ao consumidor. 
#CUSTO DE FABRICA               % DO DISTRIBUIDOR       % DOS IMPOSTOS 
#até R$12.000,00                5                       isento 
#entre R$12.000,00 e 25.000,00  10                      15 
#acima de R$25.000,00           15                      20 


#41. Faga um algoritmo que calcule o IMC de uma pessoa e mostre sua classificagao de acordo com a tabela abaixo: 
#IMC            Classificagao 
#<185           Abaixo do Peso 
#18,6 - 24,9    Saudavel 
#25,0 - 29,9    Peso em excesso 
#30,0 - 34,9    Obesidade Grau I 
#35,0 - 39,9    Obesidade Grau II(severa) 
#> 40,0         Obesidade Grau III(mórbida)
#1. Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos: 
#(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2,-5,7. 
#(b) Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] do vetor e mostre na tela esta soma. 
#(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100. 
#(d) Mostre na tela cada valor do vetor A, um em cada linha. 
'''
a = []
for n in 1, 0, 5, -2, -5, 7:
    a.append(n)
print(f'A:{a}')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = a[0] + a[1] + a[5]
print(f'B: {a[0]} + {a[1]} + {a[5]} = {soma}')

a[4] = 100
print(f'C:{a}')

for n in a:
    print(n)
'''

#2. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos. 
'''
lista_num = []
for n in range(1, 7):
    valor = int(input(f'Digite o {n}º valor:'))
    lista_num.append(valor)
print(f'Listas dos números digitados: {lista_num}')
'''

#3. Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos tém 10 elementos cada. Imprimir todos os conjuntos. 
'''
lista_num = []
lista_quadrada = []
for n in range(1, 11):
    lista_num.append(int(input(f'Digite o {n}º número: ')))

for n in lista_num:
    lista_quadrada.append(n ** 2)

print(f'Lista dos números digitados: {lista_num}')
print(f'Lista dos números digitados ao quadrado: {lista_quadrada}')
'''

#4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondentes a duas posicoes no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y. 
'''
lista_num = []
for n in range(1, 9):
    lista_num.append(int(input(f'Digite o {n}º número: ')))
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
print(f'Lista dos números digitados: {lista_num}')
print(f'Soma dos valores nas posições X e Y: {x} + {y} = {lista_num[x] + lista_num[y]}')
'''

#5. Leia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui. 
'''
lista_num = []
cont_par = 0
for n in range(1, 11):
    lista_num.append(int(input(f'Digite o {n}º número: ')))
    if n % 2 == 0:
        cont_par += 1
print(f'Números digitados: {lista_num}')
print(f'{cont_par} números pares digitados')
'''

#6. Faça um programa que receba do usuario um vetor com 10 posições. Em seguida devera ser impresso o maior e o menor elemento do vetor.
'''
lista_num = []
for n in range(1, 11):
    lista_num.append(int(input(f'Digite o {n}º número: ')))
print(f'Números digitados: {lista_num}')
print(f'Maior número digitado: {max(lista_num)}')
print(f'Menor número digitado: {min(lista_num)}')
'''

#7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição que ele se encontra. 
'''
lista_num = []

for n in range(1, 11):
    lista_num.append(int(input(f'Digite o {n}º número: ')))
    maior = max(lista_num)

print(f'Números digitados: {lista_num}')
print(f'Maior número digitado: {maior}')
print(f'Posição do maior número digitado: {lista_num.index(maior)}')
'''

#8. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa. 
'''
lista_num = []
for n in range(1, 7):
    lista_num.append(int(input(f'Digite o {n}º número: ')))
    maior = max(lista_num)

print(f'Números digitados: {lista_num[::-1]}')
'''

#9. Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa. 
'''
lista_num = []
while len(lista_num) < 6:
    num = int(input(f'Digite um número par: '))
    if num % 2 == 0:
        lista_num.append(num)
    else:
        print('Número precisa ser par')
print(lista_num[::-1])
'''

#10. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral. 
'''
notas = []
while len(notas) < 15:
    nota = int(input('Digite a nota do aluno: '))
    notas.append(nota)

print(f'Notas digitadas: {notas}\n'
      f'Méddia das notas: {sum(notas) / 15}')
'''

#11. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor. 
'''
lista_num = []
lista_num_neg = []
soma = 0
cont = 0
while cont < 10:
    num = int(input('Digite um número real: '))
    if num < 0:
        lista_num_neg.append(num)
    else:
        lista_num.append(num)
        soma += num
    cont += 1
print(f'A lista possui {len(lista_num_neg)} números negativos ({lista_num_neg})\n'
      f'Soma dos números positivos digitados ({lista_num}): {soma}')
'''

#12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a média dos valores. 
'''
lista_num = []
for n in range(1, 6):
    lista_num.append(int(input('Digite um número: ')))

print(f'Lista dos números digitados: {lista_num}\n'
      f'Maior número digitado: {max(lista_num)}\n'
      f'Menor número digitado: {min(lista_num)}\n'
      f'Média dos números digitados: {sum(lista_num) / 6}')
'''

#13. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
'''
lista_num = []
for n in range(1, 6):
    lista_num.append(int(input('Digite um número: ')))

print(f'Lista dos números digitados: {lista_num}\n'
      f'Posição do maior número digitado: {lista_num.index(max(lista_num))}\n'
      f'Posição do menor número digitado: {lista_num.index(min(lista_num))}\n')
'''

#14. Façaum programa que leia um vetor de 10 posições e verifique se existem valores iguais e Os escreva na tela. 
'''
lista_num = []
lista_repetido = []
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    lista_num.append(num)
for numero in lista_num:
    if lista_num.count(numero) > 1: 
        lista_repetido.append(numero)

print(f'Lista dos números digitados: {lista_num}\n'
      f'Lista dos números repetidos digitados: {lista_repetido}')
'''

#15. Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos. 
'''
lista_num = []
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    lista_num.append(num)

print(f'Lista dos números digitados sem repetição: {set(lista_num)}\n')
'''
#16. Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso, o código for diferente de 1  2 escreva uma mensagem informando que o código é inválido. 
'''
lista_num = []
while True:    
    for n in range(1, 6):
        num = int(input(f'Digite o {n}º número: '))
        lista_num.append(num)

    print('Digite um código:\n'
        '1- Mostrar números digitados.\n'
        '2- Mostrar números digitados na ordem inversa.\n'
        '0- Sair.')
    cod = int(input())
    if cod == 1:
        print(f'Código: {cod}\n'
              f'Lista dos números digitados: {lista_num}')
    elif cod == 2:
        print(f'Código: {cod}\n'
              f'Lista dos números digitados: {lista_num[::-1]}')
    elif cod == 0:
        print(f'Código: {cod}\n'
              'FIM.')
        break
    else:
        print(f'Código {cod} inválido!')
        break
'''

#17. Leia um vetor de 10 posições e atribua valor O para todos os elementos que possuírem valores negativos. 
'''
lista_num = []
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    if num < 0:
        num = 0
        lista_num.append(num)
    else:
        lista_num.append(num)
print(f'Lista dos números digitados: {lista_num}')
'''

#18. Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x num vetor e mostre-os na tela. 
'''
lista_num = []
mult_x = []
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    lista_num.append(num)

x = int(input('Digite um número: '))
for num in lista_num:
    if num % x == 0:
        mult_x.append(num)
print(f'Lista dos números digitados: {lista_num}\n'
      f'Lista dos números múltiplos de {x}: {mult_x}')
'''

#19. Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i +5*1)%(i+1), sendo i a posi¢ao do elemento no vetor. Em seguida imprima o vetor na tela. 
'''
lista_num = range(1, 6)
lista_i = []
for num in lista_num:
    i = lista_num.index(num)
    eq_i = (i + (5 * i)) % (i + 1)
    lista_i.append(eq_i)
print(lista_i)
'''

#20. Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um vetor com 10 posições. Preencha um segundo vetor apenas com os nimeros impares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha. 
'''
lista_num = []
lista_impar = []
for n in range(1, 11):
    num = (int(input('Digite um número de 0 a 50: ')))
    lista_num.append(num)
    if num % 2 != 0:
        lista_impar.append(num)

print('Lista dos números digitados:')
cont = 0
while cont < 10:
    print(lista_num[cont], end=' ')
    if ((cont + 1) % 2 == 0):
        print('')
    cont += 1

print('Lista dos números ímpares do vetor:')
cont = 0
while cont < len(lista_impar):
    print(lista_impar[cont], end=' ')
    if ((cont + 1) % 2 == 0):
        print('')
    cont += 1
'''

#21. Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C
'''
lista_a = []
lista_b = []
lista_c = []
#adicionando elementos lista A
for n in range(1, 6):
    num = int(input('Digite um número da lista A: '))
    lista_a.append(num)
#adicionando elementos lista B
for n in range(1, 6):
    num = int(input('Digite um número da lista B: '))
    lista_b.append(num)
#Somando elementos da lista A + B e adicionando na lista C
for n in range(0, 5):
    soma = lista_a[n] + lista_b[n]
    lista_c.append(soma)

for n in range(0, 5):
    print(f'{lista_a[n]} + {lista_b[n]} = {lista_c[n]}')
'''

#22. Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares os valores do primeiro e nas posições impares os valores do segundo. 
'''
lista_a = []
lista_b = []
lista_c = []
#adicionando elementos lista A
for n in range(1, 6):
    num = int(input('Digite um número da lista A: '))
    lista_a.append(num)
#adicionando elementos lista B
for n in range(1, 6):
    num = int(input('Digite um número da lista B: '))
    lista_b.append(num)
for n in range(0, 5):
    if n % 2 == 0:
        lista_c.append(lista_b[n])
    else:
        lista_c.append(lista_a[n])

print(f'Lista A: {lista_a}\n'
      f'Lista B: {lista_b}\n'
      f'Lista Junta: {lista_c}')
'''

#23. Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por: x1 * y1 + x2 * y2 + ... + xn * yn. 
'''
lista_a = []
lista_b = []
produto = 0
#adicionando elementos lista A
for n in range(1, 6):
    num = int(input('Digite um número da lista A: '))
    lista_a.append(num)
#adicionando elementos lista B
for n in range(1, 6):
    num = int(input('Digite um número da lista B: '))
    lista_b.append(num)

for n in range(0, 5):
    if n < 4:
        print(f'({lista_a[n]} * {lista_b[n]}) +',end=' ')
    else:
        print(f'({lista_a[n]} * {lista_b[n]}) = ',end=' ')
    produto += (lista_a[n] * lista_b[n])
print(produto)
'''
#24. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Mostre o nimero do aluno mais baixo e do mais alto, juntamente com suas alturas. 

#25. Faga um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que nao sao múltiplos de 7 ou que terminam com 7. 

###26. Faça um programa que calcule o desvio padrao de um vetor v contendo n = 10 números, onde m é a media do vetor. 

#27. Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas posições no vetor. 

#28. Leia 10 numeros inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2. Copie os valores impares de v para v1, e os valores pares de v para v2. Note que cada um dos vetores v1 e v2 tém no maximo 10 elementos, mas nem todos os elementos sao utilizados. No final escreva os elementos UTILIZADOS de v1 e v2.

#29. Faça um programa que receba 6 números inteiros e mostre: 
# Os números pares digitados; 
# A soma dos números pares digitados; 
# Os números impares digitados; 
# A quantidade de números impares digitados; 

#30. Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que contém apenas os números que estão em ambos os vetores. Não deve conter números repetidos. 

#31. Façaum programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores. Não deve conter números repetidos. 

#32. Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo: 
# Soma entre x e y: soma de cada elemento de = com o elemento da mesma posição em y. 
# Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição em y. 
# Diferença entre x e y: todos os elementos de = que não existam em y. 
# Interseção entre : e y: apenas os elementos que aparecem nos dois vetores. 
# União entre = e y: todos os elementos de r, e todos os elementos de y que não estão em r.

#33. Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero. Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor. 

#34. Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número. Note que cada valor digitado pelo usuário deve ser pesquisado no vetor, verificando se ele existe entre os números que já foram fornecidos. Exibir na tela o vetor final que foi digitado. 

#35. Faça um programa que leia dois números a e b (positivos menores que 10000) e: 
# Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algarismo menos significativo; 
# Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construídos anteriormente. 
#Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 à próxima posição. 

#36. Leia um vetor com 10 números reais, ordene os elementos deste vetor, e no final escreva os elementos do vetor ordenado.

#37. Considere um vetor A com 11 elementos onde Al < A2 < ... < A6 > AT > A8 > ... > A11, ou seja, está ordenado em ordem crescente até o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente. Dado o vetor da questao anterior, proponha um algoritmo para ordenar os elementos. 

#38. Pega ao usuario para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao final na tela os valores em ordem. 

#39. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de Pascal: 
#1
#1  1
#1  2  1
#1  3  3  1
#1  4  6  4  1
#1  5  10 10 5  1
#...































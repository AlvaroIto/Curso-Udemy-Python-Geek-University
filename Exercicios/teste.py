'''
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
'''
cont = 2
div = 0
num = int(input('Digite um número: '))

while cont <  num:
    if num > 1:
        if num % cont == 0:
            div += 1
    cont += 1

if div == 0:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')

'''
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
'''
vetor=[]
for c in range(3):
    n = int(input("Digite um número para armazena-lo:"))
    divisores = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            divisores += 1
    if divisores > 1:
        None
    else:
        vetor+=[n]
        index = vetor.index()
print(f'Os primos nesse vetor são {vetor}:{index}')
"""
Try / Except / Else / Finally

Dica de onde e quando tratar código:
- Toda entrada deve ser tratada!

Sintaxe:

else - é executado somente se não ocorrer erro
finally - O bloco finally é sempre executado. Geralmente é utilizado para fechar ou desalocar recursos

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('close')    

"""




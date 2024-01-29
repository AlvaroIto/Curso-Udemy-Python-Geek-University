"""
Bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programe para de funcionar e o usuário receba mensagem de erro inesperada.

Sintaxe:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

#Exemplo - tratando erro geral
try:
    geek()
except:
    print('Deu algum problema')

    
#Exemplo -  tratando erro específico
try:
    geek()
except NameError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


"""

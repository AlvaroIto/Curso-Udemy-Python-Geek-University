"""
Preservando metadatas com wraps

Metadados - São dados intrísecos em arquivos.
Wraps - São funções que envolvem elementos com diversas finalidades

 

"""
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        '''Eu sou uma função (logar) dentro de outra'''
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, *kwargs)
    return logar

@ver_log
def soma(a, b):
    '''Soma dois números'''
    return a + b

@ver_log
def mult(a, b):
    '''Multiplica dois números'''
    return a * b

print(soma(2, 5))
print(mult(2, 6))

print(soma.__name__)
print(soma.__doc__)
print(mult.__name__)
print(mult.__doc__)
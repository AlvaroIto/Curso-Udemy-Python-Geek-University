"""
Decorators com diferentes assinaturas

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de pedir {principal} e acompanhado de {acompanhamento}, por favor'


print(saudacao('Felicity'))
print(ordenar('Picanha', 'Batata Frita'))


"""

#Decorador com argumentos
def verifica_primeiro_argumento(valor):
    def 
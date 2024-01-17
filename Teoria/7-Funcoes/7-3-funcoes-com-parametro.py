"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> said

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saida;
- Possuem entrada mas não possuem saida;
- Não possuem entrada mas possuem saida
- Possuem entrada e saida

def quadrado(numero):
    return numero ** 2

print(quadrado(2))

#Funções podem ter n parâmetros de entrada
#Exemplos
def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return(num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))
print(multiplica(2, 4))
print(multiplica(10, 20))
print(outra(3, 2, 'geek '))
print(outra(5, 4, 'Python '))


"""

#nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))


#Diferença entre Parâmetros e Argumentos
#Parâmetros são variáveis declaradas na definição de uma função
#Argumentos são dados passados durante a execução de uma função


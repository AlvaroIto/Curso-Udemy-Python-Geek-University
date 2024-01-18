"""
Funções com parâmetro padrão


- Funções onde a passagem de parâmetro seja opcional;


#Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek')
print()


#Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2
print(quadrado(3))
print(quadrado())


#Exemplo de função onde há um valor de parâmetro padrão
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))
print(exponencial(3))


#Por que utilizar parâmetros com valor default?
- Nos permite ser mais flexíveis nas funções
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legíveis de código


"""


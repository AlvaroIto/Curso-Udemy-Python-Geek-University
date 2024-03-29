"""
Escopo de variáveis

Dois casos de escopo:
1- Variáveis globais
    - São reconhecidas, ou seja, seu escopo compreende todo o programa
2- Variáveis locais
    - São reconhecidas apenas no bloco onde foram declaradas

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dados dela
Este tipo é inferido ao atribuírmos o valor a mesma
exemplo em C:
int numero = 42;

numero = 42 # Variavel global
print(numero)
print(type(numero))

numero = 42
if numero > 10:
    novo = numero + 10 # variavel local (declarada dentro do bloco if)
    print(novo)
    
"""
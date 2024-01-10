"""
Estruturas Lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Para o and, ambos os valores precisam ser True
if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail')

Para o or, um ou outro precisa ser True
ativo = True
logado = False

if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail')

Para o not, o valor do booleano é invertido
ativo = False

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')


    
"""
ativo = False
logado = False

if ativo is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')
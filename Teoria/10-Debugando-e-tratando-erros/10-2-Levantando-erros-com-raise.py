"""
Levantando os erros com raise

raise -> Lança exceções

OBS: raise não é uma função é uma palavra reservada como def.
O raise, assim como return, finaliza a função, ou seja, nada após o raise é executado

Simplicando, pense no raise como sendo útil para que possamos criar nossas próprias excessões e mensagem de erro

Sintaxe:
raise TipoDoErro('Mensagem de erro')

raise ValueError('Valor incorreto')


Exemplo:
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'Azul')
#colore(4, 'azul')
#colore('Geek', 4)


"""

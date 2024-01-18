"""
**Kwargs

Poderiamos chamar esse paramatro por **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados e transforma esses parâmetros extras em um dicionário


"""

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernando='azul', vanessa='branco')


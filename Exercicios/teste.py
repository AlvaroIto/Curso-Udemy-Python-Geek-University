'''
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
'''
class Agenda:
    
    contador = 0
    lista_agenda = []
    
    def __init__(self, nome, idade, altura) -> None:
        self.__contato = Agenda.contador + 1
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        Agenda.contador = self.__contato

    
    def armazena_pessoa(self):
        if Agenda.contador > 3:
            print('Agenda lotada!')
        else:
            lista = []
            lista.append(self.__nome, self.__idade, self.__altura )
            print(f'Contato armazenado: {lista}')
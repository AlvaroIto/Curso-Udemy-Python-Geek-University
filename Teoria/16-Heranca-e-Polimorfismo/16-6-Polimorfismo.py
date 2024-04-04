'''
Polimorfismo
Poli - Muitas
Morfis - Formas

Quando um método é reimplementado na classe pai em classes filhas, estamos realizando uma sobrescrita de método (Overriding)
O Overriding é a melhor representação de polimorfismo


'''

class Animal(object):
    def __init__(self, nome) -> None:
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')
    
    def comer(self):
        print(f'{self.__nome} está comendo')


class Cachorro(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    def falar(self):
        print(f'{self._Animal__nome} faz au au')

class Gato(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    def falar(self):
        print(f'{self._Animal__nome} faz miau')

class Rato(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    def falar(self):
        print(f'{self._Animal__nome} faz riri')


rex = Cachorro('rex')
rex.falar()
rex.comer()

felix = Gato('Felix')
felix.falar()
felix.comer()

mickey = Rato('Mickey')
mickey.falar()
mickey.comer()
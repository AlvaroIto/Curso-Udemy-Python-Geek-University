'''
Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas

Pode ser feita de 2 maneiras:
    - Multiderivação Direta
    - Multiderivação Indireta


#Exemplo Multiderivação Direta
class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2):
    pass


#Exemplo Multiderivação Indireta
class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass
  

'''

class Animal:
    def __init__(self, nome) -> None:
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    
class Aquatico(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    def nadar(self):
        return f'{self._Animal__nome} está nadando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'
    
class Terrestre(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    def andar(self):
        return f'{self._Animal__nome} está andando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome) -> None:
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())

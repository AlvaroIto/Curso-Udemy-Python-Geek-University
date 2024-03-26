'''
O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Abastração em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados do usuário

############ EXEMPLO SEM ENCAPSULAMENTO
class Conta:
    contador = 400
    
    def __init__(self, titular, saldo, limite) -> None:
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.valor -= valor

conta1 = Conta('Geek', 150.00, 1500.00)
print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
########################################

############ EXEMPLO ENCAPSULADO
class Conta:
    contador = 400
    
    def __init__(self, titular, saldo, limite) -> None:
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor

conta1 = Conta('Geek', 150.00, 1500.00)


'''

class Conta:
    contador = 400
    
    def __init__(self, titular, saldo, limite) -> None:
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor

conta1 = Conta('Geek', 150.00, 1500.00)

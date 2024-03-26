'''
Objetos são instâncias ad classe, ou seja, após o mapeamento do objeto do mundo real para sua representação computacional, devemos criar quantos objetos forem necessários


'''

class Lampada:
    def __init__(self, cor, voltagem, luminosidade) -> None:
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True
    
    def mostra_dados(self):
        print(f'Cor: {self.__cor} Voltagem: {self.__voltagem} Luminosidade: {self.__luminosidade}')

class Cliente:
    def __init__(self, nome, cpf) -> None:
        self.__nome = nome
        self.__cpf = cpf

class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente) -> None:
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
    
#INSTÂNCIAS/OBJETOS
lamp1 = Lampada('branca', 110, 60)
lamp1.ligar_desligar()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
Lampada.mostra_dados(lamp1)


cli1 = Cliente('Felicity','123.456.789-00')
conta1 = ContaCorrente(5000, 20000, cli1)

conta1.mostra_cliente()

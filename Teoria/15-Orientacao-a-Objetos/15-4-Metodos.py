'''
Métodos (funções): Representam os comportamentos do objeto ou seja, as ações que esse objeto pode realizar no seu sistema

O método __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe

Os métodos sâo divididos em 2 grupos:

- MÉTODO DE INSTÂNCIA (criamos quando precisamos acessar os atributos de instância)

class Produto:
    contador = 0
    def __init__(self, nome, descricao, valor) -> None:
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

#Método de instância 
    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

p1 = Produto('Playstation', 'Video Game', 2300)
print(p1.desconto(50))


- MÉTODO DE CLASSE (Criamos quando não precisamos acessar os atributos de instância)

class Usuario:
    
    contador = 0
    
#Método de classe
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    def __init__(self, nome, email, senha) -> None:
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        Usuario.contador =  self.__id

user = Usuario('Felicity', 'felicity@gmail.com', '123456')
Usuario.conta_usuario()



MÉTODO PRIVADO:

class Usuario:
    
    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, email, senha) -> None:
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        Usuario.contador =  self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

#Método privado
    def __gera_usuario(self):
        return self.__email.split('@')[0]

user = Usuario('Felicity', 'felicity@gmail.com', '123456')
Usuario.conta_usuario()



MÉTODO ESTÁTICO (não tem acesso a classe):
class Usuario:
    
    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuários no sistema')

#Método Estático
    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, email, senha) -> None:
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        Usuario.contador =  self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')
    
    def __gera_usuario(self):
        return self.__email.split('@')[0]

user = Usuario('Felicity', 'felicity@gmail.com', '123456')


'''

'''
Atributos Representam as características do objeto.
Pelos atributos, conseguimos representar computacionalmente os estados do objeto
Os atributos podem ser Públicos ou Privados:
    Atributo público - por convenção, ficou estabelecido que todo o atributo de uma clase é público (pode ser utilizado em todo projeto)
    Atributo privado - deve ser utilizado o __ no inicio do nome (pode ser utilizado somente dentro da própria classe)

São divididos em 3 grupos:
    - Atributos de instância
    - Atributos de classe
    - Atributos Dinâmicos
   
#Atributos de instância: São atributos declarados dentro do método construtor.

#Atributos de classe: São atributos declarados diretamente na classe. ou seja, fora do construtor. Geralmente é iniciado com um valor e este valor é compartilhado entre todas as instâncias da classe, ou seja, ao inves de cada instãncia da classe ter seus proprios valores, como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo
exemplo:
class Produto:

    #Atributo de Classe
    imposto = 1.05

    def __init__(self, nome, descricao, valor) -> None:
        self.nome =  nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)

#Atributos Dinâmicos: São Atributos de instância que podem ser declarados em tempo de execução
exemplo:
p1 = Produto('Produto 1', 'Descrição 1', 'Valor 1')
p2 = Protudo('Produto 2', 'Descrição 2', 'Valor 2')
p2.peso = 'Peso 2'



'''
#Atributos Públicos
class Lampada:
    
    def __init__(self, voltagem, cor) -> None:
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False
    
class ContaCorrente:
    def __init(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor) -> None:
        self.nome =  nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha  = senha

#Atributos Privados
class Acesso:
    def  __init__(self, email, senha) -> None:
        self.__email = email
        self.__senha = senha


'''
A idéia de herança é a de reaproveitar o código e também de extender nossas classes.

Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e métodos da clase herdada

Quando uma classe herda de outra, ela herda TODOS os atributos e métodos da classe herdada

Exemplo:
Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;


'''

class Pessoa:
    def __init__(self, nome, sobrenome, cpf) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    #Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda) -> None:
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

    
class Funcionario(Pessoa):
    #Funcionário herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula) -> None:
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

cliente1 = Cliente('Angelina', 'Jolie', '132.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

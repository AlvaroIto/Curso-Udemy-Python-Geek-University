#1. Crie um novo pacote com o nome: heranca. Todas as (três) classes criadas abaixo deverão ser salvas neste pacote. 
#2. Crie uma classe Equipamento com dois atributos privados. 
#3. Crie uma classe Computador com dois atributos à sua escolha, também privados. A classe Computador deverá herdar tudo da classe Equipamento. 
#4. Crie os métodos de acesso e de modificação para todos os atributos definidos em ambas as classes. 
#5. Crie uma classe TestaEquipamento, que deverá conter o método main(), crie nela um objeto da classe Equipamento e instancie os dois atributos que você declarou na classe Equipamento. Crie também um objeto da classe Computador, utilizando os dois atributos declarados na própria classe e os dois herdados da classe Equipamento.
#6. O método main() deve exibir as informações dos dois objetos criados. 
#7. Criar 0 método exibe() na classe Equipamento para mostrar os dados dessa classe. 
#8. Reescreva o método exibe() na classe Computador, aproveitando o que ja esta escrito na superclasse Equipamento.

class Equipamento:
    def __init__(self, atributo1, atributo2) -> None:
        self.__atributo1 = atributo1
        self.__atributo2 = atributo2
    
    @property
    def atributo1(self):
        return self.__atributo1
    
    @atributo1.setter
    def atributo1(self, novo_atributo1):
        self.__atributo1 = novo_atributo1
    
    @property
    def atributo2(self):
        return self.__atributo2
    
    @atributo2.setter
    def atributo2(self, novo_atributo2):
        self.__atributo2 = novo_atributo2
    
    def exibir(self):
        return f'Equipamento com {self.__atributo1} e {self.__atributo2}'


class Computador(Equipamento):
    def __init__(self, atributo1, atributo2, cpu, monitor) -> None:
        super().__init__(atributo1, atributo2)
        self.__cpu = cpu
        self.__monitor = monitor

    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, novo_cpu):
        self.__cpu = novo_cpu

    @property
    def monitor(self):
        return self.__monitor
    
    @monitor.setter
    def monitor(self, novo_monitor):
        self.__monitor = novo_monitor

    def exibir(self):
        return f'Computador com {self.atributo1}, {self.atributo2}; {self.__cpu} e {self.__monitor}'

eq1 = Equipamento('atributo1', 'atributo2')
comp1 = Computador('atributo3', 'atributo4', 'cpu1', 'monitor1')

print(eq1.exibir())
print(comp1.exibir())
#1. Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura. Crie os métodos públicos necessários para sets e gets e também um método para imprimir os dados de uma pessoa. 
'''
class Pessoa:
    def __init__(self, nome, idade, altura) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    def dados(self):
        return f'Nome: {self.__nome}\nIdade: {self.__idade}\nAltura: {self.__altura:.2f}'

pessoa1 = Pessoa('Angelina', 34, 1.80)
print(pessoa1.dados())
'''

#2. Crie uma classe Agenda que pode armazenar 10 pessoas e seja capas de realizar as seguintes operações: 
# void armazenaPessoa(String nome, int idade, float altura); 
# void removePessoa(String nome); 
# int buscaPessoa(String nome); // informa em que posicão da agenda esta a pessoa 
# void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda 
# void imprimePessoa(int index); // imprime os dados da pessoa que está na posição “i” da agenda.

class Agenda:
    def __init__(self, pessoa) -> None:
        self.__pessoa = pessoa
    
    def armazena_pessoa(self):
        contador = 0
        if contador < 3:
            lista = []
            lista.append(self.__pessoa)
            contador += 1
        else:
            print('Agenda lotada!')
    
    def imprime_agenda(self):
        for n in lista:
            


class Pessoa:
    def __init__(self, nome, idade, altura) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura =altura

pessoa = Pessoa('Angelina', 45, 1.80)



#3. Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe deve armazenar o andar atual (térreo = O), total de andares no prédio, excluindo o térreo, capacidade do elevador, e quantas pessoas estão presentes nele. 
#A classe deve também disponibilizar os seguintes métodos: 
    # Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio); 
    # Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço); 
    # Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele); 
    # Sobe: para subir um andar (ndo deve subir se já estiver no tltimo andar); 
    # Desce: para descer um andar (ndo deve descer se ja estiver no térreo); 
    # Encapsular todos os atributos da classe (criar os métodos set e get).

#4. Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume e trocar os canais da televisao. 
    # O controle de volume permite aumentar ou diminuor a poténcia do volume de som em uma unidade de cada vez; 
    # O controle de canal também permite aumentar e diminuir o nimero do canal em uma unidade, porém, também possibilita trocar para um canal indicado; 
    # Também devem ecistir métodos para consultar o valor do volume de som e o canal selecionado.

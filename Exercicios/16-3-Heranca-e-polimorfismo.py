#1. Crie um novo pacote chamado sobrecarga 
#2. Crie uma classe Pessoa 
#3. Na classe Pessoa crie 3 variáveis de instância: código, nome e idade 
#4. Crie um método exibe(), que exiba o conteúdo de todas as variaveis declaradas na classe em questao 
#5. Crie uma sobrecarga do método exibe() que receba como parametro um número inteiro e decida por meio do valor desse parametro se a idade será exibida ou não. Para isso use o seguinte critério: se o valor do parametro for igual a 1, imprima idade, se não, ndo imprima a idade, mas apenas as outras variaveis de instancia 
#6. Crie um construtor padrao explicito para a classe Pessoa, esse construtor devera exibir uma mensagem: “Construtor padrão” 
#7. Crie uma classe chamada TestaPessoa que instancie um objeto da classe Pessoa usando o construtor padrão
#8. Ainda na classe TestaPessoa, inicialize as variáveis de instância: código, nome e idade com valores à sua escolha e acione o método exibe(), sem nenhum parâmetro 
#9. Repita a operação da questão anterior, acionando o método exibe(), passando a ele um argumento inteiro de valor 1 
#10. Repita o que foi feito na questão anterior, só que desta vez, passando um argumento diferente de 1 
#11. Crie um construtor sobrecarregado que permita instanciar objetos com os 3 valores sendo inicializados por valores passados como parâmetros 
#12. Na classe TestaPessoa instancie um objeto usando o segundo construtor (com os 3 parâmetros). 
#13. Exiba os dados do objeto que foi instanciado na questão anterior por meio do método exibe() sem argumentos

class Pessoa:
    def __init__(self, codigo, nome, idade) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
    
    def exibe(self,mostrar_idade=0):
        if mostrar_idade == 1:
            return f'Código: {self.__codigo}\nNome: {self.__nome}\nIdade: {self.__idade}'
        else:
            return f'Código: {self.__codigo}\nNome: {self.__nome}\n'

class Testa_Pessoa(Pessoa):
    def __init__(self, codigo, nome, idade) -> None:
        super().__init__(codigo, nome, idade)
        print(f'Construtor padrão')


p1 = Pessoa(1, 'Angelina', 45)
print(p1.exibe(1))
p2 = Testa_Pessoa(2, 'Felicity', 40)
print(p2.exibe())
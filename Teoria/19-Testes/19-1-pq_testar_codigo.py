'''
Testes automatizados

        Aplicação Web
----------------------------
/                          /
/    Frontend e Backend    /
----------------------------
/   testes automatizados   /
----------------------------

Por que testar nosso código?
    - Reduzir bugs no código
    - Teste garatem que novos recursos da sua aplicação não quebrem recursos antigos
    - Garantem que bugs que foram corrigidos anteriormente continuem corrigidos
    - Refatoração não tragam novos bugs

TDD - Test Driven Development (Desenvolvimento guiado por teste)
Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro
    - Então você escreve o código mínimo suficiente para fazer o teste passar
    - Refatora o código paraa realizar a funcionalidade e testa novamente
    - Uma vez que teste passou, o recurso é considerado completo
Estes estágios de desenvolvimento do TDD São conhecidos como:
    - Red
    - Green
    - Refactor

'''

class Gato:
    def __init__(self, nome) -> None:
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        print(f'{self.__nome} está miando...')



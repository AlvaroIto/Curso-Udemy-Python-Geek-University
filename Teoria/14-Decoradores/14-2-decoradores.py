"""
Decorators

- Decortators são funções
- Decorators envovelm outras funções e aprimoram seus comportamentos
- Decorators também são exemplos de HOF
- Decorators tem uma sintaxe própria usando @ (syntact sugar)

"""

#Decorators com Syntax sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo
    
@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()

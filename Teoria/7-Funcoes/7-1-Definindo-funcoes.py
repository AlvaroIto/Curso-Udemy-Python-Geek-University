"""
Definindo funções

- Funções são pequenos trechos de código que realizam tarefas específicas.
- Pode ou não receber entradas de dados e retornar uma saída de dados.
- Muito úteis para executar procedimentos similares por repetidas vezes

OBS: Se você escrever uma função que realiza várias tarefas dentro dela é bom fazer uma verificação para que a função seja simplificada

Já utilizamos várias funções:
- print()
- len()
- max()
- min()
- count()

#Utilizando a função integrada (bult-in) do Python print()
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores)

curso = 'Programação em Python'
print(curso)

Em Python, a forma geral de definir uma função é:^

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
nome_da_funcao = SEMPRE, com letras minúsculas, e se for nome composto, separada por underline;
parametros_de_entrada = Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não
bloco_da_funcao = também chamado de corpo da função ou implementação, é onde o processamento da função acontece
Neste bloco, pode ter ou não retorno da função

"""
#Definindo a primeira função
def diz_oi():
    print('Oi!')
#OBS: 
#-dentro das funções podemos utilizar outras funções
#-nossa função só executa 1 tarefa
#-esta função não recebe nenhum parametro de entrada
#-esta funçao não retorna nada

#Utilizando funções
diz_oi()


#EXEMPLO2
def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

cantar_parabens()

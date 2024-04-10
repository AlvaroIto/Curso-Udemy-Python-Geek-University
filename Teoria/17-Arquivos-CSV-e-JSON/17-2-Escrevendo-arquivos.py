'''
writerow() - Escreve uma linha
writer() - Gera um objeto para que possamos escrever em um arquivo CSV. 

from csv import writer

with open ('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração em minutos: ')
            escritor_csv.writerow([filme, genero, duracao])

            

dictwriter()

from csv import DictWriter

with open ('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração em minutos: ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})

'''



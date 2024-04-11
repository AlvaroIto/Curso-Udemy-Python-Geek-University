'''

Python tem um módulo built-in para se trabalhar com data e hora chamado datetime

import datetime

print(dir(datetime))

print(datetime.MAXYEAR) #Maior ano suportado

print(datetime.MINYEAR) #Menor ano suportado

print(datetime.datetime.now()) #Retorna data e hora 

#replace() para alterar data e hora
inicio = datetime.datetime.now()
print(inicio)
novo_inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(novo_inicio)

#receber dados do usuário e converter em data
nascimento = input('Informe sua data de nascimento (dd/mm/aaaa): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)

#Acessar individual dos elementos de data e hora
evento = datetime.datetime.now()
print(evento.year) #ano
print(evento.month) #mes
print(evento.day) #dia
print(evento.hour) #hora
print(evento.minute) #minutos
print(evento.second) #segundos
print(evento.microsecond) #microsegundos

#delta data e hora
delta = data_final - data_inicial
data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2024, 8, 3, 0)
tempo_para_evento = aniversario - data_hoje 
print(tempo_para_evento)

agora = datetime.datetime.now() #pode especificar timezone
hoje = datetime.datetime.today()

#Mudanças ocorrendo a meia-noite combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)

#Encontrar o dia da semana weekday()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())

#Formatando data/horas com strftime()
#dd/mm/aaaa hora:minuto
hoje = datetime.datetime.now()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

'''
import datetime






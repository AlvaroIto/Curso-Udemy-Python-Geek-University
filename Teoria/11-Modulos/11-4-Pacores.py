#Pacote

#Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos

#Pacotes -> É um diretório contendo uma coleção de módulos

#Importando pacote
from pacote import geek1, geek2 

#Importando subpacote
from pacote.pacote2 import geek3, geek4 

print(geek1.pi)
print(geek1.funcao1(4, 6))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())
print(geek4.funcao4())


#Importando módulo de um pacote
from pacote.geek1 import funcao1 
print(funcao1(4, 7))



'''
JSON -> JavaScript object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube...) e terceiros (nós desenvolvedores)


import json

class Gato:
    def __init__(self, nome, raca) -> None:
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-lata')
ret = json.dumps(felix.__dict__)
print(ret)

'''

#Integrando JSON com Pickle
# pip install jsonpickle no terminal

import jsonpickle

class Gato:
    def __init__(self, nome, raca) -> None:
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-lata')

#Escrever o arquivo json/pickle
with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
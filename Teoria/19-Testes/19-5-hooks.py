'''
hooks são os testes em si, ou seja, a execução dos testes

setup() - executado antes de cada método de teste. Util para criarmos instância de objetos e outros dados

teardown() - executado ao final de cada método de teste. Util para excluir dados ou fechar conexões com Banco de Dados


'''

import unittest

class ModuloTest(unittest.TestCase):
    def setUp(self) -> None:
        #Configurações do setup()
        return super().setUp()
    
    def tes_primeiro(self):
        #Setup vai rodar antes do teste
        #teardown() vai rodar após o teste
        pass
    
    def test_segundo(self):
        #Setup vai rodar antes do teste
        #teardown() vai rodar após o teste
        pass

    def tearDown(self) -> None:
        #Configurações do tearDown()
        return super().tearDown()
        pass


    
import unittest

from atividades import comer, dormir


class AtividadesTestes(unittest.TestCase):
    def test_comer_saudadel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma'
        )

    def test_comer_gostoso(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 hrs'
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Dormi muito! Estou atrasado para o trabalho!'
        )
if __name__ == '__main__':
    unittest.main()


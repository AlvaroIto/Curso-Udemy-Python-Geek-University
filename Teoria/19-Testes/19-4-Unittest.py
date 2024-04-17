'''
Unittest - Testes Unitários

Teste Unitário é a forma de se testar unidades individuais de código fonte.
Unidades individuais, podem ser: funções, métodos, classes, módulos, etc;

Para criar nossos testes, criamos classes que heradm de unittest. TestCase e a partir de então ganhamos todos os 'assertions' presentes no módulo
E para rodar os testes, utilizamos unittest.main()

Por convenção, todos os testes em um test case, devem ser iniciado com test_

Executar os testes no terminal:
python nome_do_modulo - v

Docstrings nos testes
Podemos acrescentar docstrings nos testes

Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Método                      Checa que
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               x é verdadeiro
assertFalse(x)              x é falso
assertIs(a, b)              a é b
assertIsNot(a, b)           a não é b
assertIsNone(x)             x é None
assertIsNotNone(x)          x não é None
assertIN(a, b)              a está em b
assertIsInstance(a, b)      a é isntância de b
assertNotIsInstance(a, b)   a não é instância de b

'''

'''
Doctests são testes que colocamos na docstring das funções/métodos Python.
Para rodar um test do doctest:

python - docstest -v nome_do_modulo.py

python -m doctest -v Teoria\19-Testes\19-3-Doctests.py
Trying:       
    soma(1, 2)
Expecting:
    3
ok
Trying:
    soma(4, 6)
Expecting:
    10
ok
1 items had no tests:
    19-3-Doctests
1 items passed all tests:
   2 tests in 19-3-Doctests.soma
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

def soma(a, b):
    #soma os números a e b
    #>>> soma(1, 2)
    #3

    #>>> soma(4, 6)
    #10
    
    #return a + b

#print(soma(4, 3)) #7

#Aplicando o TDD
############RED
def duplicar(valores):
    """duplica os valores em uma lista
    
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' anda 'NoneType'
    """
    pass



'''
#Aplicando o TDD

def duplicar(valores):
    """duplica os valores em uma lista
    
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]




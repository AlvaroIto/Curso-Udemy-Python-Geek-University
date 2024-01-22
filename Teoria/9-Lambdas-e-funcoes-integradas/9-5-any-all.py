"""
Any e All

All - Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio
Exemplo
print(all([0, 1, 2, 3, 4])) # False por causa do 0
print(all([1, 2, 3, 4, 5])) # True
print(all([])) # True

Any - Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna False
Exemplo
print(any([0, 1, 2, 3, 4])) #True
print(any([0, None, False, {}, (), []])) #False
print(any([0, None, False, {}, (), [], 1])) #True

"""






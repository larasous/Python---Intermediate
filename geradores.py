"""
Iterável, geradores e iteradores
"""
lista = [0,1,2,3,4]  # Objeto iterável
lista = iter(lista)  # Iterador

print(next(lista))  # Mostra um elemento

"""
for v in lista:  # Transforma a lista em iterador
    print(v)
"""

def gera():  # Gerador - não salva tudo na memória
    for n in range(100):
        yield n

g = gera()
for v in g:
    print(v)

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))

l1 = [x for x in range(100)]
print(type(l1))
l2 = (x for x in range(100))
print(type(l2))
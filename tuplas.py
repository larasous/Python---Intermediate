"""
Tuplas - não pode ser alterada, adicionar, remover
"""
t1 = (1, 2, 3, 'a')  # tupla () e lista []
print(t1[3])  # pode acessar por indíces

# iterar sobre tupla
for v in t1:
    print(v)

# fatiar (slices)
print(t1[:2])

t2 = 1,2,3,4,5
t3 = 6,7,8,9,10
t4 = t2 + t3  # concatenação de tuplas
print(t4)

# desempacotar 
n1, n2, n3, *_, n10 = t3
print(n10)

# repetir
t5 = (1,2) * 5
print(t5)

t5 = list(t5)  # converter para lista
print(type(t5))

lista1 = [2, 5, 6, 7]
lista1 = tuple(lista1)  # converter para tupla
print(type(lista1))
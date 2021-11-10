"""
Funções anônimas ou expressões lambda
"""
def func(arg, arg2):
    return arg * arg2

a = func(2, 10)
print(a)

b = lambda x, y: x * y  # Equivale a func
print(b(2, 10))

lista = [
    ['P1', 13],
    ['P2', 15],
    ['P3', 7],
    ['P4', 10],
    ['P5', 26]
]

# lista.sort(key=lambda item: item[1])  # Organizando pelo preço
print(sorted(lista, key=lambda i: i[1], reverse=True))  # Ordenando do maior para o menor preoço
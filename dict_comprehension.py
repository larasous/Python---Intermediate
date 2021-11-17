lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x: y for x, y in lista}
print(d1)

d2 = {a: b*2 for a, b in enumerate(range(5))}
print(d2)

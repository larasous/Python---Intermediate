l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [var for var in l1]
print(l2)

l3 = [n*2 for n in l2]
print(l3)

l4 = [(v, v2) for v in l1 for v2 in range(3)]
print(l4)

l5 = ['Luiz', 'Mauro', 'Maria']
l6 = [a.replace('a', '@') for a in l5]
print(l6)

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
l7 = [(y,x) for x, y in tupla]
print(l7)

l8 = list(range(100))
l9 = [v for v in l8 if not v % 2 if not v % 8]
print(l9)

l10 = [n if not n % 3 and not n % 8 else 0 for n in l8]
print(l10)
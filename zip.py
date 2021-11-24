"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

index = count()  # gerador
cidades = ['São Paulo', 'Salvador', 'Belo Horizonte', 'Monte Belo']
uf = ['SP', 'BA', 'MG']

cidade_uf = list(zip(index, uf, cidades))  # Retorna um iterador, vai até a menor lista

cidade2 = zip_longest(index, uf, cidades, fillvalue='Estado')  # Vai até a maior lista

for index, cidade, estado in cidade_uf:
    print(index, cidade, estado)
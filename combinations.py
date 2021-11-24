"""
Combinations, Permutactions e Products - Itertools
# Combinação - Ordem não importa
# Permutação - Ordem importa
Ambos não repetem valores únicos
# Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Ana', 'Sophia', 'Marcos', 'Joana', 'André']

print('COMBINAÇÃO')
for grupo in combinations(pessoas, 2):  # Combinação em grupo de 2
    print(grupo)

print("\nPERMUTAÇÃO")
for grupo in permutations(pessoas, 2): # Permutação em grupo de 2
    print(grupo)
    
print('\nPRODUTO')
for grupo in product(pessoas, repeat=2):  # Produto em grupo de 2
    print(grupo)
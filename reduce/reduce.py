from dados import pessoas, products, lista
from functools import reduce

# Acumulação de valores
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

total_preco  = reduce(lambda ac, i: ac + i['preco'], products, 0)
print(total_preco)

total_idade = reduce(lambda ac, i: ac + i['idade'], pessoas, 0)
print(total_idade)
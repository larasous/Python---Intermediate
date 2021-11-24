from dados import products, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)  # retorna um iterador
print(list(nova_lista)) # lista com os elementos multiplicados por 2

precos = map(lambda p: p['preco'], products)  # criar uma lista apenas com preços

for p in precos:
    print(p) 

# Aumentar o valor do preço em 5%
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

valor = map(aumenta_preco, products)

for v in valor:
    print(v) 

nomes = map(lambda p: p['nome'], pessoas)  # criar uma lista apenas de nomes
 
for pessoa in nomes:
    print(pessoa)
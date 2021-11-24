from dados import products, pessoas, lista

# filter retorna True ou False
""" nova_lista = filter(lambda x: x > 5, lista)  # retorna um iterador
print(list(nova_lista)) """

""" produto = filter(lambda x: x['preco'] > 50, products)
for p in produto:
    print(p)
     """
def filtra(p):
    if p['idade'] >= 18:
        return True

maior_idade = filter(filtra, pessoas)
for i in maior_idade:
    print(i)
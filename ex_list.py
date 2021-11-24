# Soma de compras no carrinho usando list comprehension

carrinho = []

carrinho.append(('Produto 1', '10'))
carrinho.append(('Produto 2', 30.50))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 70.5))
carrinho.append(('Produto 5', 20))

total = sum([float(p) for n, p in carrinho])
print(total)
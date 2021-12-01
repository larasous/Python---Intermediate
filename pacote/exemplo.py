# import vendas.precos  ->   vendas.precos.aumento()
# from vendas import precos  ->  precos.aumento
# Módulos - https://docs.python.org/3/tutorial/modules.html
from vendas.precos import aumento, reducao
from vendas.formata import format_preco

preco = 49.90
preco_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_aumento)

preco_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_reducao)

print(format_preco.real(preco))
"""
Dicionários - Suporta um par de chave (indíce) e valor
- Cada chave deve ter valor diferente
"""

# Criar dicionário
d1 = {'chave1': 12, 'nova_chave': 20}
d2 = dict(chave1=15, chave2=30)

d3 = {
    'str': 'valor',
    12: 'Outro valor',
    (1, 2, 3): 'Tupla',
}
print(d3[(1, 2, 3)])  # Acessa a tupla

d3.get('nomedachave')  # Verificar se a chave existe
del d3['str']  # Apagar a chave

for k in d3:  # Acessar as chaves
    print(k)

for v in d3.values():  # Acessar os valores
    print(v)

for i in d3.items():  # Acessar chaves e valores
    print(i)  # Acessar como tupla
    print(i[0], i[1])  # Acessar separado

v = d1  # Apontam para o mesmo endereço de memória
v['chave1'] = 'Luiz'  # Altera tanto em v quanto em d1
d1.pop('str')  # Apagar uma chave
d1.popitem()  # Apagar a última chave


# ----------------- Exemplo -------------------
clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio'
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes.items():
        print(f'\t{dados_k} = {dados_v}')

from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'B'},
    {'nome': 'Julia', 'nota': 'D'},
    {'nome': 'Bruna', 'nota': 'A'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Rosa', 'nota': 'A'},
    {'nome': 'Jose', 'nota': 'A'},
    {'nome': 'Sara', 'nota': 'A'},
]
ordena = lambda x: x['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
    
'''
# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  qtd = len(valores)
  print(f'\t{qtd} alunos tiraram nota {agrupamento}')
'''

# Com tee
for agrupamento, valores_agrupados in alunos_agrupados:
  v1, v2 = tee(valores_agrupados)

  print(f'Agrupamento: {agrupamento}')

  for aluno in v1:
    print(f'\t{aluno}')

  qtd = len(list(v2))
  print(f'\t{qtd} alunos tiraram nota {agrupamento}') 
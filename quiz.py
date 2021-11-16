"""
Sistema de Perguntas e Respostas com dicionários em Python
"""
LINHA = '--------------------------------'

perguntas = {
    'Pergunta 1': {
        'pergunta' : 'Quanto é 7+2^3/10? ',
        'respostas' : {'A': '1.5', 'B': '3.4', 'C': '7.8', 'D': '10'},
        'item_correto': 'C',
    },
    'Pergunta 2': {
        'pergunta' : 'Quanto é 3*2^2? ',
        'respostas' : {'A': '12', 'B': '24', 'C': '36', 'D': '40'},
        'item_correto': 'A',
    },
    'Pergunta 3': {
        'pergunta' : 'Quanto é 15*10/50? ',
        'respostas' : {'A': '3', 'B': '6', 'C': '9', 'D': '12'},
        'item_correto': 'A',
    },
    'Pergunta 4': {
        'pergunta' : 'Quanto é 10*23+50/2? ',
        'respostas' : {'A': '250', 'B': '255', 'C': '260', 'D': '265'},
        'item_correto': 'B',
    },
    'Pergunta 5': {
        'pergunta' : 'Quanto é 5*15 -(20+12/4)? ',
        'respostas' : {'A': '35', 'B': '42', 'C': '49', 'D': '52'},
        'item_correto': 'D',
    },
}
acertos = 0
for pk, pv in perguntas.items():
    
    print(LINHA)
    print(f'{pk}: {pv["pergunta"]}')
    print(LINHA)
    
    for rk, rv in pv['respostas'].items():
        print(f'({rk}): {rv}')
    print(LINHA)
    op = input('Opção escolhida: ').upper()
    if op == pv['item_correto']:
        print('Resposta correta!')
        acertos += 1
    else:
        print('Resposta errada!')

qtd = len(perguntas)
porcento = acertos / qtd * 100

if porcento <= 30.0:
    print(LINHA)
    print(f'Você acertou {acertos} perguntas!')
    print(f'Sua porcentagem foi de {porcento}%, estude mais um pouco')
elif porcento > 30.0 and porcento <= 50.0:
    print(LINHA)
    print(f'Você acertou {acertos} perguntas!')
    print(f'Sua porcentagem foi de {porcento}%, na média ein!')
else:
    print(LINHA)
    print(f'Você acertou {acertos} perguntas!')
    print(f'Sua porcentagem foi de {porcento}%, parabéns')
print(LINHA)
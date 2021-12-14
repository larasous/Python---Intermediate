import random

aux = []

def validar(cnpj):
    cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
    global aux
    aux = list(map(int, cnpj[:12]))

    try:
        digito(aux, 1)
        digito(aux, 2)
    except Exception as e:
        return False
    
    a = ''.join(map(str, aux))
    
    if a == cnpj:
        return 'CNPJ válido!'
    else:
        return 'CNPJ inválido!'


def digito(cnpj, dig):
    if dig == 1:
        i = 5
        count = 0
    elif dig == 2:
        i = 6
        count = 0
    else:
        return None

    soma = 0
    while count < len(aux):
        if i == 1:
            i = 9
        soma += cnpj[count] * i
        i -= 1
        count += 1

    try:
       
        digito_cnpj = 1 if 11 - (soma % 11) < 9 else 0
        aux.append(digito_cnpj)
        return digito_cnpj
    except:
        return False



def gera():
    dig1 = random.randint(0, 9)
    dig2 = random.randint(0, 9)
    bloco2 = random.randint(100, 999)
    bloco3 = random.randint(100, 999)
    bloco4 = '0001'

    
    inicio_cnpj = f'{dig1}{dig2}{bloco2}' \
        f'{bloco3}{bloco4}'
    
    global aux
    aux = list(map(int, inicio_cnpj))

    digito(cnpj=aux, dig=1)
    digito(cnpj=aux, dig=2)

    a = ''.join(map(str, aux))
    
    return formata(a)

def formata(cnpj):
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado
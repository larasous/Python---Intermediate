"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""
aux = []


def validar(cnpj):
    global aux
    aux = list(map(int, cnpj[:12]))

    try:
        digito(aux, 1)
        digito(aux, 2)
    except:
        return False
    
    a = ''.join(map(str, aux))
    
    if a == cnpj:
        return 'CNPJ Válido!'
    else:
        return "CNPJ Inválido!"


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
       
        digito = 1 if 11 - (soma % 11) < 9 else 0
        aux.append(digito)
        return True
    except:
        return False
    
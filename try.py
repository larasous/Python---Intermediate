"""
Usando try except como condicional
"""
def converte_num(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)      
            return valor
        except ValueError:
            pass


num = converte_num(input('Digite um numero: '))
if num is not None:
    print(num+5)
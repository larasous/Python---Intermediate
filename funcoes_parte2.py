"""
Funções (def) em Python (return) - Parte 2



def função(var):
    print(var)
    
a = função('Valor que eu quero')
print(a)  # mostra None pois a função não retorna nada


def func(msg):
    return msg

b = func('Olá mundo')
print(b) # mostra o retorno da função que será a mensagem
"""
def div(x, y):  # função para calcular a divisão entre 2 números
    
    if y == 0:  # tratamento de erro para uma divisão por zero
        return
    
    return x / y

a = div(8, 2)

if a:
    print(a) # mostra a divisão
else:
    print('Conta Inválida!') # mostra uma mensagem


def dumb():
    return ('Luiz', 'Otávio')  # retorna uma tupla

var = dumb()
print(var, type(var)) #
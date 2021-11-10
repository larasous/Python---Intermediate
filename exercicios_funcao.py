"""
1- Crie uma função1 que rebece uma função2 como parâmetro e retorne o valor da
função2 executada.
"""
def saudação():
    return 'Olá Usuário'

def func1(arg):
    return arg()

var = func1(saudação)
print(var)

"""
2 - Crie uma função1 que rebece uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""
def nome(nome):
    return f'Olá {nome}!'


def texto(nome, msg):
    return f'{nome} {msg}'


def func(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


teste = func(nome, 'Júlia')
teste2 = func(texto, nome('Maria'), 'Boa Noite')
print(teste)
print(teste2)

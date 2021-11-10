"""
Variáveis Globais podem ser reconhecidas no código todo
Variáveis Locais são reconhecidas apenas dentro do bloco de código
"""

variavel = 'valor'  # variavel global

def func():
    variavel = 1234 # variavel local
    print(variavel)
    
func()  # mostra a variavel local
print(variavel)  # mostra a variavel global


def f1():
    outra_variavel = 'Lara Amanny'
    return outra_variavel

def f2(arg):
    print(arg)
    
    
# Conectando duas funções
var = f1()
f2(var)
"""
Funções (def) Python - Parte 3 - *args **kwargs
"""
# kwargs são argumentos com palavras chaves (nomeados - dicionários)
def func(*args, **kwargs):  # args empacotados em uma tupla (não pode ser alterada)
    print(args)
    
    idade = kwargs.get('idade')  # verificar se uma chave foi passada
    
    if idade is not None:  # se a chave idade existir mostra na tela
        print(idade)
    else:
        print(idade)  # mostra None pois a chave idade não existe

lista = [1,2,3,4,5]
func(*lista, 10, 20, 30, 40, nome='Usuário', sobrenome='Miranda')

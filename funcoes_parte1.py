"""
Funções - def em Python (Parte 1)
"""

def saudacao(msg = 'Olá' , nome = 'Usuário'):  # parâmetros da função
    # bloco de comandos
    return f'{msg} {nome}'  # retorna o valor da função
    
saudacao('Oi', 'Maria')  # mostra os parâmetros passados na ordem do retorno da função
saudacao(nome='Lara', msg='Hello')  # pode atribuir visilmente os parâmetros
    
var = saudacao()  # recebe o retorno da função
print(var) # mostra na tela o retorno da função que está armazenado na variavel
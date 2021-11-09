"""
1 - Crie uma função que exibe uma saudação com os parâmetros: saudação e nome.
"""
def saudação(msg, nome):
    return f'{msg} {nome}'

print(saudação('Olá', 'Maria'))

"""
2 - Crie uma função que recebe 3 números como parâmetros e exibe a soma entre eles 
"""
def soma(n1, n2, n3):
    return n1+n2+n3

print(soma(10,-3,3))  # Mostra 10, pois -3 + 3 = 0

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual
(ex. 10%). Retorne o valor do primeiro número somado do aumento percentual
do mesmo. 
"""
def soma_percentual(num, percent):
    return num+(percent*num/100)

print(soma_percentual(10, 10))  # Mostra 11, pois 10% de 10 é 1, e 10 + 1 = 11

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se
o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função
for divisível por 5 e 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""
def fizzbuzz(x):
    if not x % 3 and not x % 5:
        return 'FizzBuzz'
    elif not x % 3:
        return 'fizz'
    elif not x % 5:
        return 'buzz'
    else:
        return x
    
print(fizzbuzz(15))  # Divisível por 3 e 5, portanto mostra FizzBuzz
print(fizzbuzz(2))  # Não é divisível 3 nem por 5, portanto mostra o próprio número
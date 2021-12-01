""" 
Formas de abrir e ler um arquivo
"""
import os

try:
    file = open('abc.txt', 'w+')
    file.write('Linha 1\n')  # write sobrescreve o arquivo, apagando tudo
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print("Lendo linhas:")
    print(file.read())  # lê o arquivo todo
    print("###########")

    file.seek(0,0)
    print(file.readline(), end='')  # lê o arquivo linha por linha
    print(file.readline(), end='')
    print(file.readline(), end='')
    print("###########")

    file.seek(0, 0)
    print(file.readlines()) # retorna uma lista com todas as linhas do arquivo
    print("###########")

    file.seek(0, 0)
    for linha in file.readlines():
        print(linha, end='')

finally:
    file.close
    
# Maneira mais pythonica
print("###########")
with open("abc.txt", "a+") as file:  # fecha o arquivo automaticamente
    # 'a+' faz o cursor ir diretamente para o final do arquivo, não apaga todo o arquivo
    file.write("Outra linha\n")
    file.seek(0)
    print(file.read())


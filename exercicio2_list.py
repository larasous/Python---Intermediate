"""
Considerando duas listas (int ou float) A e B.
Some os valores na lista retornando a soma em uma nova lista

Se uma lista for menor que a outra, a soma só vai considerar o
tamanho da menor.

Ex.:
lista_a = [1,2,3,4,5,6,7,8]
lista_b = [1,2,3,4]
----------------------------
soma = [2,4,6,8]
"""

lista1 = [1,2,3,4,5,6,7,8]
lista2 = [1,2,3,4]

soma = [i + j for i, j in zip(lista1,lista2)]
print(soma)
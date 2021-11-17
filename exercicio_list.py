"""
Separar em grupos de 0 a 9
"""
string = '012345678901234567890123456789012345678901234567890123456789'
aux = 10
lista = [string[i:i+aux] for i in range(0, len(string), aux)]
rt = '.'.join(lista)
print(rt)
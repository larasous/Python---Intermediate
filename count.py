"""
Count - Contadores infinitos (Itertools) retorna um iterador

from types import GeneratorType

var = zip('Alo', 'Alo')  # Retorna um iterador
print(isinstance(var, GeneratorType))  # Retorna false pois não é um gerador

var2 = ((x,y) for x, y in zip('ALO', 'ALO'))  # Retorna um gerador
print(isinstance(var2, GeneratorType)) # Retorna true pois não é um gerador

"""
from itertools import count

contador = count(start=5, step=5)  # Cuidado com o loop infinito

for i in contador:
    print(i)
    if i >= 20:
        break  # quebrar o loop infinito

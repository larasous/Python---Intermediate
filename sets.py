"""
Sets em Python
- add (adiciona)
- update (atualiza)
- clear
- discard (remover)
- union | (une)
- intersection & (todos os elementos presentes nos dois sets)
- difference (elementos apenas no set da esquerda)
- symmetric difference ^ (elementos que estão nos dois sets, mas não em ambos)
"""

# sets só recebem valores != do dicionário
# suportam somente elementos imutáveis
s1 = {1,2,3,4,5}  # criar set, se for somente {} -> dicionário
s2 = set()
s2.add(1)
s2.add(2)
s2.discard(2)  # remover o 2 do set

l1 = [1,2,3,1,1,1,2,2,2,6,6,6,]
l1 = set(l1)  # remover os elementos duplicados

s3 = {1,2,3,4,5,7}
s4 = {1,2,3,4,5,6,}
s5 = s3 | s4  # unir os dois sets
s6 = s3 & s4  # pegar os elementos presentes nos dois sets
s7 = s3 - s4  # pegar os elementos apenas do set da esquerda
s8 = s3 ^ s4  # pegar os elementos diferentes nos dois sets
print(s5)
print(s6)
print(s7)
print(s8)
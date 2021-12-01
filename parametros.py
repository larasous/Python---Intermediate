
def lista_clientes(clientes_iteravel, lista=[]):   # parametro mutavel lista
    lista.extend(clientes_iteravel)
    return lista


clientes = lista_clientes(['Ana', 'Joana'])
clientes1 = lista_clientes(['João', 'Maria', 'Eduarda'])
clientes2 = lista_clientes(['Mário', 'Bruno', 'Sara'])

# Por conta do parametro mutavel, as listas serão sempre iguais
print('Com problema.....\n')
print(clientes)
print(clientes1)
print(clientes2) 

print('\nResolvendo o problema.....\n')

def lista_clientes2(clientes_iteravel, lista=None):   # resolvendo o problema
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes3 = lista_clientes2(['João', 'Maria', 'Eduarda'])
clientes4 = lista_clientes2(['Mário', 'Bruno', 'Sara'])
clientes5 = lista_clientes2(['Ana', 'Joana'])

print(clientes3)
print(clientes4)
print(clientes5)
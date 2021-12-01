import math

PI = math.pi


def dobra_lista(lista: list):
    return [x*2 for x in lista]


def multiplica(lista: list):
    r = 1
    for x in lista:
        r *= x
    return r


if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
    print(__name__)  # retornar o nome do módulo apenas se este estiver sendo importado
from time import time, sleep

def velocidade(function):
    def interna(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        tempo = (end - start) * 1000
        print(f'\nA função {function.__name__} levou {tempo:.2f}ms para executar')
        return result
    return interna


@velocidade
def tempo():
    for i in range(100):
        print(i,end='')
        
        
tempo()
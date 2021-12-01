def master(function):  # função decoradora ( serve para add um recurso na função)
    def slave(*args, **kwargs):
        print('Agora estou decorada') 
        function(*args, **kwargs)
    return slave
 
 
@master  # decorador
def fala_oi():
    print('Oi')


@master
def outra_func(msg):
    print(msg)

fala_oi()
outra_func('Oi usuário') 
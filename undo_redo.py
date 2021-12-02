"""
Faça uma lista de tarefas com as seguintes opções:
    - Adicionar tarefa
    - Listar tarefa
    - Opção de desfazer (desfaz a última ação)
    - Opção de refazer (refaz a última ação)
"""
def menu():
    print('-------------------')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefa')
    print('3 - Desfazer (Undo)')
    print('4 - Refazer (Redo)')
    print('5 - Sair')
    print('-------------------')


def add(lista, tarefa):
    lista.append(tarefa)
    print('\nTarefa adicionada!\n')


def listar(lista):
    if not lista:
        print("\nLista sem tarefas\n")
    
    print('Tarefas:')
    for i, tarefa in enumerate(lista, 1):
        print(f'{i} - {tarefa}')
        
    print('\n')


def undo(lista, redo_list):
    if not lista:
        print("\nNada a desfazer\n")
        return
    
    last = lista.pop()
    redo_list.append(last)


def redo(lista, redo_list):
    if not redo_list:
        print('\nNada a refazer\n')
        return
    
    last = redo_list.pop()
    lista.append(last)

if __name__ == '__main__':
    list_tarefas = []
    redo_list = []
    
    while True:
        menu()
        op = input('Informe uma opção: ')
            
        if op == '1':
            print('-------------------')
            tarefa = input('Informe a tarefa: ').capitalize()
            add(list_tarefas, tarefa)
        elif op == '2':
            listar(list_tarefas)
        elif op == '3':
            undo(list_tarefas, redo_list)
        elif op == '4':
            redo(list_tarefas, redo_list)
        elif op == '5':
            print('Bye bye :)\n')
            break
        else:
            print('\nOpção Inválida!\n')
            menu()
            op = input('Informe uma opção: ')

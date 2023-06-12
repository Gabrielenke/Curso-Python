import os


todoList = []
repeat = True
lastInput = ''


def adicionar(acao, lista):
    lista.append(acao)
    return lista


while repeat:

    print('Comandos: List, Redo, Undo, Sair, Clear')
    inputTodo = input("Digite uma tarefa ou comando: ")
    print()

    if inputTodo.lower() == 'list':
        print(f'Tarefas: ', todoList)
    elif inputTodo.lower() == 'undo':
        todoList.pop()
    elif inputTodo.lower() == 'redo':
        todoList.append(lastInput)
    elif inputTodo.lower() == 'sair':
        repeat = False
    elif inputTodo.lower() == 'clear':
        os.system('cls||clear')

    else:
        adicionar(inputTodo, todoList)
        lastInput = inputTodo

# lista = [3, 31, 4, 32, 1, 65, 78, 88]
# lista.sort()
# print(lista)

lista = [
    {'nome': 'joao', 'idade': 25},
    {'nome': 'maria', 'idade': 27},
    {'nome': 'jose', 'idade': 28},
    {'nome': 'marcos', 'idade': 30},
    {'nome': 'maria', 'idade': 27},
    {'nome': 'jose', 'idade': 28},

]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['idade'])

exibir(l1)
exibir(l2)

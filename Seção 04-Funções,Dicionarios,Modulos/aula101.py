# map - mapear dados
from functools import partial


def printIter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55.55},
    {'nome': 'p3', 'preco': 5.59},
    {'nome': 'p4', 'preco': 22},
    {'nome': 'p5', 'preco': 81.23},

]


def mudaPreco(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto


def aumentarPorcentagem(valor, porcentagem):
    return round(valor * (porcentagem/100), 2)


novosProdutos = map(mudaPreco, produtos)
aumentarPreco = partial(aumentarPorcentagem)


printIter(produtos)
printIter(novosProdutos)

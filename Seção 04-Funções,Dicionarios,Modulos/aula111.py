# reduce - faz a reduçao de um iteravel para um unico valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},

]


# def funcReduce(total, produto):
#     return total + produto['preco']


# total = reduce(
#     funcReduce, produtos, 0
# )
# print(total)

total = reduce(
    lambda total, produto: total + produto['preco'], produtos, 0
)

# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco']for p in produtos]))

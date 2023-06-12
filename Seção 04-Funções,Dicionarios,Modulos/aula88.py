# lista = []
# for i in range(10):
#     lista.append(i)
# # print(lista)

# lista = [i for i in range(10)]
# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55.55},
    {'nome': 'p3', 'preco': 5.59},
]
novosProdutos = [
    {'nome': produto['nome'], 'preco': produto['preco'] * 1.05}
    for produto in produtos
]
# print(novosProdutos)
print(*novosProdutos, sep='\n')

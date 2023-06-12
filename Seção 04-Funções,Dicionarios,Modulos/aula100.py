import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novosProdutos = [{'preco': round(produto['preco'] * 1.1, 2)}
                 for produto in copy.deepcopy(produtos)
                 ]
produtosOrdenadosNome = sorted(
    produtos, key=lambda produto: produto['nome'], reverse=True)
produtosOrdenadosPreco = sorted(produtos, key=lambda produto: produto['preco'])

print(*produtos, sep='\n')
print()
print(*novosProdutos, sep='\n')
print()
print(*produtosOrdenadosNome, sep='\n')
print()
print(*produtosOrdenadosPreco, sep='\n')

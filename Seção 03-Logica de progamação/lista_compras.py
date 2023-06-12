listaCompras = ['maça', 'banana', 'laranja', 'uva', 'abacaxi']
adicionarItem = input('Digite o item que deseja adicionar a lista: ')

if adicionarItem in listaCompras:
    print('O item ja esta na lista de compras')
    print(listaCompras)

else:
    listaCompras.append(adicionarItem)
    print("Item adicionado com sucesso")
    print(listaCompras)

removerItem = input('Digite o item que deseja remover da lista: ')

if removerItem in listaCompras:
    listaCompras.remove(removerItem)
    print('Item removido com sucesso')
    print(listaCompras)
else:
    print('O item não foi removido da lista de compras,pois nao esta na lista')
    print(listaCompras)

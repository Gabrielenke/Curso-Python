def adcionaClients(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


clientes1 = adcionaClients('Luiz')
adcionaClients('Maria', clientes1)
print(clientes1)


clientes2 = adcionaClients('jao')
adcionaClients('gabriel', clientes2)
print(clientes2)

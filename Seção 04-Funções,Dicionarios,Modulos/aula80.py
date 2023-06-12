# ''''''''
# exercicio
# Crie uma função que encontra o primeiro duplicado considerando o segundo numero como a duplicação.
# Requisitos:
# A ordem do numero duplicado é considerada a partir da segunda ocorrencia do numero, ou seja, o numero duplicado em si.
# Exemplo: [1,2,3,3,2,1] retorna 3
# Exemplo: [1,2,3,4,5,6] retorna None
# ''''''''

lista_de_listas_de_inteiros = [
    [1, 2, 3, 3, 2, 1],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3, 2, 1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]


def encontraDuplicado(listaInteiros):
    numerosChecados = set()
    primeiroDuplicado = -1

    for i in listaInteiros:
        if i in numerosChecados:
            primeiroDuplicado = i
            break

        numerosChecados.add(i)

    return primeiroDuplicado


for lista in lista_de_listas_de_inteiros:
    print(lista, encontraDuplicado(lista))

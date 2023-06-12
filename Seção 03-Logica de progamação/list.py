# arr = [1, 2, 3, 4, 5,]
# arr.append(50)
# arr.append(70)
# arr.append(80)
# arr.append(90)
# arr.append(40)
# arr.append(10)
# arr.pop()
# print(arr)

# listaA = [1, 2, 3]
# listaB = [4, 5, 6]
# listaC = listaA + listaB
# listaA.extend(listaB)
# print(listaA)
# print(listaC)

lista = ['gabriel', 'joao', 'maria', 'pedro',
         'jose', 'ana', 'julia', 'marcos', 'jorge', 'ju']

for nome in lista:
    print(lista.index(nome) + 1, end=' - ')
    print(nome)

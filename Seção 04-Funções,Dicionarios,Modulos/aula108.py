
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [2, 4, 6, 8, 9, 2, 5]

# for i in range(len(lista1)):
#     res.append(lista1[i]+lista2[i])
# print(res)

res = [x+y for x, y in zip(lista1, lista2)]
print(res)

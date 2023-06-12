from itertools import count, combinations, permutations, product, repeat

# c1 = count()
# r1 = range(10)

# print('c1', hasattr(c1, '__iter__'))
# print('r1', hasattr(r1, '__iter__'))
# print('c1', hasattr(c1, '__next__'))
# print('r1', hasattr(r1, '__next__'))

# for i in c1:
#     print(i)
#     if i >= 10:
#         break


def printIter(iter):
    for i in iter:
        print(i, end='\n')
    print()


pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
camisetas = [['branca', 'preta'],
             ['p', 'm', 'g'],
             ['masculino', 'feminino']]
printIter(combinations(pessoas, 2))
printIter(permutations(pessoas, 3))
printIter(product(*camisetas))

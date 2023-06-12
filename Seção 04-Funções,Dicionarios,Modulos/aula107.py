# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
import itertools


# def zipper(l1, l2):
#     maxInterval = (min(len(l1), len(l2)))
#     return [
#         (l2[i], l1[i]) for i in range(maxInterval)
#     ]


l1 = ['BA', 'SP', 'MG', 'RJ']
l2 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# print(zipper(l1, l2))

print(list(zip(l1, l2)))

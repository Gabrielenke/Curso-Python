# import sys

# generator = (n for n in range(1000))
# print(sys.getsizeof(generator))
# print(type(generator))
# for n in generator:
#     print(n)

def generator(x):
    for n in range(x):
        yield n  # pausa a funcao e retorna o valor


gen = generator(100)
for n in gen:
    print(n)

def executa(funcao, *args):
    return funcao(*args)


print(executa(
    lambda x, y: x * y, 4, 5
))

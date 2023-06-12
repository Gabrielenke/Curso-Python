x = 1


def escopo():
    global x
    x = 11
    y = 2
    print(x, y)


print(x)
escopo()

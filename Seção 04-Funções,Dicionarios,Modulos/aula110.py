from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'B'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'D'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'B'},
]


def ordena(aluno):
    return aluno['nota']


alunosAgrupados = sorted(alunos, key=ordena)

grupos = groupby(alunosAgrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)

    for aluno in grupo:
        print(aluno)

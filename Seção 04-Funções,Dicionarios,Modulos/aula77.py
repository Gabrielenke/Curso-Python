perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2? ',
        'opçoes': [1, 2, 3, 4],
        'resposta':'4'
    },
    {
        'pergunta': 'Quanto é 5* 5? ',
        'opçoes': [25, 50, 10, 51],
        'resposta': '25'
    },
    {
        'pergunta': 'Quanto é 10/2 ? ',
        'opçoes': [5, 8, 2, 4],
        'resposta': '5'
    },
]

respostas_certas = 0
respostaDigite = ''
for pergunta in perguntas:
    print(pergunta['pergunta'])
    print(pergunta['opçoes'])

    respostaDigite = input("Digite a opçao correta:")

    print(respostaDigite)

    if (respostaDigite == pergunta['resposta']):
        print("VOCE ACERTOU")
    else:
        print('Resposta errada')

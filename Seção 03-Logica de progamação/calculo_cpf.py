import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0, 9))

# calculo do primeiro digito
noveDigitos = cpf[:9]
resultado = 0
resultado2 = 0
contagemRegressiva = 10
contagemRegressiva2 = 11

for digito1 in noveDigitos:
    resultado += int(digito1) * contagemRegressiva
    contagemRegressiva -= 1

digito1 = (resultado*10) % 11
if digito1 > 9:
    digito1 = 0


# CALCULO DO SEGUNDO DIGITO
dezDigitos = noveDigitos + str(digito1)

for digito2 in dezDigitos:
    resultado2 += int(digito2) * contagemRegressiva2
    contagemRegressiva2 -= 1

digito2 = (resultado2 * 10) % 11

if digito2 > 9:
    digito2 = 0

cpf = dezDigitos + str(digito2)

print(cpf)

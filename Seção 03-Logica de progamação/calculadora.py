num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
operador = input("Digite o operador que quer usar: (+,-,/,*) : ")


if operador == '+':
    print(num1+num2)
elif operador == '-':
    print(num1-num2)
if operador == '/':
    print(num1/num2)
if operador == '*':
    print(num1*num2)
else:
    print("Voce digitou alguma informaçao incorreta")

nome = str ( input ('Digite seu nome: '))
n1 = float (input ('Digite sua primeira nota: '))
n2 = float (input ('Digite sua segunda nota: '))
n3 = float (input('Digite sua terceira nota: '))

mediafinal = float (n1*2 + n2*3 + n3*5)/10

if (mediafinal < 4.9):
    print(f"{nome} Você foi reprovado!): com media: {mediafinal: .2f}")
elif (mediafinal >= 5 and mediafinal <=6.9):
    print(f"{nome}Você está em recuperação, com media: {mediafinal: .2f}")
elif (mediafinal >= 7):
    print(f"{nome} você foi aprovado, com media: {mediafinal: .2f}")
else:
    print('numero invalido')
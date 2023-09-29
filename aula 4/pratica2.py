perguntas = []
cont = 0

print ('Responda com S ou N abaixo:')
perguntas.append(str(input('Conhece a vitima do furto? [S] ou [N]')))
perguntas.append(str( input('Esteve no local do furto? [S] ou [N]')))
perguntas.append(str(input('Morta perto da vitima? [S] ou [N]')))
perguntas.append(str(input('A vítima lhe devia? [S] ou [N]')))
perguntas.append(str(input('Já trabalhou com a vítima? [S] ou [N]')))

print(perguntas)

for resposta in perguntas:
    if resposta == 's':
        cont +=1

if cont == 2:
    print('Pessoa suspeita')
elif (cont == 3 or (cont ==4)):
    print('pessoa cumplice')
elif cont == 5:
    print('ladrão')
else:
    print ('pessoa inocente')
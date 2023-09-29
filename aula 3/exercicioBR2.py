#Foi realizada uma pesquisa de algumas características físicas de 5 alunos de um
#curso, a qual coletou os seguintes dados referentes a cada pessoa para serem
#analisados:
#sexo (masculino e feminino)
#cor dos olhos (azuis, verdes ou castanhos)
#cor dos cabelos ( louros, castanhos, pretos)
#idade
#
#Faça um algoritmo que determine e escreva:
#a) a quantidade de pessoas do sexo feminino cuja idade está entre 18 e 35;
#b) a quantidade de pessoas que têm olhos castanhos e cabelos pretos.
feminino = 0
caracteristicas = 0 
cabelo_preto = 0
for i in range (2):
    sexo = str(input('Qual seu sexo: (m) ou (f)'))
    olhos = int (input('Qual a cor dos seus olhos? [1]azul [2]verde [3]castanho '))
    cabelos = int(input('Qual a cor do seu cabelo? [1]louro [2]castanho [3]preto '))
    idade = int(input('Qual sua idade? '))

    #a) a quantidade de pessoas do sexo feminino cuja idade está entre 18 e 35;
    if ((sexo=='f') and (idade >=18 and idade <= 35 )):
        feminino +=1
    

    #b) a quantidade de pessoas que têm olhos castanhos e cabelos pretos.
    if((olhos == 3) and (cabelos == 3)):
        caracteristicas+=1


print(f'quantidade de mulheres: {feminino} e a quantidade de olhos castanhos: {caracteristicas}')     

#Sua missão é auxiliar os atletas da School, escreva um programa que receba o nome e o tempo (em minutos) 
#de três voltas de 5 corredores e armazene tais tempos em um dicionário, onde a chave é o nome do corredor, 
#e os valores são os minutos de cada volta. Por fim, deverá ser mostrado a média (com três casas decimais) 
#de tempo de cada corredor e o nome (todo em maiúsculo) do corredor que obteve a menor média.

corredores = {}

for i in range(5):
    nome = input(f'Digite o nome do corredor: {i+1}: ')
    tempos = []

    for j in range (3):
        tempo = int(input('Digite o tempo {i+1} do corredo: '))
        tempos.append(tempo)
    corredores[nome] = tempos

medias = {}

for nome, tempos in corredores.items():
    media = sum(tempos)/3
    medias[nome] = round(media,3) #round() faz um arredonamento

melhor_corredor = min(medias, key=medias.get)
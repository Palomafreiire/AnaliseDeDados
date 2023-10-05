#Crie um programa que utilize o NumPy para realizar análises específicas 
#sobre as notas, como calcular a média das notas dos três primeiros alunos e 
#verificar quais alunos tiraram notas acima de 7.

import numpy as np

notas = []

for i in range(6):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas.append(nota)

#converte lista em array
notas = np.array(notas)

#calcula a media
media_estudantes = np.mean(notas[:3])

#filtra por notas acima de sete
medias_acima_sete = notas[notas>=7]

print(notas)
print(f'A media dos tres primeiros estudantes: {media_estudantes: .2f}')
print(f'Media acima de 7 {medias_acima_sete}')




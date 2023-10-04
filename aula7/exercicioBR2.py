#Crie um programa que utilize arrays com NumPy para armazenar os dados de temperatura média diária 
#de uma cidade nos últimos sete dias e calcule a temperatura média e a temperatura máxima e mínima 
#registrada nesse período.

import numpy as np

diaria = np.array([25, 27, 39, 40, 42, 28, 30])

media_diaria = np.mean(diaria)
print(f'A media diaria foi: {media_diaria}')

temp_maxima = np.max(diaria)
print(f'A temperatura maxima foi de: {temp_maxima}')

temp_minima = np.min(diaria)
print(f'A temperatura minima foi: {temp_minima}')



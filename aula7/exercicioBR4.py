#Crie um programa que utilize o NumPy para calcular a média de vendas nos primeiros 10 dias 
#e verificar se houve algum dia em que as vendas foram maiores que 1000.

import numpy as np

vendas = []

for i in range(10):
    valor_vendas = float(input(f'Qual o valor das vendas de hoje {i+1}: '))
    vendas.append(valor_vendas)


vendas = np.array(vendas)
media_vendas = np.mean(vendas[:10])

media_acima_mil = vendas[vendas > 1000]

print(vendas)
print(media_vendas)
print(media_acima_mil)

    

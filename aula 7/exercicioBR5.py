#Crie um programa que utilize o Broadcasting do NumPy para converter 
#as temperaturas registradas em graus Celsius  para Fahrenheit e Kelvin. 

import numpy as np

temperaturas = np.array([25.0, 30.0, 35.0, 20.0])

temperatura_fahrenheit = (temperaturas * 9/5) + 32

temperatura_kelvin = temperaturas + 273.15

print('A temperatura em graus Celsius: ', temperaturas)
print('A temperatura em Fahrenheit: ', temperatura_fahrenheit)
print('A temperastura em Kelvin: ', temperatura_kelvin)

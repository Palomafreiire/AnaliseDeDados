#Escreva um programa que leia três valores com ponto flutuante: 
#A, B e C. Em seguida, calcule e mostre:

a = float(input ('Valor de A: '))
b = float(input ('Valor de B: '))
c = float(input ('Valor de C:'))

#a área do triângulo retângulo que tem o 
# valor de A como base e o valor de C como altura.

area_triangulo = (a * c) / 2

print(f'A area triangulo retangulo com base A e altura C é: {area_triangulo}')

# Calcula e mostra a área do círculo com raio C

import math

area_circulo = math.pi * (c ** 2)
print(f'A area do circulo é: {area_circulo: .2f}')

# Calcula e mostra a área do trapézio com A e B como bases e C como altura

area_trapezio = ((a + b) * c)/2
print(f'A area do trapezio é: {area_trapezio}')

# Calcula e mostra a área do quadrado com lado B

area_quadrado = b **2
print(f'A area do quadrado é: {area_quadrado}')

# Calcula e mostra a área do retângulo com lados A e B
area_retangulo = a * b
print(f'A area do retangulo é: {area_retangulo}')
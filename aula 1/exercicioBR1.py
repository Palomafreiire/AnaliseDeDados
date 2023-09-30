#Desenvolva um programa que leia a largura e altura de uma parede, 
#calcule e mostre a área a ser pintada e a quantidade de tinta necessária 
#para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados (m²).

altura = float(input('Qual a altura da sua parede? '))
largura = float(input('Qual a largura da sua parede? '))

#calcula a area a ser pintada
area = (largura * altura) 

# calcula a quantidade de tinta necessaria:
quantidade_tinta = area/2

print(f'A area a ser pintada é {area} metros quadrados')
print(f'Qual a quantidade de tinta necessária para o serviço {quantidade_tinta} litros.')
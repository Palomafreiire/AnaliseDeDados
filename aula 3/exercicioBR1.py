#Faça um programa que peça 10 numero inteiros, calcule e mostre quanto
#desses numeros são pares e quantos impares
numero_par = 0
numero_impar = 0
for i in range (10):
    numero = int(input('Digite um numero inteiro: '))

    if(numero%2 == 0):
        print('Esse é um numero par')
        numero_par+=1
    else:
        print('Esse é um numero impar')
        numero_impar+=1


print (f'existe numeros par: {numero_par} e numeros impar: {numero_impar}')


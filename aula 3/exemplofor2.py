numero = int (input ('Digite um numero: '))
soma = 0

# i vai representar os divisores do numero
for i in range(1, numero):
    
    if(numero % i == 0):
        soma+=i

if numero==soma:
    print("é um numero perfeito")
else:
    print("ele não é um numero perfeito")



print('Você saiu da execução')
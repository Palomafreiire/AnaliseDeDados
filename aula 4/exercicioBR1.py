#Desenvolva um programa que possua dois vetores/listas (A e B) 
#de 5 elementos cada (o usuário insere os valores nos dois vetores). 
#Crie um terceiro vetor (C) que seja a 
#união entre os 2 vetores anteriores, ou seja, que contém os números dos 
#dois vetores. Após isso, apresente: 


a = []
b = []

for i in range (5):
    a.append(int (input('Digite os valores da lista A: ')))
    b.append(int (input('Digite os valores da lista B: ')))

c = a+b #adiciona os valores de A e B na lista 
print(c)
soma_pares =0
media_impares=0
soma_impares=0
qtd_impares=0

for final in c:
    if final%2 ==0:
        soma_pares+=final #soma_pares = soma_pares + final
    else:
        qtd_impares+=1 #qtd_impares  = qtd_impares +1
        soma_impares+=final #soma_impares = soma_impares + final

print(f'Soma dos numeros pares {soma_pares}')
print(f'A media dos numeros impares {media_impares}')
print(f"O Menor valor de C {min(c)}")
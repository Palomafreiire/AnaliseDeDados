arquivo = open('exercicio2BR.txt', 'w')

valor = []
contador = 0 


for i in range(10):
    valor.append(input ('Escreva o valor: '))


arquivo.writelines("\n".join(valor))

arquivo.close()

for i in range((len(valor))):
    if valor[i]>valor[i-1]:
        contador+=1

print('A quantidade de profundidade maior que a anterior: ', contador)

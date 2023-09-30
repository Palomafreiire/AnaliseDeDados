#Desenvolva um programa para calcular a redução do tempo de vida de um fumante. 
#Pergunte a quantidade média de cigarros fumados por dia e por quantos anos ele já fumou. 
#Considere que um fumante perde 10 min de vida a cada cigarro.  
#Calcule e exiba quantos dias de vida o fumante perdeu até o momento

media_cigarros = int(input('Quantidade media de cigarros fumados por dia: '))
anos = int (input('Quantos anos você fuma: '))

total_cigarros = media_cigarros * 365 * anos

minutos_perdidos = total_cigarros * 10

dias_perdidos = minutos_perdidos / (60*24)

anos_perdidos = dias_perdidos / 365

print(f'Você perdeu aproximadamente {dias_perdidos: .2f} dias de vida')
print(f'Você perdeu {anos_perdidos} anos de vida')



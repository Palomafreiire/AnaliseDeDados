from datetime import date
anoAtual = date.today().year
maior_idade = 0
menor_idade = 0
idade = 0


for i in range (5):
    ano_nascimento = int (input('Que ano você nasceu? '))

    idade= anoAtual - ano_nascimento

    if(idade >= 18):
        print(f'Você tem {idade} então é maior de idade')
        maior_idade+=1 #para saber quantas pessoas são maiores de idades
    else:
        print(f'você tem {idade} então é menor de idade')
        menor_idade+=1 #para saber quantas pessoas são menor de idades


print (f'Nesse progama são {maior_idade} pessoas maiores de idade e {menor_idade} pessoas são menores de idade!')
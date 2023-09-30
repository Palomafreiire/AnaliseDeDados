#Desenvolva um programa que receba o nome de um ciclista, a distância 
#que ele percorreu em Km e o tempo que ele gastou nesse percurso, em horas.  
#O programa deverá calcular a velocidade média do ciclista e, exibi-la na tela 
#duas vezes, uma em Km/h e a outra em m/s. Dividimos por 3,6 quando queremos 
#converter Km/h para m/s.

nome_ciclista = input('Qual é seu nome? ')
distancia_pecorrida = float(input('Qual a distancia que vocÊ pecorreu em KM: '))
tempo_gasto = float(input('Quanto tempo você fez esse percurso em horas: '))

velocidade_mediakm = tempo_gasto / distancia_pecorrida
velocidade_mediams = velocidade_mediakm / 3.6

print(f'A velocidade do {nome_ciclista} em KM foi de {velocidade_mediakm: .4f} e em metros deu: {velocidade_mediams: .4f}')
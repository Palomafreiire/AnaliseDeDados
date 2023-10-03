def media_num(num1, num2):
    media = (num1+num2)/2
    return media

altura1 = float(input('Digite a altura de 1: '))
altura2 = float(input('Digite a altura de 2: '))

resultado = media_num(altura1, altura2)
print(f'a media das alturas foi {resultado: .2f2}')


#FUNÇÃO
# GARANTIR TRES CARACTERISTICAS:
# 1 TIPO
# 2 QUANTIDADE
# 3 ORDEM

#VARIAVEIS:
# ela é considerada global quando sua declaração acontece no algoritmo principal.
# a local é considerada quando sua declaração acontece em um subprograma(função ou procedimento)

#VARIAVEIS GLOBAIS:
# inicializada/utilizada no algoritmo principal
# todos os subprogramas podem utilizar a variavel global

#VARIAVEIS LOCAIS:
# inicializada/utilizada na função
# somente a função pode utiliza-la
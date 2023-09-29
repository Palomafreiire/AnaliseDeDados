#chave é separada por {}
agenda = {'pedro':9198928392}

#metodo get()
print(agenda.get('ana', 'não encontrado'))
print(agenda.get('pedro', 'não encontrado'))

#metodo pop()
#além de remover o elemento com a chave especificada do dicionarios
#nos retorna o valor desse elemento


#exemplo1
dicionario = {}
numero = int(input('escolha o valor que quer a multiplicação: '))

for i in range(0, numero+1, 1): #se não colocar o +1 o range não considera o ultimo numero
    dicionario[i] = i*i

print(dicionario)

#comando items()
#retorna uma lista com todos os itens (chave/valor)

#comando keys()
#retorna uma lista com todas as chaves do dicionario

#comando values()
#retorna todos os valores
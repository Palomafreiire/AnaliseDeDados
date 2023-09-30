arquivo = open('exemplo4.txt', 'w')

dados = []

for i in range(5):
    dados.append(input('Digite o nome do voluntario: '))
    

arquivo.writelines("\n".join(dados)) #join transforma uma lista em uma string

arquivo.close()

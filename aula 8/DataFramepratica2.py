import pandas as pd

# Utilizando uma lista de listas para montar 
#um DataFrame com várias colunas:


estados_nordestes = [
    ['alagoas', 'AL', '3.4 milhões', "Maceio"],
    ['Bahia', 'BA', '15,4 milhoes', 'salvador'],
    ['Ceara', 'CE', '9,2 milhoes', 'Fortaleza'],
    ['Maranhão', 'MA', '7,1 milhoes', 'São Luis'],
    ['Paraiba', 'PB', '4 milhoes', 'Joao pessoa'],
    ['Pernambuco', 'PE', '4 milhoes', 'Recife'],
    ['Piaui', 'PI', '3,3 milhoes', 'Teresina'],
    ['Rio Grande do Norte', 'RN', '3,5 milhões', 'Natal'],
    ['Sergipe', 'SE', '2,4 milhões', 'Aracaju']
]

# Fazendo as colunas do DataFrame
df = pd.DataFrame(estados_nordestes, columns=['Estado', 'Sigla', 'População', 'Capital'])

#adicionar uma informação na lista
idh =  [0.631, 0.631, 0.631, 0.631, 0.631, 0.631, 0.631, 0.631, 0.631]

# dentro do DataFrame eu to criando uma coluna e adicionado as infomação na lista ja existente
df['IDH'] = idh

print(df)

# exibir apenas uma coluna 
print(df[['Estado', 'Sigla']])


# exibir uma linha toda:
print(df.loc[2])

#exibir de a linha até outra linha
print(df.loc[2:4])

#exibir as primeiras posições
print(df.loc[:6])

# exibir a posição apenas das colunas que quero
print(df.loc[2:4,['Estado', 'Sigla']])

# o comando ILOC separa a linha / coluna
# comando é a seleção baseada em posição inteira
#posição entre linha e coluna, em vez de rotulos(nomes) feito bota em LOC
print(df.iloc[1:4, 0:3])
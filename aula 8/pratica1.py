import pandas as pd

# CRIANDO UM DATAFRAME A PARTIR DE UM DICIONARIO

dados = {
    'Nome' : ['Taty', 'maria', 'Paloma'],
    'Cidade': ['recife', 'Fortaleza', 'João pessoa'],
    'Idade': [37, 30, 29],
    'Telefone': ['(81)9999-9999', '(81)9999-9990', '(81)9990-9990']
}

# CRIAR DATAFRAME
df = pd.DataFrame(dados)

print(df)
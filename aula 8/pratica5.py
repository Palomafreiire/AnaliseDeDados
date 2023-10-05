import pandas as pd

# SUBTRAÇÃO DE COLUNAS

data = {
    'a': [10, 20, 30],
    'b': [5, 15, 25],
    'c': [2, 4, 6]
}

df = pd.DataFrame(data)
df['Subtracao_a_c'] = df['a'] - df['c']
print(df)
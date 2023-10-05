import pandas as pd

# um dicionario de valores de vendas ja existentes
vendas = {
    'Produto': ['Smartphone', 'Laptop', 'Tablet', 'Fone de ouvido', 'Smart TV'],
    'Quantidade': [100, 50, 80, 120, 30],
    'Preço unitario': [800, 2500, 600, 80, 1800]
}

df_vendas = pd.DataFrame(vendas)

#calcular a receita total para cada produto e adicionar uma nova coluna 'receita'

df_vendas['Receita'] = df_vendas['Quantidade'] * df_vendas['Preço unitario']
print(df_vendas)

#produtos que vendeu mais de 80 unidades
produtos_oitenta = df_vendas[df_vendas['Quantidade'] > 80]
print(produtos_oitenta)

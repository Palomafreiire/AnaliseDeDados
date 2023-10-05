import pandas as pd

#OPERAÇÕES ARITMETICAS COM PANDAS

data = {
    'num1': [10, 20, 30],
    'num2': [5, 15, 25]
    
}
df_numeros = pd.DataFrame(data)

#SOMA
df_numeros['soma'] = df_numeros['num1'] + df_numeros['num2']

#SUBTRAÇÃO
df_numeros['sub'] = df_numeros['num1'] - df_numeros['num2']

#MULTIPLICAÇÃO
df_numeros['mult'] = df_numeros['num1'] * df_numeros['num2']

#DIVISÃO
df_numeros['div'] = df_numeros['num1'] / df_numeros['num2']

print(df_numeros)




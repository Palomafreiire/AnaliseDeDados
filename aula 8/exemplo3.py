import pandas as pd

dados_alunos = {
    'Nome': ['Paloma', 'Camyla', 'Karol'],
    'nota1': [8.5, 7.8, 6.5],
    'nota2': [6.0, 1.2, 9.2]
}

df_estudantes = pd.DataFrame(dados_alunos)
df_estudantes['Media'] = df_estudantes[['nota1', 'nota2']].mean(axis=1) # o axis é para pegar a 1a nota com a 2a nota, posição de linha por linha igual
df_aprovados = df_estudantes[df_estudantes['Media'] >=7]
print(df_aprovados[['Nome', 'Media']])

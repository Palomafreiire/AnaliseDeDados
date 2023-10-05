import pandas as pd

#fazendo um dicionario dos dados existentes de estudantes

estudantes = {
    'Nome': ['Paloma', 'Camyla', 'Sandrelly', 'Karol', 'Deborah' ],
    'Idade': [29, 30, 22, 28, 27],
    'Media': [8.5, 7.8, 9.2, 6.5, 8.9]

}

df_alunos = pd.DataFrame(estudantes)
# adicionando coluna status
status = ['aprovado', 'aprovado', 'aprovado', 'reprovado', 'aprovado']
df_alunos['Status'] = status

print(df_alunos)


#selecionando apenas os estudantes aprovados:
df_aprovados = df_alunos[df_alunos['Status'] == 'aprovado']
print(df_aprovados)



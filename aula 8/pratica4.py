import pandas as pd

dados_alunos = []

for i in range(3):
    nome = input ('Qual é seu nome: ')
    disciplina = input('Nome da disciplina: ')
    nota = float(input('Insira a nota do aluno: '))
    dados_alunos.append({'Nome': nome, 'Disciplina': disciplina, 'Nota': nota})

df = pd.DataFrame(dados_alunos)
print(df)
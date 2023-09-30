arquivo = open('exemplo3.txt', 'w')

disciplina = input ("Qual a disciplina você está cursando: ")
turma = input ("qual sua turma: ")

arquivo.write(disciplina + '\n')
arquivo.write(turma)

print(arquivo) # não consegue ver no console pq o arquivo está com o comando w (write)

arquivo.close()

arquivo = open('exemplo3.txt', 'r')

print(arquivo.read())
arquivo.close() #se abrir duas vezes, tem que fechar duas vezes
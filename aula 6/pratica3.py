def media_aluno (n1,n2):
    media = (n1+n2)/2 #exemplo de variavel local
    return media


def status_aluno (media):
    if media > 6:
        print('Aluno aprovado')
    elif media >= 4 and media_aluno <= 6:
        print('Verificação suplementar')
    else:
        print('Reprovado')



nota1 = float(input('Digite sua primeira nota: ')) #exemplo de variaveis globais
nota2 = float(input('Digite sua segunda nota: '))

    
print (f'a media do aluno ficou em: {media_aluno(nota1,nota2)}')

resultado = media_aluno(nota1, nota2)
status_aluno(resultado)


texto = 'sorria hoje é sexta'

print(texto[::-1]) #de tras para frente
print(texto[0]) #primeira letra


#contatenação de String:
#existem varias formas:

nome= "irineu"
sobrenome = "você não sabe nem eu"

print(f'{nome}, {sobrenome}')
print(nome, sobrenome)
print(nome + ", " + sobrenome)
print('{}, {}'.format(nome,sobrenome))

#COMANDOS:

#String: Troca de palavras
#replace()

texto = "Sorria! hoje é sexta"
novo_texto =  texto.replace("Sorria", "Força") #cria uma nova string para alterar, pq não consegue alterar a original
print(novo_texto)

#COMANDOS:
#len() : tamanho da string
#find() : para encontrar ocorrencias em uma string
#upper() : converter a string para maiusculo e 
#lower() : para minusculo
#capitalize() : converte apenas a primeira letra da string em maiusculo
#tittle() : converter a primeira letra de todas as palavras de uma string em maisculo

frase = input('digite uma frase: ').upper() #pode ser assim ou individual feito embaixo
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(len(frase))

#COMANDOS:
texto = "Você é linda demais"
print(texto.split(" ")) #espaço
print(texto.split("@")) #posso botar qualquer separador ou nenhum


#lstrip() : remover espaços em branco na esquerda

alunos = ['maria', 'João', 'ana']
print(alunos)
print(", ".join(alunos)) #unir a string
print(' - '.join(alunos))

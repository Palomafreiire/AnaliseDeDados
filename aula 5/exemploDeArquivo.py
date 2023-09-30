arquivo = open("exemplo.txt", 'r')
soma = 0.0
quant = 0


for nota in arquivo:
    nota = float(nota)
    soma+=nota
    quant+=1


arquivo.close() #nunca esquecer de fechar o arquivo

media = soma/quant
print(f'A média foi: {media: .2f}')
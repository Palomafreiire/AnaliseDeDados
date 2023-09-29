valores = [4, 7, -23, 67]

#subistituir valor
valores[2] = 8
#adicionando valores
valores.append(1)
print(valores)
#adicionando valores em um indice especifico
valores.insert(0,100)
print(valores)
#ordem crescente
valores.sort()
print(valores)
#ordem decrescente 
valores.reverse()
print(valores)
#contar quantidade de valores
print(len(valores))
#ou
quant = len(valores) #fazer uma variavel
#apagar o ultimo elemento
valores.pop()
print(valores)
#apagar o elemento que quero
valores.pop(2)
print(valores)

#exemplo
nomes = []
for i in range(5):
    nomes.append(input('Digite um nome: '))
    #ou
    #nome = input('Digite um nome: )
    #nomes.append(nome)

nomes.sort()
print(nomes)

#comandos de minimo, maximo e soma
#min(notas)
#max(notas)
#sum(notas)
#media = sum()/len()

#comandos2
#count() retorna o numero de ocorrencias de determinado objeto
#index() procura o elemento na lista e retorna index
#len() o tamanho de uma lista ou o numero de itens que a compoe
#concatenar listas por meio do operador +
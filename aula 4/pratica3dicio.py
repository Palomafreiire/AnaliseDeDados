cardapio = {'coxinha': 5.00, 'pastel':4.00, 'suco':3.50, 'bolo': 4.50}

while True: 

    decisao = input('Você quer modificar o valor de algum produto? [s] ou [n] ')

    if decisao.lower() != 's':
        break

    pergunta = input('Você deseja [A]adicionar, [R]Remover, [M]modificar')

    if pergunta.lower() =='a':
        nome = input('Qual o nome do produto? ')
        valor = float(input('Digite o valor do produto: '))
        cardapio[nome] = valor
        
    elif pergunta.lower() == 'r':
        nome = input('Qual é o nome do produto que deseja remover? ')
        cardapio.pop(nome, "não encontrado")
        
    elif pergunta.lower() == 'm':
        nome = input('Qual o produto que você que modificar? ')
        valor = float(input('Qual o novo valor do produto? '))
        if cardapio.get(nome):
            cardapio[nome] = valor
        else:
            print('nome é invalido')
    else:
        print('Opção invalida')
    decisao = input("\nvocê deseja continuar? [s] ou [n]? ") 

     

print (cardapio)

        


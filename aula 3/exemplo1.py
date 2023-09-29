##valorCompra = float(input('Digite o valor da sua compra: (caso queira sair digite 0) '))

##while valorCompra != 0:
##    valorCompra = float(input('Digite o valor da sua compra: '))
##    valorTotal = float 
##    valorTotal += valorCompra
##    print(f'você ja gastou: {valorTotal}')
##
##    if valorCompra < 0:
##        print('valor incorreto, digite um novo valor')
##
##print('Você encerrou o programa!')
total = 0
while True:
    valor=float(input('Digite o valor do produto (ou 0 para encerrar) '))

    if valor==0:
        break
    elif valor<0:
        print('valor inválido')

    total +=valor 

    if total > 1000:
        total = total * 0.9
    
print(f'o valor da compra com desconto é de {total}')
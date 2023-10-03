def soma_num(a, b):
    return a+b

def subtracao_num(a,b):
    return a-b

def multiplicacao_num(a,b):
    return a*b

#o maior numero tem que ser dividido pelo menor
def divisao_num(a,b):
    if a>=b:
        return a/b
    else:
       return b/a


#PROGRAMA PRINCIPAL:
#while resposta == 'S':
#ou

while True:
    
    a = int(input('Escolha o primeiro numero: '))
    b = int(input('Escolha o segundo numero: '))
    escolha_operacao = input('Qual operação aritmetica você quer fazer? [S] SOMA, [B]SUBTRAÇÃO, [M]MULTIPLICAÇÃO, [D]DIVISÃO, [E]SAIR ').upper()

    if escolha_operacao == 'S':
        print(soma_num(a,b))
    elif escolha_operacao == 'B':
        print(subtracao_num(a,b))
    elif escolha_operacao == 'M':
        print(multiplicacao_num(a,b))
    elif escolha_operacao == 'D':
        print(divisao_num(a,b))
    else:
        print('programa finalizado')
    break


#função para reverter um numero: 

#Tem que primeiro converter em string:
def reverso(num):
    num = str(num)
    return (num[::-1])

numero = int (input('Digite o numero que quer ver ao contrario: '))
print(reverso(numero))
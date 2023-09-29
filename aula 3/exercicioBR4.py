#Desenvolva um programa utilizando o para que faça a tabuada de um número
#inteiro que será digitado pelo usuário. Mas a tabuada não deve necessariamente
#iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados pelo
#usuário.


numero = int (input('Digite um numero para fazer a tabuada: '))
valor_inicial = int( input ('digite o valor inicial da tabuada: '))
valor_final= int (input ('digite o valor final da tabuada: '))

for i in range (valor_inicial, valor_final+1):
    
    print (f"a tabuada fica: {numero} x {i} = {numero*i}")

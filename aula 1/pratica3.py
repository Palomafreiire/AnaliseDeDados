carros_vendidos = int (input("Quantos carros você vendeu esse mês: "))
vendas = float (input('Qual o valor total das suas vendas: '))
salario = float( input("Qual seu salario fixo: "))
comissao = float(input('Informe a comissão por cada carro vendido: '))


salario_final = salario + (comissao*carros_vendidos) + (vendas*0.05)

print(f'Seu salario final vai ficar de {salario_final: .2f}')
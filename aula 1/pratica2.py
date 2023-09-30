salario_inicial = float(input("Qual é seu salario: "))
bonus = salario_inicial*0.10
salario_final = bonus+salario_inicial

print(f'O seu salario era R$ {salario_inicial: .2f} e com o bonus de 10% de {bonus} reais, você vai passar a receber agora {salario_final: .2f}')
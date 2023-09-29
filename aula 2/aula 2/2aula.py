nome = input("Digite o Nome: ")
sexo = input("Digite seu sexo: ").upper()
valor = float(input("Valor total das compras: "))

if(sexo=="F"):
    total=valor-(valor*0.13)
    print(f"Com o desconto de 13% concedido o total das compras será de R${total:.2f}")
else:
    total=valor-(valor*0.05)
    print(f"Com o desconto de 5% concedido o total das compras será de R${total:.2f}")
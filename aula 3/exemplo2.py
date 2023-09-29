cont=0.0
soma=0.0
while True:
    nota= float(input("Qual a nota: "))
    if(nota==-1):
        break
    cont+=1
    soma+=nota
    media=soma/cont
print(f"Foram inseridas {cont:.2f} notas com a média total de {media:.2f}")

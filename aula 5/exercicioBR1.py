
frase = input("digita uma frase: ")
substituir = input(f"Quer substituir alguma palavra dessa frase?  {frase} ")
nova_palavra = input("Nova palava:  ")

nova_palavra = frase.replace(substituir, nova_palavra)

print('a frase nova ficou: ', nova_palavra.upper())



def armazenar_idade():
    nomes = []
    idades = []

    while True:
        nome = input('Digite um nome: ')
        idade = int(input(f'Digite a idade de {nome}: '))

        if nome == 'maria':
            print('Maria não pode ser adicionada')
            continue
        if idade == -1:
            break

        nomes.append(nome)
        idades.append(idade)

    return nomes, idades

print(armazenar_idade())
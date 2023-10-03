from random import randint

def sorteia():
    numeros = []
    for i in range(5):
        numeros.append(randint(0,99))
    return numeros


def somaPar(numeros):
    pares = []
    for i in numeros:
        if i%2 == 0:
            pares.append(i)
    print(f'Valores pares da lista: {pares}')
    print(f'A soma dos valores pares é: {sum(pares)}')

somaPar(sorteia())
 
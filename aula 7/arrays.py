import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Acessando um elemento especifico
elemento = arr [2]
print('Elemento da posiçaõ 2: ', elemento)

# Fatiamento do array

sub_array = arr[1:4]
print('\nFatiamento do array')
print(sub_array)

# OPERAÇÕES MATEMATICAS EM ARRAYS
# ele soma o primeiro valor do arr1 com o primeiro valor do arr2

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
arr3 = np.array([1, 2, 3])

# soma de arrays
soma = arr1 + arr2
print('Soma dos arrays: ', soma)

# Subtração de arrays

subtracao = arr2 - arr1
print("A subtração dos arrays: ", subtracao)

# SOMA dos elementos do array
arra = np.array([1, 2, 3, 4, 5])

#soma dos elementos dentro do array
soma = np.sum(arra)
print('Soma dos elementos: ', soma)


# BROADCASTING 
# permite realizar operações de array de diferentes dimensões

ar1 = np.array([[1, 2, 3], [4, 5, 6]])
ar2 = np.array ([10, 20, 30])

#broadcast para somar array bidimensional com array unidimensional
resultado = ar1 + ar2
print('Resultado após broadcast')
print(resultado)


#array unidimensional
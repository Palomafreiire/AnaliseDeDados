notas = []

for i in range(5):
    notas.append(float (input('Digite sua nota: ')))

   
soma = sum(notas)
media = soma/len(notas)
    
print(f'Media das notas: {media: .2f}')

for nota in notas:
    if nota > media:
        print(f'a nota {nota} é maior que a média')
        

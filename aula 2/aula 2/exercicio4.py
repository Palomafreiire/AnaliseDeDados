idade = int( input('Digite sua idade: '))

if idade < 4 or idade >= 60:
    print('entrada gratuita')
elif idade > 4 and idade < 18:
    print('Sua entrada custa 20 reais')
elif idade >=18:
    print('Sua entrada custa 30 reais')
else:
    print ('informação errada!')
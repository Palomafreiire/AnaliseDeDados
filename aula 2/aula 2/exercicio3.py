level = int(input("Qual é o level do Voltorb? "))

if level >= 1 and level <= 20:
    w = 20 + (level) ** 3
elif level > 20 and level <= 40:
    w = 8000 + (level - 10) ** 2
elif level > 40 and level <= 60:
    w = 9000 + 5 * level
elif level > 40 and level <= 80:
    w = 9300 + 2 * level
elif level > 80 and level <= 100:
    w = 9500 + level
else:
    print('Inválido.')

print('O dano fo10i de {}'.format(w))
num = int(input('Escolha um numero para saber sua tabuada: '))
print('-' * 15)
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
print('-' * 15)

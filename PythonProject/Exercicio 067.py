while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if valor < 1:
        break
    for c in range(1, 11):
        print(f'{valor} x {c} = {valor * c}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

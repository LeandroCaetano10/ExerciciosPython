valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em forma decrescente são {valores}')
if 5 in valores:
    print('O valore 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')

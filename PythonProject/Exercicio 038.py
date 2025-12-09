pnum = int('Primeiro número: ')
snum = int('Segundo número')
if pnum > snum:
    print('O primeiro valor é maior!'.format(pnum))
elif snum > pnum:
    print('O segundo valor é maior!'.format(snum))
elif pnum == snum:
    print('Não existe valor maior os 2 números são iguais!')

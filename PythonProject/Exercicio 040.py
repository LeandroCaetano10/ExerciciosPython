pn = float(input('Primeira nota: '))
sn = float(input('Segunda nota: '))
media = ( pn + sn ) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(pn, sn, media))
if media < 5:
    print('O aluno esta REPROVADO!')
elif media >= 5.1 and media <= 6.9:
    print('O aluno esta de RECUPERAÇÃO!')
elif media >= 7:
    print('O aluno esta APROVADO!')

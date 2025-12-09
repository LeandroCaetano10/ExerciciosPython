def lin():
    print('-' * 20)


def área():
    larg=float(input('LARGURA (m): '))
    comp= float(input('COMPRIMENTO (m): '))
    print(f'A área de um terreno {larg}X{comp} é de {larg*comp}m².')


#programa Principal
lin()
print('Controle de Terrenos')
lin()
área()

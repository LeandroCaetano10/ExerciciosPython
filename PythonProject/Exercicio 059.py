pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
sair = False
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair ''')
    opcao = int(input('>>> Qual é a sua opcao: '))
    if opcao == 1:
        print('A soma do valor {} + {} é igual a {}'.format(pv, sv, pv + sv))
    elif opcao == 2:
        print('A multiplicação de {} X {} é igual a {}'.format(pv, sv, pv * sv))
    elif opcao == 3:
        if pv > sv:
            print('O primeiro valor {} é o MAIOR '.format(pv))
        else:
            print('O Segundo valor {} é o MAIOR'.format(sv))
    elif opcao == 4:
        print('Informe os números novamente')
        pv = int(input('Primeiro valor: '))
        sv = int(input('Segundo valor: '))
    elif opcao == 5:
        sair = True
        print('FIM DO PROGRAMA')
    else:
        print('Opção Inválida. Tente novamente')
    print('-=' * 20)

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro / cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desconto = preco - (preco * 10 / 100)
    print('Sua compra de R${} vai custar R${} no final com um desconto de 10%.'.format(preco, desconto))
elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print('Sua compra de R${} vai custar R${} no final com um desconto de 5%.'.format(preco, desconto))
elif opcao == 3:
    print('Sua compra de R${} vai custar R$ {} no final com valor normal.'.format(preco, preco))
elif opcao == 4:
    juros = preco + (preco * 20 / 100)
    print('Sua compra de R${} vai custar R${} no final com 20% de juros.'.format(preco, juros))

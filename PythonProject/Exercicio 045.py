from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
print('Suas opções:')
print('[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
opcao = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 10)
print('Computador jogou {} \nJogador jogou {}'.format(itens[maquina], itens[opcao]))
print('-=' * 10)
if opcao == 0:
    if maquina == 0:
        print('EMPATE')
    elif maquina == 1:
        print('Você PERDEU. TENTE NOVAMENTE')
    elif maquina == 2:
        print('Jogador VENCE')
if opcao == 1:
    if maquina == 0:
        print('Jogador VENCE')
    elif maquina == 1:
        print('EMPATE')
    elif maquina == 2:
        print('Você PERDEU. TENTE NOVAMENTE')
if opcao == 2:
    if maquina == 0:
        print('Você PERDEU. TENTE NOVAMENTE')
    elif maquina == 1:
        print('Jogador VENCE')
    elif maquina == 2:
        print('EMPATE')

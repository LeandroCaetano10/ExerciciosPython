from random import randint
from time import sleep
sleep(1)
print('-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar')
print('-'*20)
sleep(2)
num = int(input('Em que número eu pensei? '))
numero = randint(0, 5)
sleep(2)
print('PROCESSANDO...')
sleep(2)
if num == numero:
    print('Parabéns, você acertou!')
else:
    print('Ganhei Eu pensei no número {} e nao no número {}'.format( numero, num))
sleep(2)
print('FIM')

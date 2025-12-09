
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(1, tot):
    partidas.append(int(input(f'Quantos gols na {c+1}ª partida: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['Nome']} jogou {tot} partidas. ')
for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i+1} , fez {v} Gols')
print(f'Foi um total e {jogador['Total']} gols')

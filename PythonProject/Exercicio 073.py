times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Botafogo',
         'Bahia', 'Fluminense', 'São Paulo', 'Bragantino', 'Corinthians',
         'Atlético MG', 'Grêmio', 'Vasco da Gama', 'Ceará SC', 'Internacional',
         'EC  Vitória', 'Santos', 'Fortaleza', 'Juventude', 'Sport Recife' )
print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 30)
print(f'Os 4 ultimos são {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 30)
print(f'O Santos está na {times.index('Santos')+1}ª posição')
print('-=' * 30)

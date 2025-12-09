distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a comerçar uma viagem de {} km/h'.format(distancia))
if distancia <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia * 0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia * 0.45))

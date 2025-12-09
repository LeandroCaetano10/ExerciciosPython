largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
parede = largura * altura
pintar = parede / 2
print('Sua parede tem a dimensão de {} x {} a sua área é de {}m2.'.format(largura, altura, parede))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(pintar))

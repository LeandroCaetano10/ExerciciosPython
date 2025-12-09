din = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Com {} você pode comprar US${:.1f}'.format(din, din/5.33))
print('Com {} você pode comprar €{:.1f}'.format(din, din/6.18))
print('Com {}você pode comprar £{:.1f}'.format(din, din/7.01))

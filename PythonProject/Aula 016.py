lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche))
print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posiçao {cont}')

for pos , comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
________________________________________________________________
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.index(5))

pessoa = ()
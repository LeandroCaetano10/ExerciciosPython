#valores = list()
#for cont in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))
#for c, v in enumerate(valores):
#    print(f'Na posição {c} entrei o valor {v} .')
#print('Cheguei ao final da lista')


a = [0, 2, 4, 6, 8]
b = a[:]
b[2] = 8
crescente = a.sort()
decrescente = b.sort()
print(f'A lista A {a} , em forma Crescente {crescente}')
print(f'Alista B {b} , em forma Decrescente {decrescente}')

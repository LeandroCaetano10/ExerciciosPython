from random import shuffle
pa = str(input('Digite o nome do primeiro aluno: '))
sa = str(input('Digite o nome do segundo aluno: '))
ta = str(input('Digite o nome do terceiro aluno: '))
qa = str(input('Digite o nome do quarto aluno: '))
lista = [pa, sa, ta, qa]
sorteio = shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))

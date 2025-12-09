import random
pa = str(input('Digite o nome do primeiro aluno: '))
sa = str(input('Digite o nome do segundo aluno: '))
ta = str(input('Digite o nome do terceiro aluno: '))
qa = str(input('Digite o nome do quarto aluno: '))
sorteio = random.choice([pa, sa, ta, qa])
print('O aluno escolhido foi {}!'.format(sorteio))

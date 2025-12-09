#aluno = dict()
#media = list()
#for c in range(1):
#    aluno['Nome'] = str(input('Nome: '))
#    aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
#    media.append(aluno.copy())
#for a in media:
#    for k, v in a.items():
#        print(f'{k} é igual a {v}')
#if aluno["Média"] >= 7:
#    print('Situação é igual a APROVADO!')
#elif 5 <= aluno["Média"] < 7:
#    print('Situação é igual a RECUPERAÇÃO')
#else:
#    print('Situação é igual a RECUPERAÇÃO')

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno["Média"] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno["Média"] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

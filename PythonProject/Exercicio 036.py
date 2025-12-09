casa = float(input('Qual é o valor da casa: R$ '))
salario = float(input('Qual é o salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
meses = anos * 12
porcento = salario * 30 / 100
pm = casa / meses
if porcento < pm:
    print('Para pagar uma casa de R$ {} em {} anos a prestação será de R$ {:.2f} . EMPRÉSTIMO NEGADO! '.format(casa, anos, pm))
elif porcento > pm:
    print('Para pagar uma casa de R$ {} em {} anos a prestação será de R$ {:.2f} . EMPRÉSTIMO APROVADO! '.format(casa, anos, pm))

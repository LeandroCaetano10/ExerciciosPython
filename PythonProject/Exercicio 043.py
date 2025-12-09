peso = float(input('Qual é o seu peso? (KG): '))
altura = float(input('Qual é a sua altura? : '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você esta no PESO NORMAL!')
elif imc >= 25.1 and imc < 30:
    print('Você esta em SOBREPESO!')
elif imc >= 30.1 and imc < 40:
    print('Você esta em OBESIDADE!')
elif imc >= 40.1:
    print('Você esta em OBESIDADE MORBIDA, cuidado!')

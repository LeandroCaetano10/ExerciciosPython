s = cont = 0
while True:
    n = int(input('Digite um valor ( 999 para parar ): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Você digitou {cont} valores e a soma vale {s}')

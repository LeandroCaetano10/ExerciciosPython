#def contador(* num):
#    tam = len(num)
#   print(f'Recebi os valores {num} e ao todo são {tam} números.')
#
#
#contador(2, 7, 9, 10)
#contador(3, 3, 3, 4, 1, 5, 6)
#contador(8, 11, 17, 15, 21, 20, 13)


#def dobra(lst):
#	pos = 0
#	while pos < len(lst):
#		lst[pos]*=2
#		pos +=1
#
#
#valores = [6, 3, 9, 1, 0, 2]
#dobra(valores)
#print(valores)
#
def soma(* valores):
    s = 0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores}, temos {s}.')


soma(5, 7)
soma(2, 9, 4)
soma(12, 7, 75,42)
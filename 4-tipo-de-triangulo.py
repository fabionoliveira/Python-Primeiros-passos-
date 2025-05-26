#la=0, ld=0, lc=0
#la, lb, lc
#la == lb and la == lc and lb == lc triangulo
#la >= lb + lc  nao é triangulo
#la >= lb + lc or lb >= la + lc or lc >= lb + la
#tipo triangulo


#SE ( A >= (B+ C) ou B >=(A+C) ou C >= (B+A) )

#equilátero mesma medida os tres lado

#escaleno os três lados com medidas diferentes

#isósceles é um polígono que apresenta três lados, sendo dois deles congruentes (mesma medida). O lado com medida diferente é chamado de base do triângulo isósceles.


import os
import time
import sys

la = 0
lb = 0
lc = 0
tipo = ' '

print('Digite valores para saber qual TIPO de Triângulo.')
print('Obs: Digitar Valores "Positivos".')

la = int(input('Digite valor para lado a: ' ))
lb = int(input('Digite valor para lado b: ' ))
lc = int(input('Digite valor para lado c: ' ))

if la < 0 or lb < 0 or lc < 0:
	print('\nValor "NEGATIVO" encontrado, tente novamente!!!')
	sys.exit()
	
if (la >= (lb + lc) or lb >= (la + lc) or lc >= (lb + la)):
        print('\nSão apenas 3 lados.')
        print('Não é um Triângulo, tente novamente!!!.')

elif la == lb and la == lc and lb == lc:
        tipo = '"Equilatero",'
        print('\nO tipo de Triângulo é',tipo,'são 3 lados iguais.')

elif la == lb and la != lc or  la == lc and lb != lc or  lb == lc and lb != la:
        tipo = '"Isósceles",'
        print('\nO tipo de Triângulo é',tipo,'são 2 lados iguais 1 diferente.')

else:
        tipo = '"Escaleno",'
        print('\nO tipo de Triângulo é',tipo,'são todos lados diferentes.')





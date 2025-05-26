# n1=0, n2=0, n3=0, maior=0
#n1, n2, n3

#n1 < 0 or n2 < 0 or n3 <0
#n1 == n2 or n1 == n3 or n2 == n3
#n1 > n2 and n1 > n3
#n2 > n1 and n2 > n3

#maior


import os
import time
import sys

n1 = 0
n2 = 0
n3 = 0
maior = 0

print('Digite três valores para saber qual é o Maior.')
print('Obs: Não digite valor "NEGATIVO" ou "IGUAIS".')
n1 = int(input('Digite valor para nº 1:' ))
n2 = int(input('Digite valor para nº 2:' ))
n3 = int(input('Digite valor para nº 3:' ))

if n1 < 0 or n2 < 0 or n3 <0:
    print('Valor negativo encontrado, tente novamente!!!')
    print('O programa será fechado.')
    time.sleep(5)
    print('Programa finalizado')
    sys.exit()

elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Valores iguais encontrado, tente novamente!!!')
    print('O programa será fechado.')
    time.sleep(5)
    print('Programa finalizado')
    sys.exit()

if n1 > n2 and n1 > n3:
    maior = n1
    print('O valor maior é: ', maior)

elif n2 > n1 and n2 > n3:
    maior = n2
    print('O valor maior é: ', maior)

else:
    maior = n3
    print('O valor maior é: ', maior)


# -*- coding: utf-8 -*-
import math
import sys

# 0 1 2 => configuro os indice em um for range
v = [1,0,-1]
vc = ['Vitoria', 'Salvador']

n = len(v) # calcula o tamanho

# no FOR IN o x aqui será cada valor interno do vetor
for x in v:
    aux = math.pow (x,2) + x
    print(f'{aux}')

print(f'O Vetor contém {n} elementos.')

# no FOR RANGE o i aqui será apenas a posição de cada valor do vetor
print('\nvalores gerados no FOR RANGE.')

for i in range(0,len(vc)):
    aux = vc[i] #**3 + 10
    print(aux)

sys.exit



# -*- coding: utf-8 -*-
import os
import sys
import time


def LerNum():
    num = int(input('Digite um número: '))

    if num >= 0:
        
        print( num, 'é Positivo')
        return num
    
    else:
        print(num,' é Número NEGATIVO!!!')
        sys.exit()

# função verifica se um número é par
def numeroPar ( num ):
 if num %2==0:
     return True
 else:
     return False



num = LerNum()
n = numeroPar(num)
print(f'O número {num} Par?\nResultado {n}')

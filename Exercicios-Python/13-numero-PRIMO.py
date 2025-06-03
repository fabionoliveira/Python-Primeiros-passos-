# -*- coding: utf-8 -*-
import os
import sys
import time


def LerNum():
    num = int(input('Digite um Número "Positivo": '))

    if num > 0:
        
        print( f'O número {num} é Positivo')
        return num
    elif num == 0 or num < 0:
        if num ==0:
            print('O número deve ser maior que Zero!!')
        else:
            print(f'O número {num} é NEGATIVO!!!')
        print('Tente Novamente!!!')
        sys.exit()
                

# função que verifica se um número é primo ou não.
def numeroPrimo ( num ):
 
 contdiv=0; # contar divisores
 for i in range (1, num+1, 1):
     if num % i == 0:
         
         contdiv +=1; # incrementa 1 ao contdiv
 
 if  contdiv == 2:
     #print(contdiv)
     return True # é primo
     
 else:
     return False # não é primo

#função somar números primos.
def somaPrimo(x,num):
    soma = 0
    for i in range(x, num+1):
        if numeroPrimo (i):
            soma += i
            
    return soma
    
num = LerNum()
primo = numeroPrimo(num)
soma = somaPrimo(1,num)
print(f'O número {num} é Primo?\nResultado {primo}')
print(f'Soma dos números PRIMOS de 1 á {num} é {soma}.')

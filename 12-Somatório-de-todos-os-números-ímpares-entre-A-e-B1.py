# -*- coding: utf-8 -*-

import os
import sys


def saldoimapresdeAeB ( a, b):
   
    saldo = 0

    #print('\n')
    if a < b:
        
        for cont in range ( a , b+1):
                
            if cont %2 != 0:
                print(cont, end = ' ')
                saldo += cont
            
        return saldo

    elif b < a:
        
        for cont in range ( b , a+1):
                
            if cont %2 != 0:
                print(cont, end = ' ')
                saldo += cont
            
        return saldo
    
    else:
        print('\nOs Número informado não podem ser >>IGUAIS<<.')
        print('\nTente novamente!!!')
        print('\nPrograma finalizado.')
        sys.exit()
        

def Executar():
    print('\nDigite valores para A e B.')
    a = int(input('\nDigite o Número para A: '))
    b = int(input('Digite o Número para B: '))
    print('\n_______________________ Resultado _______________________')

    soma = saldoimapresdeAeB ( a, b)
    print('\n')
    print(f'\nO Somatório de todos os números ímpares entre A e B é {soma}.\n')
    
                    
Executar()
#sys.exit()
    

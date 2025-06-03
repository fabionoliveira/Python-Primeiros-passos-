# -*- coding: utf-8 -*-

import os
import sys


def lern():
    n = int(input('\nDigite o Número: '))
    return n

def calpar(n):
    par = 0

    for cont in range (0,n,1):

        if cont %2 == 0:
            par += cont
            
    return par


def calimpar(n):
    impar = 0

    for cont in range (0,n,1):
        if cont %2 != 0:
            impar += cont
            
    return impar


def exibir(n, par, impar):
    print(f'\nNúmero......: {n}')
    print(f'Total Par...: {par}')
    print(f'Total Impar.: {impar}')


def inicio():
    tecla = 0

    lmenu = '1 Ler '
    lmenu += '\n2 Calcular '
    lmenu += '\n3 Exibir '
    lmenu += '\n4 Sair '
    lmenu += '\nItem: '
    
    while tecla != 4:
        print('\n*** Menu Programa ***')
        tecla = int(input(lmenu))
        
        if tecla ==1:
            n = lern()

        elif tecla ==2:
            totpar = calpar(n)
            totimpar = calimpar(n)
            
        elif tecla ==3:
            exibir(n, totpar, totimpar)

        
inicio()
sys.exit()
    

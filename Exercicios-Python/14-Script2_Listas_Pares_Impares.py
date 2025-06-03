# -*- coding: utf-8 -*-
import os
import sys

Num = list(range(1,11)) #criando vetor Num
P = [] # vetor de pares
I = [] #vetor de impares

def gerar():
    for x in Num: # x são os valores de Num 
        if x %2 ==0:
            P.append(x) # inserir números pares

        else:
            I.append(x) # inserir números impares

def mostrar():
    os.system('cls')
    print(f'Números: {Num}')
    print(f'Pares..: {P}')
    print(f'Impares: {I}')

def controle():
    gerar()
    mostrar()

controle()

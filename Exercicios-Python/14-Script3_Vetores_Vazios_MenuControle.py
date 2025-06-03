# -*- coding: utf-8 -*-

import os
import sys

# vetores vazios 
sal=[]
ida=[]
aum=[]


def novaLinha():
    salario = float(input('Salário: '))
    idade = int (input('Idade: '))
    sal.append(salario)
    ida.append(idade)
    valor = salario * 1.1
    aum.append ( valor )

def mostrarDados():
    #os.system('cls')
    n = len(sal)
    for i in range(0,n):
        print(f'Salário: {sal[i]:0.2f} Aumento: {aum[i]:0.2f} Idade: {ida[i]}')

    #os.system('sleep 3')


def controle():
 while ( True ):
     #os.system('cls')
     linhasmenu = '1 Inserir\n2 Mostrar\n3 Sair\nItem:'
     itemmenu = int(input(linhasmenu))
     if itemmenu==1:
         novaLinha()

     elif itemmenu==2:
         mostrarDados()

     elif itemmenu==3:
         break

controle()
sys.exit

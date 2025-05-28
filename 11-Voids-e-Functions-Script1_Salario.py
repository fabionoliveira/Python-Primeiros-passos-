# -*- coding: utf-8 -*-
import os
import sys
import time

taxaaumento = 0.1
def cal_Aumento ( salario ):
    sal = taxaaumento * salario + salario
    return sal


def mostrar ( salario, aumento):
    os.system('cls')
    saida = f'Salario:R$ {salario:.2f} \nAumento:R$ {aumento:.2f}'
    print(saida)
    time.sleep(5)


def executar():
    os.system('cls')
    salario = float(input('\nDigite o salário:'))
    aumento=cal_Aumento ( salario )# função
    mostrar (salario, aumento) #processo
    time.sleep(5)


# executando as sub rotinas
executar() # executando o processo executar()
sys.exit
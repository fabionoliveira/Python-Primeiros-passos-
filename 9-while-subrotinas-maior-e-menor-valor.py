# Quadro Resumo
# 1) salario, salmaior, salmenor, media, saldo, cont
# 2) salario
# 3) cont += 1, saldo += salario, media = saldo / cont
# 4) salmaior, salmenor, media, saldo

# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-

import os
import sys

# variáveis globais com escopo global
import time

salario = 0
salmaior = 0
salmenor = 0
media = 0
saldo = 0
cont = 0


def LerCalcular():
    global salario
    global salmaior
    global salmenor
    global media
    global saldo
    global cont
    # ler salario
    salario = float(input('Digite o salário:'))

    # fazer os calculos
    cont += 1
    saldo += salario
    media = saldo / cont

    if cont == 1:
        salmaior = salario
    salmenor = salario

    if salario < salmenor:
        salmenor = salario

    if salario > salmaior:
        salmaior = salario


# fim da sub rotina LerCalcular()

def Resultados():
    #os.system('cls')
    print('\n*** Exibição de Resultados ***')
    print('\nSaldo:', saldo)
    print('\nMedia:', media)
    print('\nSalário Maior:', salmaior)
    print('\nSalário Menor:', salmenor)
    #os.system('sleep 5')


# fim da sub rotina Resultados

# código de menu controle está das sub rotinas
item = 0
while item != 3:
    #os.system('cls')
    item = int(input(
        '\n** Menu de Controle***\n1 Ler e Calcular\n2 Resultados\n3 Finalizar\nitem:'))

    if item == 1:
        LerCalcular()

    elif item == 2:
        Resultados()

sys.exit
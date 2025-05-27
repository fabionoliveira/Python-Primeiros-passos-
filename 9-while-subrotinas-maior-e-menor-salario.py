# Quadro Resumo
#_______________________________________________
#  CRIAR VARIAVEIS
#  ida = 0, contmenor = 0, contmaior = 0,
#  sal = 0, salmaior = 0, salmenor = 0,
#  salmenor18 = 0, salmaior18 = 0
#_______________________________________________
# LER
# ida, sal
#_______________________________________________
# CALCULOS
# contmenor += 1, contmaior += 1
#_______________________________________________
# EXIBIR
# salmaior, salmenor, contmenor,
# salmenor18, salmaior18, contmaior
#_______________________________________________

# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-

import os
import sys

# variáveis globais
ida = 0
contmenor = 0
contmaior = 0
sal = 0
salmaior = 0
salmenor = 0
salmenor18 = 0
salmaior18 = 0


def IdaSal():
    global ida
    global contmenor
    global contmaior
    global sal
    global salmaior
    global salmenor
    global salmenor18
    global salmaior18

    #Ler
    ida = int(input('Digite sua Idade: '))
    sal = float(input('Digite seu Salário: '))

    #Calculos
    if ida >= 1 and ida < 18:
        contmenor += 1

        if contmenor == 1:
            salmaior = sal
            salmenor = sal

        if sal < salmenor:
            salmenor = sal

        if sal > salmaior:
            salmaior = sal

    if ida >= 18 and ida < 120:
        contmaior += 1

        if contmaior == 1:
            salmaior18 = sal
            salmenor18 = sal

        if sal < salmenor18:
            salmenor18 = sal

        if sal > salmaior18:
            salmaior18 = sal


#Exibir
def Exibir():
    print('_' * 68)
    print('*' * 22, 'Exibição de Resultados', '*' * 22)
    print('------- Menor Idade -----------')
    print(f'Salário Maior R${salmaior:.2f}')
    print(f'Salário Menor R${salmenor:.2f}')
    print(f'Contagem de Menor de Idade é {contmenor}\n')

    print('-------- Maior Idade ----------')
    print(f'Salário Menor R${salmenor18:.2f}')
    print(f'Salário Maior R${salmaior18:.2f}')
    print(f'Contagem de Maior de Idade é {contmaior}\n')


#Menu Programa
menu = 0
while menu != 3:
    print('=' * 25, 'Menu do Programa', '=' * 25)
    menu = int(input('[1]Incluir [2]Exibir [3]Sair do Programa\n>>>Opção:'))

    if menu == 1:
        IdaSal()

    elif menu == 2:
        Exibir()

print('_' * 68)
print('Saindo do programa!!!\nPrograma finalizado...\n')
sys.exit

# -*- coding: utf-8 -*-
import os
import sys
import time
import math

def LerMon():
    mon = float(input('Digite o Valor do Montante: '))
    return mon


def LerPer():
    per = int(input('Digite PERÍODO em Meses: '))
    return per


def VlJur():
    jur = 5
    return jur


def VlCap(mon, per, jur):
    cap = mon / ((jur/100)* per)
    return cap


def Exibir(cap, mon, per, jur):
    #os.system('cls')
    print('')

    lsaida = '---------------------------- Exibir Resultados ----------------------------'
    lsaida += '\nValor Montante Informado foi R${:0.2f}'
    lsaida += '\nTaxa de JUROS (Simples) de " {}% " ao mês.'
    lsaida += '\nPERÍODO de " {} " meses.'
    lsaida += '\nPara o "MONTANTE" informado, o Valor do Capital deve ser R${:0.2f}\n'
    print(lsaida .format(mon, jur, per, cap))


def MenuPrin():
    menu = 0

    lmenu = '[1]Incluir '
    lmenu += '[2]Calcular '
    lmenu += '[3]Exibir '
    lmenu += '[4]Sair '
    lmenu += '\n>>Opção: '

    while True:
        #os.system('cls')
        print('')
        print('=' * 30, 'Menu Programa', '=' * 30)
        menu = int(input(lmenu))

        if menu == 1:
            print('-' * 33, 'Incluir', '-' * 33)
            mon = LerMon()
            per = LerPer()
            print('')

        elif menu == 2:
            print('-' * 31, 'Calcular... ', '-' * 30)
            jur = VlJur()
            cap = VlCap(mon, per, jur)
            print('Calculado com Sucesso!!!')
            print('')
            time.sleep(3)

        elif menu == 3:
            Exibir(cap, mon, per, jur)

        elif menu == 4:
            print('-' * 28, 'Sair Escolhido!!!', '-' * 28)
            print('Programa Finalizado')
            break

MenuPrin()
sys.exit()

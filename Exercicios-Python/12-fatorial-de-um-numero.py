# -*- coding: utf-8 -*-

import os
import time
import sys


def LerN():
    print('\nPara saber o Fatorial de um Número.')
    num= int( input('Digite um Número: '))
    return num

    
def CalF(num):
    fat = 1
    for num in range (1, num+1):
       fat = fat * num
    return fat

    
def Exibir(num,fat):
    os.system('cls')
    print(f'\nFatorial do número digitado {num}! é {fat}')
    time.sleep(20)


def MenuPrin():
    menu = 0

    lmenu = '[1]Incluir '
    lmenu += '[2]Calcular '
    lmenu += '[3]Exibir '
    lmenu += '[4]Sair '
    lmenu += '\n>>Opção: '
    
    while True:
        os.system('cls')
        print('')
        print('=' * 30, 'Menu Programa', '=' * 30)
        menu = int(input(lmenu))
        
        if menu == 1:
            print('-' * 33, 'Incluir', '-' * 33)
            num = LerN()
            
        elif menu == 2:
            print('-' * 31, 'Calcular... ', '-' * 30)
            print('\nCalculado com Sucesso!!')
            fat = CalF(num)

        elif menu == 3:
            print('-' * 28, 'Exibir Resultados', '-' * 28)
            Exibir(num,fat)
            
        elif menu == 4:
            print('-' * 28, 'Sair Escolhido!!!', '-' * 28)
            print('\nPrograma Finalizado\n')
            break

                    
MenuPrin()
sys.exit()

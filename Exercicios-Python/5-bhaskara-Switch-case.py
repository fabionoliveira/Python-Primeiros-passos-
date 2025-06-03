# QUADRO RESUMO
#
#Variáveil e constantes
#1. a=0, b=0 , c=0, delta=0, x1=0, x2=0, tecla=0
#
#Leitura de dados
#2. a, b, c, tecla
#
#Cálculo e condições
# 3. a == 0
#    b * b -4 * a * c
#    delta >= 0
#    - b + ((delta **(1/2) / 2 * a)
#    - b - ((delta **(1/2) / 2 * a)
#    delta < 0
#Exibir
# 4. a, b, c, delta, x1, x2
#
###########################################################

import os
import time
import sys

a = 0
b = 0
c = 0
delta = 0
x1 = 0
x2 = 0
tecla = 0

os.system('cls') 
tecla = int(input("\n____________Menu do Programa_____________\n[1]->Ler,Cálcular,Exibir\n[2]->Sair do Programa\n>>> Opção:"))

if tecla == 1:
    print('\n-*-* Informe os valores para A, B, C *-*-')
    a = int(input('Digite o valor para A:'))
    b = int(input('Digite o valor para B:'))
    c = int(input('Digite o valor para C:'))

    delta = b * b -4 * a * c

    if a == 0:
        print('\nO valor para "a" deve ser diferente de Zero!!!')
        print('\nTente novamente!!!')
        print('\nO Programa será finalizado!!!')
        print('Programa finalizado.')
        sys.exit()                    
 
    if delta < 0:
        print('\n"Sem solução no conjunto dos números Reais!"')
        print('\n-*-* Tela de Resultados *-*-')
        print(' Valor de a....:', a )
        print(' Valor de b....:', b )
        print(' Valor de c....:', c )
        print(' Valor de delta:', delta )
        print('\nO Programa será finalizado!!!')
        print('Programa finalizado.')
        sys.exit()
           
    if delta >= 0:        
        x1 = - b + ((delta **(1/2) / 2 * a))
        x2 = - b - ((delta **(1/2) / 2 * a))
        print('\n-*-* Tela de Resultados *-*-')
        print(' Valor de a....:', a )
        print(' Valor de b....:', b )
        print(' Valor de c....:', c )
        print(' Valor de delta:', delta )
        print(f'\n Valor de x1...: {x1:.2f}')
        print(f' Valor de x2...: {x2:.2f}')      
    
if tecla == 2:
    print('Saindo do Programa!!!')
    print('Programa finalizado.')
    sys.exit()    


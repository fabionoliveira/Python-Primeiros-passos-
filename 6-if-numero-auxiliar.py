#QUADRO RESUMO
# 1) n1=0, n2=0, n3=0, n4=0, aux=0
#
# 2) n1, n2, n3, n4
#
# 3) Sem calculos
#
# 4) Valor em ordem crescente n1, n2, n3, n4
#
######################################################



import os
import time
import sys


n1 = 0
n2 = 0
n3 = 0
n4 = 0
aux = 0
tecla = 0


os.system('cls')

tecla = int ( input ("\n=============== Menu do Programa ===============\n[1] Executar [2] Sair do Programa\n>>> Opção:") )

if tecla == 1:
    print('\n-*-*-*-*-*-*-* Informe os valores *-*-*-*-*-*-*-')

    n1=int(input('Digite valor para O primeiro Número: '))
    n2=int(input('Digite valor para O segundo Número: '))
    n3=int(input('Digite valor para O terceiro Número: '))
    n4=int(input('Digite valor para O quarto Número: '))

    if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
        print('\nValores iguais identificados tente novamente!!!\nO programa será finalizado.\nPrograma finalizado.\n')
        sys.exit()
               
    if n1 > n2:
        aux = n1
        n1 = n2
        n2 = aux
        
    if n1 > n3:
        aux = n1
        n1 = n3
        n3 = aux

    if n1 > n4:
        aux = n1
        n1 = n4
        n4 = aux

    if n2 > n1:    
        aux = n2
        n2 = n1
        n1 = aux
        
    if n2 > n3:
        aux = n2
        n2 = n3
        n3 = aux

    if n2 > n4:
        aux = n2
        n2 = n4
        n4 = aux

    if n3 > n1:
        aux = n3
        n3 = n1
        n1 = aux

    if n3 > n2:
        aux = n3
        n3 = n2
        n2 = aux

    if n3 > n4:
        aux = n3
        n3 = n4
        n4 = aux

    if n4 > n1:
        aux = n4
        n4 = n1
        n1 = aux

    if n4 > n2:
        aux = n4
        n4 = n2
        n2 = aux

    if n4 > n3:
        aux = n4
        n4 = n3
        n3 = aux
    
        
    print('\n-*-*-*-*-*-*-* Tela de Resultados *-*-*-*-*-*-*-')
    print('A ordem crescente dos números informados são:\n''(',n4,',',n3,',',n2,'e',n1,').\n')

if tecla == 2:
    print('________________________________________________')
    print('Saindo do programa.\nPrograma finalizado.\n')
    sys.exit()
    
    

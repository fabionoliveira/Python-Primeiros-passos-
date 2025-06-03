import os
import sys
import time

n1 = 0
n2 = 0
n3 = 0
n4 = 0
msg = ''
tecla = 0

os.system('cls')
tecla = int(input("\n============== Menu do Programa ==============\n[1]->Executar [2]->Sair do Programa\n>>> Opção:"))

if tecla == 1:
    n1 = int(input('Digite valor para o primeiro número:'))
    n2 = int(input('Digite valor para o segundo número:'))
    n3 = int(input('Digite valor para o terceiro número:'))
    n4 = int(input('Digite valor para o quarto número:'))

    print('\n-*-*-*-*-*-* Tela de Resultados *-*-*-*-*-*-')

    if n1 % 2 == 0 and n1 % 3 == 0:
        msg = 'é divisível por 2 e 3 ao mesmo tempo!'
        print(n1, msg)
    
    if n2 % 2 == 0 and n2 % 3 == 0:
        msg = 'é divisível por 2 e 3 ao mesmo tempo!'
        print(n2, msg)
    
    if n3 % 2 == 0 and n3 % 3 == 0:
        msg = 'é divisível por 2 e 3 ao mesmo tempo!'
        print(n3, msg)
    
    if n4 % 2 == 0 and n4 % 3 == 0:
        msg = 'é divisível por 2 e 3 ao mesmo tempo!'
        print(n4, msg)

if tecla == 2:
    print('Saindo do programa.')
    print('Programa finalizado.')
    sys.exit()

import os
import sys
import time

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
maior = 0
menor = 0
tecla = 0

os.system('cls')
tecla = int(input("\n============== Menu do Programa ==============\n[1]->Executar [2]->Sair do Programa\n>>> Opção:"))

if tecla == 1:
    n1 = int(input('Digite valor para o primeiro número:'))
    n2 = int(input('Digite valor para o segundo número:'))
    n3 = int(input('Digite valor para o terceiro número:'))
    n4 = int(input('Digite valor para o quarto número:'))
    n5 = int(input('Digite valor para o quinto número:'))

    maior = n1
    menor = n1

    print('\n-*-*-*-*-*-*-* Tela de Resultados *-*-*-*-*-*-*-')

    if n2 > maior:
        maior = n2

    if n3 > maior:
        maior = n3

    if n4 > maior:
        maior = n4

    if n5 > maior:
        maior = n5

    if n2 < menor:
        menor = n2

    if n3 < menor:
        menor = n3

    if n4 < menor:
        menor = n4

    if n5 < menor:
        menor = n5

    print('O maior número é''\033[1;33m',maior,'\033[m''e o menor número é''\033[1;33m',menor,'\033[m''.')
if tecla == 2:
    print('Saindo do programa.')
    print('Programa finalizado.')
    sys.exit()

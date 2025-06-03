# Crie um programa com menu repetitivo (while)
# que leia uma lista de valores indeterminada. Use o
# conceito de CONTADOR e ACUMULADOR e
# apresente no final, a SOMA dos valores e a
# MÉDIA da lista de valores digitados.

import os
import sys

cont = 0 # contador
valor = 0
saldo = 0 # acumular
media = 0

while True:
    os.system('cls')
    menu = '\n1 Ler'
    menu += '\n2 Mostrar'
    menu += '\n3 Sair'
    menu += '\nitem:'
    item = int ( input( menu ))
    if item == 1:
        os.system('cls')
        valor = float (input('Digite o valor:'))
        saldo = saldo + valor # acumular o valor
        cont = cont + 1 # contar valores
        media = saldo / cont # calcular a média acumulada
    elif item == 2:
        print ('\nValor:', valor, ' Cont:', cont, ' Saldo:', saldo , ' Media:', media )
        os.system('sleep 5')
    elif item == 3:
        print ('\nO programa foi finalizado!')
        os.system('sleep 3')
        break
        sys.exit

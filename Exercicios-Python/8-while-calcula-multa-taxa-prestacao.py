#   QUADRO RESUMO
#______________________________________________________________________
#   CRIAR VARIÁVEIS:
#   vlpre = 0, dias = 0, vmulta = 0, juros = 0, vlpagar = 0, contvl = 0.
#   vlac = 0, menu = 0
#______________________________________________________________________
#   LER:
#   vlpre, dias
#______________________________________________________________________
#   CÁCULAR:
#   vmulta = (vlpre * 2) /100
#   juros = ( 1 / 30 ) * dias
#   vlpagar = vlpre + vmulta + juros
#______________________________________________________________________
#   EXIBIR:
#   vlpre, dias, vmulta, juros, vlpagar
#   contvl, vlac
#______________________________________________________________________

import os
import sys

#Variaveis
vlpre = 0
dias = 0
vmulta = 0
juros = 0
vlpagar = 0
contvl = 0
vlac = 0
menu = 0

print("""b) Faça um programa com Menu repetitivo leia o VALOR de uma prestação e a quantidade
de DIAS em atraso. Calcule o valor da MULTA com TXMULTA de 2% sobre o VALOR da prestação,
calcule o valor total de JUROS proporcional aos dias, com TXJUROS de 1% ao mês.
Finalmente calcule o valor a pagar VLPAGAR que será a soma de VALOR + MULTA + 
JUROS. Insira um CONTADOR de valores e um ACUMULADOR de valores, coloque uma 
opção no menu para exibir estas variáveis no final.""")
#os.system('cls')
while True:
    print('\033[1:34m=\033[m' * 25,'\033[1:34mMenu do Programa\033[m','\033[1:34m=\033[m' * 25)
    os.system('cls')
    menu = '\033[1:34m[1]\033[mIncluir '
    menu += '\033[1:33m[2]\033[mMostrar Acumulado '
    menu += '\033[1:31m[3]\033[mSair do Programa'
    menu += '\nOpção:'
    item = int(input(menu))
    if item == 1:
        #Ler
        vlpre = int(input('Digite o valor da prestação: '))
        dias = int(input('Digite a quantidade de dias em atraso: '))

        #Calculos
        vmulta = ((vlpre * 2) / 100)
        juros = ((1 /30) * dias)
        vlpagar = vlpre + vmulta + juros

        #Contador e Acumulado
        contvl = contvl + 1
        vlac = vlac + vlpagar

        #Exibir
        print('_'* 14,'\033[1:36mDetalhamento dos Valores com reajuste\033[m','_'* 15)
        print(f'Prestação R${vlpre:0.2f}\nDias em atraso: {dias}\nValor Multa (2%) R${vmulta:0.2f}\
                \nJuros Proporcional de (1%) ao mês R${juros:0.2f}\nValor à pagar: >>R$\033[4:36m{vlpagar:0.2f}\033[m<<')
        break

    if item == 2:
        #Exibir opção 2
        print('=' * 28, '\033[1:33mAcumulado\033[m','=' * 29)
        print(f'Contagem de Prestações: {contvl}\nValor Acumulado >>R$\033[1:33m{vlac:0.2f}\033[m<<')
        break

    if item == 3:
        #Finaliza Programa
        print('\033[1:31m_\033[m' * 68)
        print('\033[1:31mSaindo do programa!!!\nPrograma finalizado...\033[m\n')
        break
        sys.exit()

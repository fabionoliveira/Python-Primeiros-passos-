# QUADRO RESUMO
# ________________________________________
# CRIAR VARIAVEIS
# sexo = '', sal = 0, saldom = 0, contm = 0, medm = 0,
# saldof = 0, contf = 0, medf = 0, somamf = 0, somasal = 0
# ________________________________________
# LER
# sexo, sal
# ________________________________________
# CALCULO
# contf += 1
# saldof += sal
# medf = saldof / contf
# contm += 1
# saldom += sal
# medm = saldom / contm
# somamf = contm + contf
# somasal = saldom + saldof
# ________________________________________
# EXIBIR
# saldom, medm, contm
# saldof, medf, contf
# somamf, somasal
# ________________________________________

# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-

import sys
import os
#Variáveis Globais
sexo = ''
sal = 0
contf = 0
contm = 0
medf = 0
medm = 0
saldof = 0
saldom = 0
somamf = 0
somasal = 0


def GenSal():
    global sexo
    global sal
    global contf
    global contm
    global saldof
    global saldom
    global medf
    global medm
    global somamf
    global somasal

    #Ler
    sexo = str(input('Digite o sexo (Ex: M/F): '))
    sal = float(input('Digite seu salário R$'))

    #Calculos
    if sexo == 'f' or sexo == 'F':
        contf += 1
        saldof += sal
        medf = saldof / contf

    elif sexo == 'm' or sexo == 'M':
        contm += 1
        saldom += sal
        medm = saldom / contm

    else:
        print('Sexo inválido, digite novamente!')

    somamf = contm + contf
    somasal = saldom + saldof

#Tela de Exibição
def Exibir():
    print('-' * 28, 'Exibir Resultados', '-' * 28)
    print(f'Saldo R${saldom:.2f} e a Média dos Salários dos Homens é R${medm:.2f}')
    print(f'Contagem de Homens: {contm} \n')
    print('-' * 75)
    print(f'Saldo R${saldof:.2f} e a Média dos Salários das Mulheres é R${medf:.2f}')
    print(f'Contagem de Mulheres: {contf}\n')
    print('-' * 75)
    print(f'Saldo de todos Salários R${somasal:.2f}')
    print(f'Contagem de Homens e Mulheres: {somamf}\n')

#Menu Programa
menu = 0
while menu != 3:
    print('=' * 30, 'Menu Programa', '=' * 30)
    menu = int(input('[1]Incluir [2]Exibir [3]Sair\n>>Opção:'))

    if menu == 1:
        GenSal()

    elif menu == 2:
        Exibir()
print('Programa Finalizado')
sys.exit()

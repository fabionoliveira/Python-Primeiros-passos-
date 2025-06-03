# coding: utf-8

import os
import sys

nome = ['Sara Lemes','Ricardo Jafé']
salario = [12000, 10243.20]
idade = [30, 45]
aum = 0


def LerDados():
     
    for i in range(0,len(nome)):
        print(f'\nNome: {nome[i]}\nSalário: {salario[i]:0.2f}\nIdade: {idade[i]}')
        i += 1
        print('-' * 80)

def Exibir():
    for i in range(0,len(salario)):
        if idade[i] >= 18:
            aum = salario[i] * 1.15
            
            print(f'\nNome: {nome[i]}\nSalário: R${salario[i]:0.2f}\nAumento: R${aum:0.2f}\nIdade: {idade[i]}')
            print('-' * 80)

        else:
            print(f'\nNome: {nome[i]}\nSalário: R${salario[i]:0.2f}\nIdade: {idade[i]}')
            print('=' * 80)        

def controle():

    while True:
        print('=' * 30, 'Menu Programa', '=' * 35)
        
        lmenu = '1 Ler Valores Explícitos\n2 Aumento Salário\n3 Sair\nOpção: '
        menu = int(input(lmenu))
        
        if menu == 1:
            print('=' * 30, 'Ler Dados Explícitos','=' * 28)
            LerDados()
            
        elif menu ==2:
            print('=' * 30, 'Aumento Salário','=' * 33)
            Exibir()

        elif menu == 3:
            print('-' * 28, 'Sair Escolhido!!!', '-' * 33)
            print('\nPrograma Finalizado.\n')
            break
                        

controle()
sys.exit()



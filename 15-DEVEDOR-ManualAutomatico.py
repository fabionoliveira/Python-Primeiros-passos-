#coding: utf-8

import os
import time
import sys
import random

ValorDivida = []
DiasAtraso = []
ValorPagar = []
ValorJuros = [] 
ValorMulta = []
nomeDevedor = []

# Incliu para Simples conferencia
ValorTxD = [] # Valor em R$ TX Juros por dia em atraso
SomaVLDiAtraso = [] # Soma valores em R$ dos Atrasados.


def LerDados():
    nome=str(input('Digite Nome: ')).upper()
    nomeDevedor.append(nome)
    divida=float(input('Digite o valor da divida: R$ '))
    ValorDivida.append(divida)
    dias=int(input('Digite quantos Dias de atraso: '))
    DiasAtraso.append(dias)

def DAtraso():
    for i in range(0,len(DiasAtraso)):
                
        if DiasAtraso[i] > 0:
            ValorMulta.append( 2/100 * ValorDivida[i])
            ValorJuros.append( 1/30 * DiasAtraso[i] * ValorDivida[i])
            ValorPagar.append(ValorDivida[i] + ValorJuros[i] + ValorMulta[i])
            ValorTxD.append( 1/30 * DiasAtraso[i])
            SomaVLDiAtraso.append(ValorTxD[i] * DiasAtraso[i])


def DivAuto():
       
    for i in range(0,3):
        ValorDivida.append(round(random.random() * 500,2))
        nome = str(input(f'Digite NOME para a Divida R${ValorDivida[i]:0.2f}: ')).upper()
        nomeDevedor.append(nome)
                
    for i in range(0,3):
        DiasAtraso.append(round(random.random() * 50))
                        
def Exibir():
    for i in range(0,len(nomeDevedor)):
        print(f'Nome Devedor: {nomeDevedor[i]}')
        print(f'Valor Divida..........: R${ValorDivida[i]:0.2f}')
        print(f'Dias de Atraso........: {DiasAtraso[i]} dias.')
        print('---- Taxa por dia e Valor -------------------')
        print(f'Taxa de Juros diária..: R${ValorTxD[i]:0.2f}')
        print(f'Valor dias em Atraso..: R${SomaVLDiAtraso[i]:0.2f}')
        print('---- Multa e Valor a Pagar ------------------')
        print(f'Valor da Multa de (2%): R${ValorMulta[i]:0.2f}')
        print(f'Valor Juros...........: R${ValorJuros[i]:0.2f}')
        print(f'Valor a Pagar.........: R${ValorPagar[i]:0.2f}')
        print('='*45,'\n')
        time.sleep(4)

def Controle():
    while True:
        #os.system('cls')
        print('=' * 80)
        print('>>> OBS: Usar Modo Manual ou Automático. <<<')
        print('=' * 30, 'Menu Programa', '=' * 35)

        lmenu = '1 Inserir Dados Manual\n2 Gera Divida Automático\n3 Exibir\n4 Sair\n>>Opção: '
        menu = int(input(lmenu))
        if menu == 1:
            print('=' * 30, 'Inserir Dados','=' * 35)
            LerDados()

        elif menu == 2:
            print('=' * 30, 'Gerar Divida Automática...','=' * 22)
            DivAuto()
            
        elif menu == 3:
            print('=' * 30, 'Calcular...','=' * 37)
            print('Calculado com Sucesso!!!')
            DAtraso()
            print('=' * 30, 'Exibir Devedores','=' * 32)
            Exibir()
            
        elif menu == 4:
            print('-' * 28, 'Sair Escolhido!!!', '-' * 33)
            print('\nPrograma Finalizado.\n')
            break

Controle()
sys.exit()

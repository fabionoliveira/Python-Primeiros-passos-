# -*- coding: utf-8 -*-

import time
import os
import random

# Cria os vetores de leitura
vetor =[]
doador =[]

# Gera 5 valores de doações com duas casas decimais
def gerarDoações():
    for i in range(0,5):
        vetor.append( round( random.random() * 100, 2) )
        
def lerDoadores():
    for i in range (0, 5):
        nome = input(f'Digite o doador para R$ {vetor[i]}:')
        doador.append(nome)# adiciona doador

def mostrarResultados():
    os.system('cls')
    print('\nLista de Doações por doador\n')
    print('='*40)
    for i in range(0,5):
        print(f'R${vetor[i]} : {doador[i]}')

        print(f'Total de doações: R${sum(vetor)}\nNúmero de doações: {len(vetor)}\nMédia do lote: R$ {round(sum(vetor)/len(vetor), 2)}\nDoação Mínima: R$ {min(vetor)}\nDoação Máxima: R$ {max(vetor)}')
        print('-'* 40,'\n')
        time.sleep(5)



        
    
def controle():
 while True:
     os.system('clear')
     item = int(input('\n***Menu de Controle***\n1 Ler doadores\n2 Resultados\n3 sair\nitem:'))
     if item == 1:
         gerarDoações()
         lerDoadores()

     elif item == 2:
         mostrarResultados()

     elif item ==3:
         break
 
controle()

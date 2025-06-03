# -*- coding: utf-8 -*-
import time
import os
import random

# criando um vetor de 5 valores inteiros
vetor = list ( range(1,6) )

# transformando os valores do vetor em reais

for i, x in enumerate(vetor):
    vetor[i] = round( random.random()*100, 2)

# criando o vetor de doadores vazio
doador=[]

def lerDoadores():
 for i,x in enumerate(vetor):
     nome=input(f'Digite o doador para R$ {vetor[i]} :')
     doador.append(nome) # adiciona doador

def mostrarResultados():
    #os.system('clear')
    print('\n\nLista de Doações por doador\n\n')
    for i in range(0,len(doador)):
        print('='*15, doador[i],'='*15)
        print(f'R${vetor[i]} :{doador[i]}')
        print(f'Total de doações: R$ {round (sum(vetor),2)}\nNúmero de Doações:{len(vetor)}\nMédia do lote: R$ {round (sum(vetor)/len(vetor),2)}\nDoação mínima: R$ {min(vetor)}\nDoação Máxima: R$ {max(vetor)}\n')
        #print(f'','='*15,'{doador[i]}','='*15,'')
    time.sleep(3)
               
def controle():
    while True:
        #os.system('clear')
        item=int(input('\n***Menu de Controle***\n1 Ler doadores\n2 Resultados\n3 sair\nitem:'))

        if item==1:
            lerDoadores()

        elif item==2:
            mostrarResultados()

        elif item ==3:
            break

controle()

#sys.exit()

"""
  Faça um Programa Estrurado com menu repetitivo
usando while, para ler 2 valores, calcular a média e exibir
no final, os valores, a média e o status do aluno. Se a
média for menor que 6 o aluno será reprovado caso
contrário aprovado.



    Quadro Resumo de variáveis
1) n1=0, n2=0, media=0, status = ''
2) n1, n2
3) media=(n1+n2)/2
4) media, status



NOTA: a) Existem Sub Rotinas para Leitura, calcular e para exibir dados.
      b) Você pode criar uma sub rotina def controle() para executar o programa
"""

# -*- coding: utf-8 -*-


import os
import sys


# Criando funções de leitura
def lerN1():
    os.system('cls')
    n1 = float(input('\nDigite a nota 1:'))
    return n1


def lerN2():
    os.system('cls')
    n2 = float(input('\nDigite a nota 2:'))
    return n2


# sub rotina do tipo função para calcular e armazenar a media
def calcMedia(n1, n2):
    media = (n1 + n2) / 2
    return media


# sub rotina comum para exibir a media, produzir e exibir o status do aluno
def mostrar(media):
    #os.system('cls')
    print(f'\nMédia:{media}')

    if media < 6:
        status = 'Aluno Reprovado!'
    else:
        status = 'Aluno Aprovado!'

    print('\nStatus:', status)
    #os.system('sleep 3')


# sub rotina def controle() para executar o programa
# para executar uma função vc deve criar uma variável
def controle():
    itemMenu = 0

    linhasMenu = '\n*** Menu de Controle ***'
    linhasMenu += '\n1 Ler...'
    linhasMenu += '\n2 Calcular...'
    linhasMenu += '\n3 Mostrar...'
    linhasMenu += '\n4 Sair...'
    linhasMenu += '\nSelecione operação:'

    while True:
        os.system('cls')
        itemMenu = int(input(linhasMenu))

        if itemMenu == 1:
            nota1 = lerN1()
            nota2 = lerN2()

        elif itemMenu == 2:
            media = calcMedia(nota1, nota2)
            print('\nMédia calculada com sucesso!')
            #os.system('sleep 2')





        elif itemMenu == 3:
            mostrar(media)
            





        elif itemMenu == 4:
            print('\nO programa foi finalizado')
            #os.system('sleep 2')
            break  # sair do laço infinito

    sys.exit


# Fim da sub rotina controle de menu


# Executando o programa
controle()

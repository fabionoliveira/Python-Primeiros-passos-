#coding: utf-8
"""
Faça um código contendo vetores com valores não explícitos, para armazenar o 
nome, a situação do empregado que poderá ser: “efetivo” ou “estagiário” e a idade. 
A leitura deverá ser feita através de um menu de controle, coloque também uma 
opção para exibir somente os nomes dos estagiários e outra opção para exibir 
somente o nome dos efetivos, finalmente uma opção para exibir os funcionários 
menores de idade.
"""
import os
import sys

n = []
ida = []
sit = []


def InDados():

    nome = str(input('Digite o Nome: ')).upper()
    situacao = str(input('Situação (“efetivo”= F ou “estagiário” = E): ')).upper()
    idade = int(input('Digite a Idade: '))
    n.append(nome)
    sit.append(situacao)
    ida.append(idade)
    
       
def mostrarEfe():
    for i in range(0,len(sit)):
        if sit[i] == 'F':
            print(f'Nome: {n[i]}\n')
        

def mostrarEst():
    for i in range(0,len(sit)):
        if sit[i] == 'E':
            print(f'Nome: {n[i]}\n')
        

def menorIda():
    for i in range(0,len(ida)):
        if ida[i] < 18:
            print(f'Nome: {n[i]}\n')
            
    
def controle():
    while True:
        print('=' * 30, 'Menu Programa', '=' * 35)

        lmenu = '1 Inserir Dados\n2 Efetivos\n3 Estagiários\n4 Menor Idade\n5 Sair\n>>Opção: '
        menu = int(input(lmenu))
        if menu == 1:
            print('=' * 30, 'Inserir Dados','=' * 35)
            InDados()

        elif menu == 2:
            print('=' * 30, 'Efetivos','=' * 40)
            mostrarEfe()

        elif menu == 3:
            print('=' * 30, 'Estagiários','=' * 37)
            mostrarEst()

        elif menu == 4:
            print('=' * 30, 'Menor Idade','=' * 37)
            menorIda()
            
        elif menu == 5:
            print('-' * 28, 'Sair Escolhido!!!', '-' * 33)
            print('\nPrograma Finalizado.\n')
            break

controle()
sys.exit()

        
    

    
 

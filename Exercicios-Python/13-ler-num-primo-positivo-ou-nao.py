# -*- coding: utf-8 -*-
import os
import sys
import time

def LerNum():
    n = int(input('Digite um número: '))

    if n > 0:
        print( f'O número {n} é Positivo.')
        return n
    
    elif n <= 0:
        print('O número Não pode ser "Negativo ou Igual a Zero!!"')
        print('Tente Novamente!!!')
        sys.exit()
         

# função verifica se um número é par ou impar.
def numeroPar(n):
 if n %2 == 0:
     return True
 else:
     return False


# função que verifica se um número é primo ou não.
def numeroPrimo(n):
 contdiv=0; # contar divisores
 for r in range (1, n+1, 1):
     if n % r == 0:
         contdiv +=1; # incrementa 1 ao contdiv
 
 if  contdiv == 2:
     return True # é primo
 else:
     return False # não é primo

#Void soma números Primos.
def somarPrimos ( x, n):
 somarprimos=0
 for r in range (x, n+1):
     if numeroPrimo (r):
         somarprimos += r # acunular os valores primos

 print(f'\nSoma dos números PRIMOS de {x} até {n} é = {somarprimos}.')
    

#Menu de Controle
def MenuPrin():
    menu = 0

    lmenu = '[1]Ler Número. '
    lmenu += '\n[2]Número é Par ou Impar? '
    lmenu += '\n[3]Número é Primo ou Não? '
    lmenu += '\n[4]Somar Números Primos de 1 até Número. '
    lmenu += '\n[5]Sair '
    lmenu += '\n>>Opção: '

    while True:
        #os.system('cls')
        print('')
        print('=' * 30, 'Menu Programa', '=' * 30)
        menu = int(input(lmenu))

        if menu == 1:
            print('-' * 33, 'Incluir', '-' * 33)
            n = LerNum()
                        
        elif menu == 2:
            print('-' * 25, 'O número é Par ou Impar?... ', '-' * 20)
            status = numeroPar (n)
            if status:
                print(f'O número {n} é Par.')
            else:
                print(f'O número {n} é Impar.')
            time.sleep(0.4)

        elif menu == 3:
            print('-' * 27, 'O número É Primo?... ', '-' * 25)
            status = numeroPrimo (n)
            if status:
                print(f'O número {n} é Primo.')
            else:
                print(f'O número {n} não é Primo.')
            time.sleep(0.4)            

        elif menu == 4:
            print('-' * 21, 'Soma dos números Primos... ', '-' * 25)
            exibir = somarPrimos( 1, n)
            
        elif menu == 5:
            print('-' * 28, 'Sair Escolhido!!!', '-' * 28)
            print('Programa Finalizado\n')
            break

MenuPrin()
sys.exit()


"""
menu 1: chama uma função inteira para ler um número inteiro positivo N;
menu 2: chama uma função booleana para saber se o N é par ou ímpar;
menu 3: Chama uma função booleana para analisar se N é primo ou não
menu 4: chama um void para exibir a soma dos números primos de 1 até N.
menu 5: Finalizar Programa. 
"""

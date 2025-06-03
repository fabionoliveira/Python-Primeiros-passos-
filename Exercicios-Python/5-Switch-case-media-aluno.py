import os
import sys
import time

N1=0
N2=0
MG=0
F=0
tecla = 0

os.system('clear');
tecla = int( input ("\nMenu\n1 Executar \n2 Sair\nItem:"))

if tecla == 1:
    N1 = float( input ( "\nDigite n1:"))
    N2 = float( input ( "\nDigite n2:"))
    F = float( input ( "\nDigite as faltas:"))
    MG = (N1 * N2) ** (1/2)

    if MG < 6 or F > 20:
        print( "\nReprovado!")
        print("\nFaltas:", F)
        print(f"\nMédia.:, {MG:.2f}")
    else:
        print (f"\nAprovado!\nMédia:, {MG:.2f}")
        print("\nFaltas:", F)

elif tecla == 2:
    sys.exit()

    


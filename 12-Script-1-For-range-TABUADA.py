import sys
import os


def gerarTabuada ( tabuada ):
    os.system('cls')
    r=1
    for i in range(1,11):
        r = tabuada * i
        print(f'{tabuada} * {i} = {r}')
    #os.system('sleep 5')


def executar():
    tabuada = int (input('Digite a tabuada:'))
    gerarTabuada ( tabuada )


# Execução do programa
executar()
sys.exit

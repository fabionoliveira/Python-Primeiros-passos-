# -*- coding: utf-8 -*-
import sys
import os


def mostrarNãoDivisiveisPor3(x, y):
    for i in range(x, y + 1):
        if i % 3 != 0:
            print(i)


def executar():
    x = int(input("Digite x:"))
    y = int(input("Digite y:"))
    mostrarNãoDivisiveisPor3(x, y)
    sys.exit


# Executando o programa
executar()

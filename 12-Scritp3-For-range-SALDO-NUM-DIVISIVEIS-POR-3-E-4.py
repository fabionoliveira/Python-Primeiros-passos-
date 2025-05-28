# -*- coding: utf-8 -*-
import sys


def saldoDeNumerosDivisiveisPor3e4 ( x , y ):
  saldo=0
  for i in range ( x, y+1 ):
      if i%3==0 and i%4==0:
         print ( i )
         saldo+= i  # acumular o saldo
  return saldo


def executar():
  x = int(input('Digite x:'))
  y = int(input('Digite y:'))
  soma = saldoDeNumerosDivisiveisPor3e4 (x , y)
  print (soma)
  sys.exit


# Executando o programa
executar()

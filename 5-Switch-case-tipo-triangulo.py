# I - Montando a Fórmula    SemPer = (A + B + C) / 2

 

# II - Montando o Quadro Resumo
# 1) A=0, B=0, C=0, Tipo = '', SemPer=0
# 2) A, B, C 

 

# 3) SemPer = (A + B + C ) /2
#    (Obs: O Tipo será processado por IFs/Desvios)

 

# 4) SemPer, Tipo

 

# III - Montando o Diagrama de Blocos

 

# IV - Finalmente Codificar o programa

 

import os
import sys
import time

 

A=0
B=0
C=0
SemPer=0
Tipo = ''

 


A = float (input ('Digite o Lado A:') )
B = float (input ('Digite o Lado B:') )
C = float (input ('Digite o Lado C:') )

 

if A<=0 or B<=0 or C<=0:
   print('Os lados devem ser positivos!')
   sys.exit() # Finaliza o programa aqui mesmo

 

else:
   SemPer = (A+B+C)/2
   
   if A==B and A==C:
      Tipo = 'Equilátero'

 

   elif A!=B and A!=C and B!=C:
      Tipo = 'Escaleno'

 

   else:
      Tipo = 'Isósceles'

 

   print('Semiperimetro',SemPer)
   print('Tipo........:', Tipo)
   sys.exit() # Garantir o término do programa

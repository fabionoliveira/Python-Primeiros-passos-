# 1) nunlados=0,  medlado=0, area=0, p=0, apotema=0
# 2) numlados, medlado
# 3) a=( p*(p-a)*(p-b)*(p-c) ) **(1/2), formula área do triangulo
#    p=(a+b+c) / 2, formula do perimetro do triângulo
#    a=l*l, formula área do quadrado
#    p=l*5, formula perimetro do pentágono
#    a=p*apotema, formula área do pentágono
# 4) Área de triangulo, quadrado, pentagono

import os
import time
import sys

numlados = 0
medlado = 0
area = 0
p = 0
apotema = 0

numlados = float(input('Digite o Número de lados: ' ) )
      
if numlados < 3:
	print('NÃO É UM POLÍGONO')
	print('O Programa será Finalizado, tente novamente!!!')
	time.sleep(5)
	print('Programa Finalizado')
	sys.exit()

elif numlados == 3:
        print('TRIÂNGULO')
        medlado = float(input('Digite a Medida lado: ' ) )
        p = (medlado + medlado + medlado)/2
        area = (p * (p - medlado) * (p - medlado) * (p - medlado) ) ** (1/2)
        print(f'Área do Triângulo é:{area:.2f}')
	
elif numlados == 4:
        print('Quadrado')
        medlado = float(input('Digite a Medida lado: ' ) )
        area = medlado * medlado
        print(f'Área do Quadrado é:{area:.2f}')
	
elif numlados == 5:
        print('PENTÁGONO')
        medlado = float(input('Digite a Medida lado: ' ))
        apotema = ( medlado / 2 ) / 72
        p = medlado * 5 
        area = (p * apotema) / 2
        print(f'Área do Pentágono é:{area:.2f}')

else:
	print('POLÍGONO NÃO IDENTIFICADO')
	print('O Programa será Finalizado, tente novamente!!!')
	time.sleep(5)
	print('Programa Finalizado')
	sys.exit()

import os
import time
import sys


a = 0
b = 0
c = 0
triangulo = False
p = 0
semper = 0
area = 0
tipo = ''
tecla = 0

tecla = int(input("\n============== Menu do Programa =============\n[1]->Ler,Cálcular,Exibir [2]->Sair do Programa\n>>> Opção:"))
    
if tecla == 1:
    print('-*-* Informe as medidas para A, B, C *-*-')
    a = int(input('Digite a medida para A: '))
    b = int(input('Digite a medida para B: '))
    c = int(input('Digite a medida para C: '))

    p = a + b + c
    semper = (a + b + c)/2
    area = (p * (p - a) * (p - b) * (p - c) ) ** (1/2)
    triangulo = a < (b + c) and b < (a + c) and c < (a + b)

    print('\n-*-* Cálculando... *-*-')

    if triangulo == False:
        print('\nTriângulo igual a:>>',triangulo,'<<')
        print('\n"Uma figura qualquer de três lados."')
        print('Tente novamente!!!')
        print('Programa finalizando.')
        sys.exit()
                        
    if a == b and a == c:
        print('É um Triângulo.')
        tipo = 'Equilátero'
        print('\n-*-* Tela de Resultados *-*-')
        print('O Triângulo é >>',tipo,'<<')
        print(f'O semiperimetro do Triângulo é: {semper:.2f}cm')
        print(f'Área do Triângulo é: {area:.2f} cm quadrado')
        print('=============================================')
            
    elif a != b and a != c and b != c:
        print('É um Triângulo.')
        tipo = 'Escaleno'
        print('\n-*-* Tela de Resultados *-*-')
        print('O Triângulo é >>',tipo,'<<')
        print(f'O semiperimetro do Triângulo é: {semper:.2f}cm')
        print(f'Área do Triângulo é: {area:.2f} cm quadrado')
        print('=============================================')

    elif a == b and a != c or a == c and b != c or b == c and b != a:
        print('É um Triângulo.')
        tipo = 'Isósceles'    
        print('\n-*-* Tela de Resultados *-*-')
        print('O Triângulo é >>',tipo,'<<')
        print(f'O semiperimetro do Triângulo é: {semper:.2f}cm')
        print(f'Área do Triângulo é: {area:.2f} cm quadrado')
        print('=============================================')
        
if tecla == 2:
    print('Saindo do programa!!!')
    print('Programa finalizado.')
    sys.exit()



        

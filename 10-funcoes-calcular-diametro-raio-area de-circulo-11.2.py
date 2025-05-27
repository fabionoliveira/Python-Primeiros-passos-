"""
2. Fazer o quadro resumo, diagrama de blocos e código fonte de um
programa que leia o Comprimento, calcule o diâmetro, o raio e a área de
um círculo. Ao final exiba Diâmetro, Raio e Área. (Faça um menu com as
opções necessárias para executar as sub rotinas. )
 Fórmulas que serão usadas: diametro=comprimento / 3.14
 raio=diametro / 2, area=raio * raio * 3.14
_________________________________________________________
QUADRO RESUMO
1	Criar variáveis
    comp = 0, diam = 0, raio = 0, area = 0, menu = 0
2	Ler
	comp
3	Cálculos
    diametro=comprimento / 3.14,
    raio=diametro / 2,
    area=raio * raio * 3.14
4	Exibir
	diam, raio, area
"""
import os
import sys

def Ler():
    comp = float(input('Digite o Comprimento: '))
    print(' ')
    return comp


def CalDiam(comp):
    diam = comp / 3.14
    return diam


def CalRaio(diam):
    raio = diam / 2
    return raio


def CalArea(raio):
    area = raio * raio * 3.14
    return area


def Exibir(diam, raio, area):
    print('As informações após Cálculos do >>Comprimento<< digitado de um Circulo são:')
    print(f'Diâmetro: {diam:0.3f}\nRaio....: {raio:0.3f}\nÁrea....: {area:0.3f}\n')


def MenuPrin():
    menu = 0

    lmenu = '[1]Incluir '
    lmenu += '[2]Calcular '
    lmenu += '[3]Exibir '
    lmenu += '[4]Sair '
    lmenu += '\n>>Opção: '

    while True:

        print('=' * 30, 'Menu Programa', '=' * 30)
        menu = int(input(lmenu))

        if menu == 1:
            print('-' * 33, 'Incluir', '-' * 33)
            comp = Ler()


        elif menu == 2:
            print('-' * 31, 'Calcular... ', '-' * 30)
            diam = CalDiam(comp)
            raio = CalRaio(diam)
            area = CalArea(raio)
            print('Diâmetro, Raio e Área de um Circulo calculados com sucesso!!\n')

        elif menu == 3:
            print('-' * 28, 'Exibir Resultados', '-' * 28)
            Exibir(diam, raio, area)

        elif menu == 4:
            print('-' * 28, 'Sair Escolhido!!!', '-' * 28)
            print('Programa Finalizado')
            break
    sys.exit()


MenuPrin()

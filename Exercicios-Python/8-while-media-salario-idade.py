#   QUADRO RESUMO
#______________________________________________________________________
#   CRIAR VARIÁVEIS:
#   nome='', sal = 0, ida = 0, contpes = 0, medsal = 0, medida = 0,
#   somasal = 0, somaida = 0
#______________________________________________________________________
#   LER:
#   nome, sal, ida
#______________________________________________________________________
#   CÁCULAR:
#   contpes = contpes + 1
#   somasal = somasal + sal
#   somaida = somaida + ida
#   medsal = somasal / contpes
#   medida = somaida / contpes
#______________________________________________________________________
#   EXIBIR:
#   contpes , somasal, somaida, mediasal, medida
#______________________________________________________________________
import os
import sys

nome = ''
sal = 0
ida = 0
contpes = 0
medsal = 0
medida = 0
somasal = 0
somaida = 0

while True:
    print('=' * 25, 'Menu do Programa', '=' * 25)
    os.system('cls')
    menu = int(input('[1] Incluir Dados [2] Mostrar Dados coletados [3] Sair do Programa\n>>> Opção:'))
    if menu == 1:
        print('=' * 68)
        print('_' * 17,' !!! Informe os dados abaixo. !!!','_' * 16)
        nome = str(input('Digite seu nome: '))
        ida = int(input('Digite sua idade com "formato numérico" exemplo 33:'))
        if ida >= 100:
            print('Nossa você é super idoso!')
        sal = float(input('Digite o valor de seu salário R$'))
        contpes = contpes + 1
        somasal = somasal + sal
        somaida = somaida + ida
        medsal = somasal / contpes
        medida = somaida / contpes

    elif menu == 2:
        print('_' * 68)
        print('*' * 26, 'Dados coletados','*' * 25)
        print(f'\nQuantidade de pessoas......{contpes}')
        print(f'Total soma dos salários R${somasal:8.2f}')
        print(f'Total soma das Idades......{somaida}')
        print (f'Média dos salários .....R${medsal:8.2f}')
        print(f'Média das idade............{medida:3}\n')
        print('=' * 68)
        break
        
        

    elif menu == 3:
        print('_' * 68)
        print('Saindo do programa!!!\nPrograma finalizado...\n')
        sys.exit()

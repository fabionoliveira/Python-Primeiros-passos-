import os
import time
import sys

ano = 0
msg = ''
tecla = 0

os.system('cls')

tecla = int(input('\n=============== Menu do Programa ===============\n[1] Executar [2] Sair do Programa\n>>> Opção: '))

if tecla == 1:

    print('\n-*-*-*-*-*-*-*-* Informe o Ano  *-*-*-*-*-*-*-*-')
    ano = int(input('Digite um ano qualquer [ex: 1547]: '))    

    if ano <= 0:
        print('\nAno Negativo não existe tente novamente!!')
        print('\nO programa será finalizado.\nPrograma finalizado.\n')
        sys.exit()

    if ano % 4 == 0:
        msg = 'é bissexto.'

    else:
        msg = 'não é bissexto.'

    print('\n-*-*-*-*-*-*-* Tela de Resultados *-*-*-*-*-*-*-')
    print('Ano digitado',msg,'\n')

if tecla == 2:
    print('________________________________________________')
    print('Saindo do programa.')
    print('Programa finalizado.\n')
    sys.exit()

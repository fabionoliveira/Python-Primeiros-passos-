# Meu script python
# Aluno: FABIO NUNES DE OLIVEIRA
# Atividade E pag 41

import os # Módulo do Systema Operacional
import time # Módulo time - Funções de tempo
import sys # Finaliza o programa

# Minhas variáveis e constantes
a=' '
b=' '
c=' '
d= ''
r1= ''
r2= ''

# Leitura ou Entrada de Dados
os.system('cls'); # apaga a tela no windows
a=float(input('Digite o valor diferente de ZERO para a:'))
b=float(input('Digite o valor para b:'))
c=float(input('Digite o valor para c:'))

# Cálculos Processamento
if a == 0:
   print('O valor Digitado para "a" é ZERO, o programa será finalizado!!!')
   time.sleep(5)
   print('O programa foi finalizado')
   sys.exit ()
   
else:
    d= (b**2 -4 * a * c)
    r1= (-b + (d**(1/2))) / (2 * a)
    r2= (-b - (d**(1/2))) / (2 * a)

print('\n**** Tela de Resultado das Raizes ****')

print('O valor de Delta é:' , d)

print('O valor de Raiz 1 é: ' , r1)

print('O valor de Raiz 2 é: ' , r2)

time.sleep(5) # pausa de 5 segundos
print('O programa foi finalizado')
sys.exit () #Finaliza programa


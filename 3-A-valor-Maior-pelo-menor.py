# Meu script python
# Aluno: FABIO NUNES DE OLIVEIRA
# exercício (4) da página 41 do livro Estudo Dirigido de Algoritmos

#a. Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor

import os # Módulo do Systema Operacional
import time # Módulo time - Funções de tempo
import sys # Finaliza o programa

# Variáveis e Constantes

n1=0
n2=0
r=''

# Leitura ou Entrada de Dados
os.system('cls')
n1=float (input('Digite o 1º valor:' ))
n2=float (input('Digite o 2º valor:' ))

# Cálculos Processamento
os.system('cls')
if n1 > n2:
   r=n1-n2

else:
     r=n2-n1     

# Mostrar os resulados para o usuário
print('\n**** Tela Resultado ****')

print ('O resultado do valor Maior pelo menor é:' , r )

time.sleep(5) # pausa de 5 segundos
print('O programa foi finalizado')
sys.exit

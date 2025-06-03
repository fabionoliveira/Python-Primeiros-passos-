# Meu script python
# Aluno: FABIO NUNES DE OLIVEIRA
# Atividade B

import os # Módulo do Systema Operacional
import time # Módulo time - Funções de tempo
import sys

# Minhas variáveis e constantes
v=' '

# Leitura ou Entrada de Dados
os.system ('cls')
v= int(input('Digite um valor inteiro positivo ou negativo:' ))


# Cálculos Processamento
if v < 0:
	v=(v) * (-1)

# Mostrar os resulados para o usuário	
print('\n**** Tela de Resultado ****')
print('O Valor é:', v)

time.sleep(5) # pausa de 5 segundos
print('O programa foi finalizado')
sys.exit

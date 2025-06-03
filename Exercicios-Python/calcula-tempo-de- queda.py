# Meu script python
# Aluno: FABIO NUNES DE OLIVEIRA
# Atividade C 25-02-21

import os # Módulo do Systema Operacional
import time # Módulo time - Funções de tempo

# Minhas variáveis e constantes
g=10
a=0.0
tq=0.0

# Leitura ou Entrada de Dados
a= input('Digite a Altura:') # ler o valor da altura

# Cálculos Processamento
tq= ((2 * float(a))**(1/2)) /g # calcula o tempo queda
     
os.system("cls") # apaga a tela no windows 
print('\n') # pula uma linha

# Mostrar os resulados para o usuário
print (f'O Tempo de Queda é: {tq: .4f} ') #exibe o tempo queda

time.sleep(5) # pausa de 5 segundos
print('O programa foi finalizado')

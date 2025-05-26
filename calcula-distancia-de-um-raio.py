# Meu script python
# Aluno: FABIO NUNES DE OLIVEIRA
# Atividade B 25-02-21

import os # Módulo do Systema Operacional
import time # Módulo time - Funções de tempo

# Minhas variáveis e constantes
t=0
v=340
d=0

# Leitura ou Entrada de Dados
t= input('Digite Tempo:') # ler o valor de tempo

# Cálculos Processamento
d= float (t) * float(v) # calcula a distancia

os.system("cls") # apaga a tela no windows 
print('\n') # pula uma linha

# Mostrar os resulados para o usuário
print (f'Distância de um Raio é: {d: .1f} metro(s) ') #exibe distancia

time.sleep(5) # pausa de 5 segundos
print('O programa foi finalizado')

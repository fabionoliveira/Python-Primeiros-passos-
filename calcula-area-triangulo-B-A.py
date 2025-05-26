# Meu script python
# Aluno: FABIO NUNES DE OLIVEIRA
# Atividade A 25-02-21

import os # Módulo do Systema Operacional
import time # Módulo time - Funções de tempo

# Minhas variáveis e constantes
b=0
a=0
t=0

# Leitura ou Entrada de Dados
b= input('Digite a Base:') # ler o valor de base
a= input('Digite a Altura:') # ler o valor da altura

# Cálculos Processamento
t=(float(b) * float(a)) /2 # calcula a area triangulo

os.system('cls'); # apaga a tela no windows 
print('\n') # pula uma linha

# Mostrar os resulados para o usuário
print (f'O valor da área do Triângulo é: {t: .2f} ') #exibe area do triangulo

time.sleep(5) # pausa de 5 segundos
print('O programa foi finalizado')

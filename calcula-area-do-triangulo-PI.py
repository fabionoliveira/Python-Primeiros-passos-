# Meu script python
# Aluno: FABIO NUNES DE OLIVEIRA
# Atividade D 25-02-21

import os # Módulo do Systema Operacional
import time # Módulo time - Funções de tempo

# Minhas variáveis e constantes
d=0
p=0
r=0
a=0
pi=3.14

# Leitura ou Entrada de Dados
p= input('Digite Perimetro:') # ler o perimetro

# Cálculos Processamento
d=float(p) / pi # calcula diametro
r= float(d) / 2 # calcula o raio
a=(float (r) * float(r)) * pi # calcula a area 

os.system("cls") # apaga a tela no windows 
print('\n') # pula uma linha

# Mostrar os resulados para o usuário
print (f'O valor da Área é: {a: .2f} ') #exibe area do triangulo

time.sleep(5) # pausa de 5 segundos
print('O programa foi finalizado')

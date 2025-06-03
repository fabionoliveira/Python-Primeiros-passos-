# Meu Script Python
# Aluno Fabio Nunes

# 1 Constantes e variáveis
tempo = 0
velocidade = 0
distancia = 0
litros_usados = 0

#Leitura variaveis
tempo = input('Digite o Tempo gasto:')
velocidade = input('Digite a Velocidade Média:')

# 2 Calculos
distancia = float(tempo) * float(velocidade)
litros_usados = float(distancia) / 12

# 3 Exibir Resultado

print('Velocidade Média foi de:', velocidade, 'km/h')
print('Tempo gasto foi de:',tempo, 'hora(s)')
print('Distancia percorrida foi de:', distancia,'km')
print('Litros usado na viagem Foi de:', litros_usados, 'litro(s)')
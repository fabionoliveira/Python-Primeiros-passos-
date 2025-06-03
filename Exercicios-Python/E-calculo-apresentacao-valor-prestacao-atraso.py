# Meu Script Python
# Aluno Fabio Nunes

# 1 Constantes e variáveis
v=0
tx=0
tp=0
prestacao=0

#Leitura variaveis
v=input('Digite o Valor R$:')
tx=input('Digite a Taxa %:')
tp=input('Digite o Tempo meses:')

# 2 Calculos
prestacao=float(v) + (float(v) * float(tx) /100) * float(tp)

# 3 Exibir Resultado 
print('A Prestação é:', prestacao)
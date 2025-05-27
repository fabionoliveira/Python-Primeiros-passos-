import os
import sys

nome = ''
email = ''
ida = 0
tel = ''
rua = ''
num = ''
cep = ''
bai = ''
cid = ''
est = ''
pais = ''
sal = 0
texto = ''

print("""\nFaça um programa para ler os dados de uma pessoa: nome, email, idade, 
telefone, rua, número, cep, bairro, cidade, estado, país e salário. No final exiba 
um texto de apresentação dessa pessoa usando as regras de formatação/composição 
de strings aprendidas nesta aula. Cada variável deverá ter o seu respectivo datatype,
ou seja, idade será número inteiro, nome será string, salário será decimal, etc…\n""")

os.system('cls')
print('=' * 15, 'Menu do Programa','=' * 15)

menu = int(input('[1] Executar [2] Sair do Programa\n>>> Opção:'))

if menu == 1:
    print('\n!!! Informe os dados para preencher o "Texto" abaixo. !!!')
    nome = str(input('Digite seu Nome:')).rstrip()
    email = str(input('Digite seu E-mail:')).strip()
    ida = int(input('Digite sua Idade:'))
    tel = str(input('Digite número de Telefone:')).strip()
    rua = str(input('Digite o nome da Rua:')).strip()
    num = str(input('Digite o Número:')).strip()
    cep = str(input('Digite o CEP:')).strip()
    bai = str(input('Digite o Bairro:')).strip()
    cid = str(input('Digite a Cidade:')).strip()
    est = str(input('Digite o Estado:')).strip()
    pais = str(input('Digite o País:')).strip()
    sal = float(input('Digite o valor de seu Salário R$:'))

    texto = f'Meu nome é {nome:10}, meu e-mail é {email:10},\ntenho {ida:03} ano(s) de idade, meu telefone é ({tel[0:2]}){tel[2:7]}-{tel[7:11]},' \
            f'\ne moro na rua {rua:10}, número {num:5}, CEP: {cep[0:5]}-{cep[5:8]},' \
            f' \nno Bairro {bai:10} em {cid:10}, no estado de {est:10},\nque fica no país {pais:10}, e recebo um salário de R${sal:8.2f}.'

    print('\n','-*' * 10, 'Texto', '*-' * 10)

    print(texto)

if menu == 2:
    print('_' * 49)
    print('Saindo do programa!!!\nPrograma finalizado...\n')
    sys.exit()



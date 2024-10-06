import math

'''1. Escreva um programa que receba 2 números de sua escolha e que depois imprima a soma, a subtração, multiplicação, divisão, divisão inteira, o resto da divisão do maior pelo menor e coloque na mensagem a palavra resto ao invés de símbolo %.

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

print(f'\nO resultado da soma de {x} + {y} =', x + y)
print(f'O resultado da subtração de {x} - {y} =', x - y)
print(f'O resultado da multiplicação de {x} x {y} =', x * y)
print(f'O resultado da divisão de {x} por {y} =', x / y)
print(f'O resultado da divisão inteira de {x} por {y} = {math.trunc(x / y)}')
print(f'O resto da divisão de {x} por {y} =', x % y)

#2. Faça um programa que peça as 4 notas bimestrais e mostre a média do aluno

n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))
n4 = int(input('Nota 4: '))
media = (n1 + n2 + n3 + n4) / 4

print(f'A média do aluno é {media}')

#3. Crie um script Python que leia o dia, mês e ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

dia = int(input('Dia em formato DD: '))
mes = int(input('Mês em formato MM: '))
ano = int(input('Dia em formato AAAA: '))

print(f'Data de nascimento: {dia}/{mes}/{ano}')

#4. Organize os números 2,3,4,5,10,12 para obter a saída (resposta) 18 em uma única operação

print(f'12 + 10 - 4 - 3 - 2 + 5 = {12 + 10 - 4 - 3 - 2 + 5}')

#5. Crie um programa que leia o nome completo de uma pessoa e mostre: a) O nome com todas as letras maiúsculas e minúsculas b) Quantas letras ao todo c) Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
primeiro_nome = nome.split()[0]

print(f'\na) Maiúsculo: {nome.upper()}, minúsculo: {nome.lower()}')
print(f'b) Seu nome possui {len(nome)} letras')
print(f'c) Seu primeiro nome possui {len(primeiro_nome)} letras')'''

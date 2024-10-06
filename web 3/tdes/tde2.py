'''1. Faça um programa que sorteia um número de 0 a 9999 e mostre na tela cada
um dos dígitos separadamente.exemplo: unidade: 4 dezena: 3 centena: 8 milhar

import math

num = random.randint(0, 9999)

numero = f'{numero:04d}'

milhar = numero[0]
centena = numero[1]
dezena = numero[2]
unidade = numero[3]

# Exibe os resultados
print(f'Número: {num}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')'''

'''2. Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até
200Km e R$0,45 para viagens mais longas.

dist = int(input('Qual a distancia? '))

if dist <= 200:
    preco = 0.50 * 200
else:
    preco = 0.45 * dist

print(f'Preço total = {preco}')'''

'''3. Uma loja fornece 10% de desconto para funcionários e 5% de desconto para
clientes vips. Faça um programa usando while que calcule o valor total a ser
pago por uma pessoa. O programa deverá ler o valor total da compra
efetuada e um código que identifique se o comprador é um cliente comum (1)
, funcionário (2) ou vip(3) .

cargo = int(input('Qual seu cargo(cliente comum(1), funcionário(2) ou vip(3): '))
valorT = float(input('Valor da compra? '))

if cargo == 2:
    valorT *= 0.9
elif cargo == 3:
    valorT *= 0.95
else:
    valorT = valorT

print(f'Cargo: {cargo}, valor total: {valorT}')'''

'''4. Dado o valor do produto e a forma de pagamento.
1= à vista;
2= à prazo.
Se o produto for pago à vista aplique um desconto de 10% antes de mostrar
o valor final, senão informe o mesmo valor do produto.

f = int(input('Qual a forma de pagamento(1 - a vista, 2 - a prazo)? '))
preco = float(input('qual o valor? '))

if f == 1:
    preco *= 0.9
else:
    preco = preco

print(f'Valor final: {preco}')'''

'''5.Crie um programa que leia o conceito de um aluno na disciplina Desenv Web 3
e imprima seu significado, de acordo com a tabela abaixo. Caso seja informado um
conceito inexistente, deve ser exibida uma mensagem de erro.
Conceito Significado
A Excelente
B Ótimo
C Bom
D Regular
E Ruim
F Nos vemos de novo ano que vem...

c = input('Qual seu conceito? ')

if c == 'A' or c == 'a':
    print('Excelente!')
elif c == 'B' or c == 'b':
    print('Ótimo!')
elif c == 'C' or c == 'c':
    print('Bom')
elif c == 'D' or c == 'd':
    print('Regular')
elif c == 'E' or c == 'e':
    print('Ruim')
elif c == 'F' or c == 'f':
    print('Nos vemos ano que vem...')
else:
    print('Erro.')'''

'''6. Dada uma letra, escreva na tela se essa letra é uma vogal ou consoante
(considerar apenas letras minúsculas).

l = input('Digite uma letra: ')

if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
    print('Vogal')
else:
    print('Consoante')'''

'''7. Crie um programa usando o for que leia uma lista. Mostre apenas os
números pares. Esta lista deve ser assim: [1, 2, 3, 4, 5, 6, 7, 8, 9]; 7. Faça um
programa usando o for que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Números pares:")
for num in num:
    if num % 2 == 0:
        print(num)'''

'''8. Faça um programa usando o for que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando uma mensagem
de erro e voltando a pedir as informações.'''



'''9. Faça um programa usando o for que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.'''



'''10.Faça um programa usando o for que calcule o número médio de alunos por
turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para
cada turma. As turmas não podem ter mais de 40 alunos.'''

numT = int(input("Digite o número de turmas: "))

totalA = 0
turmasS = 0

for i in range(numT):
    while True:
        alunos = int(input(f"Digite a quantidade de alunos na turma {i + 1}: "))

        if 0 <= alunos <= 40:
            totalA += alunos
            turmasS += 1
            break
        else:
            print("Erro: A turma não pode ter mais de 40 alunos. Tente novamente.")

if turmasS > 0:
    mediaA = totalA / turmasS
else:
    mediaA = 0

print(f"Média de alunos por turma: {mediaA:.1f}")
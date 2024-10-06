#Condicionais if/else/elif --------------------------------------
'''
idade = int(input('Digite a sua idade'))

if idade >= 18:
    print(f'A idade {idade}, você é maior de idade ')
else:
    print(f'A idade {idade}, você é menor de idade ')

#-----------------------------------------------------------

num = int(input("Digite um numero "))

if num >= 10:
    print(f'O numero {num} é maior ou igual 10')
else:
    print(f'O numero {num} é menor ou igual a 10')

#----------------------------------------------------------

nome = input('Digite o seu nome')
if nome == 'Thereza':
    print('Esse nome é marivilhoso!')
    print(f'Bom dia {nome}!')
else:
    print(f'Bom dia {nome}!')

#-----------------------------------------------------------

d = int(input('Digite o valor de d'))
e = int(input('Digite o valor de e'))

if d > e:
    print(f'O valor de {d} > {e}')
elif d == e:
    print(f'O valor de {d} = {e}')
else:
    print(f'Não atende a nenhuma das premissas')

# ----------------------------------------------------------

nota = float(input('Digite a nota do aluno'))

if nota >= 9:
    print(f'Parabéns!A nota do aluno foi {nota}, conceito A')
elif nota >= 8:
    print(f'Bom trabalho!A nota do aluno foi {nota}, conceito B')
elif nota >= 7:
    print(f'A nota do aluno foi {nota}, conceito C')
elif nota >= 6:
    print(f'Cuidado!A nota do aluno foi {nota}, conceito D')
else:
    print(f'Reprovado :(!A nota do aluno foi {nota}, conceito E')

#------------------------------------------------------------------------------
x = float(input('Digite o valor de x'))
y = float(input('Digite o valor de y'))

res = 0
op = input('Digite a operação desejada + ,- , *, /')

if op =='+':
    res = x + y
    print(f'A soma de {x} + {y} = {res}')
elif op =='-':
    res = x - y
    print(f'A subtração de {x} - {y} = {res}')
elif op =='*':
    res = x * y
    print(f'A mulitplicação de {x} * {y} = {res}')
elif op =='/':
    res = x / y
    print(f'A divisão de {x} / {y} = {res}')
print('Término do programa!Volte sempre!')

#-----------------------------------------------------------------------------------

z = float(input('Digite o valor de z'))

if z <= 10 and z % 2 == 0:
    print(f'O valor de {z} é menor ou igual a 10 e é par')
else:

#For ------------------------------------------------------------------------------

e = 10
for i in range(e):
    print('Olá')
#-------------------------------------------------------------------
for n in range(1,8):
    print(f'O valor de {z} não é menor ou igual a 10 e ou não é par')
    print(f'Numero {n}')
#-------------------------------------------------------------------

for num in range(1,10):
    if num % 2 == 0:
        print(f'O numero {num} é par')
    else:
        print(f'O numero {num} é impar')

#---------------------------------------------------------------------

for n1 in range(10,30,3):
    print(f'Numero: {n1}')

for n2 in range(30,10,-2):
    print(f'Numero: {n2}')

#exemplo de break ------------------------------------------------------

for n3 in range(10):
    if n3 > 7:
        break
    print(f'Numero: {n3}')
print('Fim')

#exemplo de continue ---------------------------------------------------

for n4 in range(20,30):
    if n4 == 25:
        continue
    print(f'Numero: {n4}')
print('Fim')

#exemplo de tabuada ----------------------------------------------------

v = int(input('Digite um numero para calcular a tabuada'))

for t in range(0,11):
    print(f'{v} * {t} = {v * t}')'''










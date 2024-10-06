#comentário de 1 linha
'''comentário de multiplas linhas'''
'''
print('Olá Mundo!')
print(3 + 5)
print(True)

print('Olá!\nBom dia!\nSejam Bem Vindos de novo!')
print( 3 + 3)
print('4' + '4')
#print('Olá' + 5) não pode concatenar string com valor numerico usando o +, somente com a virgula
print('Olá' , 5)
print( 3 , 3)
print('4' , '4')

#Variavel ----------------------------------------------------------

a = 10
print('o valor da variavel =',a)

b= 4
c = 10.22589

print('O valor de a',a,'\nO valor de b',b,'\nO valor de c',c)
print('O valor de a é {}'.format(a),'\nO valor de b é {}'.format(b),'\nO valor de c é {}'.format(c))
print(f'O valor de a é {a}')
print(f'O valor de a é {a}, o valor de {b}, o valor de {c}')

#exemplo de definição de casas decimais

print('O valor de c {:.2f}'.format(c))
print(f'O valor de c {c:.2f}')

soma = a + b + c
print('A soma dos valores = {:.1f}'.format(soma))
print(f'A soma dos valores = {soma:.2f}')

print('A soma dos valores = {}'.format(a + b))
print(f'A soma dos valores = {a + b}')

#outra maneira de se declarar variavel-------------------------------------------------

n1,n2,n3,n4 = 10,20,30,40

print('A soma dos valores = {}'.format(n1 + n2 + n4))
print(f'A soma dos valores = {n1 + n2 + n3 + n4}')

#exemplo de operadores aritméticos -------------------------------------------------

s = n1 + n2 + n3 + n4
sub = n1 - n3
mult = n1 * n4
div = n2 / n4
r = n1 % n2     # resto da divisão
i = n1 // n4    #inteiro da divisão

print('A soma dos valores = {}'.format(s))
print(f'A soma dos valores = {s}')

print('A subtração dos valores = {}'.format(sub))
print(f'A subtração dos valores = {sub}')

print('A multiplicação dos valores = {}'.format(mult))
print(f'A multiplicação dos valores = {mult}')

print('A divisão dos valores = {}'.format(div))
print(f'A divisão dos valores = {div}')

print('O resto da divisão = {}'.format(r))
print(f'O resto da divisão = {r}')

print('O valor inteiro da divisão = {}'.format(i))
print(f'O valor inteiro da divisão = {i}')

# recebendo valores externos --------------------------------------------------------

v1 = int(input('Digite o valor de v1'))
v2 = float(input('Digite o valor de v2'))

print('A divisão de {} / {} = {}'.format(v1,v2,v1/v2))
print(f'A divisão de {v1} / {v2} = {v1/v2}')

print('A multiplicação de {} * {} = {}'.format(v1,v2,v1*v2))
print(f'A multiplicação de {v1} * {v2} = {v1*v2}')

#outra maneira de converter de string para int ou float ---------------------------
'''
v3 = input('Digite o valor de v3')
v4 = input('Digite o valor de v4')

v3 = int(v3)
v4 = float(v4)

print('A divisão de {} / {} = {}'.format(v3,v4,v3/v4))
print(f'A divisão de {v3} / {v4} = {v3/v4}')

#Operadores relacionais >,<,>=,<=,==,!= ----------------------------------------------

print('O valor de v3 {} é igual o valor de v4 {}? {}'.format(v3,v4,v3 == v4))
print(f'O valor de {v3} é igual o valor de {v4}? {v3 == v4}')
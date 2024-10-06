#_*_coding:utf-8_*_
#Operadores Relacionais >,<,>=,<=,== -------------------------
'''
a,b = 5,9
print('O valor de a e b são iguais?{}'.format(a == b))
print(f'O valor de a a e b são iguais?{a == b} ')

print('O valor de a  é maior que b?{}'.format(a > b))
print(f'O valor de a é maior que b? {a > b} ')

print('O valor de a  é menor que b?{}'.format(a < b))
print(f'O valor de a é menor que b? {a < b} ')

#Operadores logicos and(e), or(ou), not(negação) --------------

idade = 50
totalcompra = 200

print(idade == 50 and totalcompra == 200)
print(idade >= 50 and totalcompra >=200)
print(idade >= 50 or totalcompra >= 200)

x = True
print(not x)

#Operadores de associação in (está dentro do parametro), not in(não está dentro do parametro)

fruta = ['pera','maça','uva']
print('uva' in fruta)
print('banana' not in fruta)

num = [1,2,3,4,5]
print(5 in num)
print(2 not in num)

#Operador diferente != -----------------------------------------------------

c = 10
d = 12
print(c != d)'''

#math ---------------------------------------------------------------------

#potência - pow() ---------------------------------------------------------

import math

#x = int(input('Digite um numero '))
#y = int(input('Digite o valor da potência '))

'''print('O numero {} elevado {} = {}'.format(x,y,math.pow(x,y)))
print(f'O numero {x} elevado{y} = {math.pow(x,y)}')

p = math.pow(x,y)

print('O numero {} elevado {} = {}'.format(x,y,p))
print(f'O numero {x} elevado{y} = {p:.0f}')

#raiz quadrada - sqrt() ----------------------------------------------------

r = math.sqrt(x)
print('A raiz quadrada de {} = {}'.format(x,r))
print(f'A raiz quadrada de {x} = {r:.0f}')

#trunc() - traz somente a parte inteir a do numero -------------------------

x1= float(input('Digite um numero '))
print('O valor inteiro {} = {}'.format(x1,math.trunc(x1)))
print(f'O valor inteiro de {x1} = {math.trunc(x1)}')

#outra maneira de importar um modulo ---------------------------------------

from math import trunc,pow,sqrt

x1= float(input('Digite um numero '))
print('O valor inteiro {} = {}'.format(x1,trunc(x1)))
print(f'O valor inteiro de {x1} = {trunc(x1)}')

#random() - numeros aleatorios --------------------------------------------

import random

r = random.random()
print(f'O numero aleatório é {r:.1f}')
from random import random,randint,randrange,uniform,choice

r1 = random()
print(f'O numero aleatório é {r1:.1f}')

#definido intervalo  ----------------------------------------------------

print(random() * 10)

print(randint(0,11))

z = randint(0,11)#numeros aleatorios inteiro
print(f'O numero aleatório inteiro {z}')

print(randrange(0,10,2))#definindo valor inicial,final,incremento

print(f'{uniform(5,10):.1f}') #numeros flutuantes definindo intervalo

m = [1,2,3,5,8,9,6,12,58]
print(choice(m)) #escolhe a partir da lista existente um valor aleatório

cor = ['verde','amarelo','roxo','azul','lilas']
print(choice(cor))

import random

cor = ['verde','amarelo','roxo','azul','lilas']
random.shuffle(cor) # embaralha a lista
print(cor)

#Analisar string ------------------------------------------------------------

#len() - quantidade de caracteres de uma string -----------------------------

nome = input('Digite o seu nome')

l = len(nome)
print('O nome da pessoa é {} e possui {} caracteres'.format(nome,len(nome)))
print(f'O nome da pessoa é {nome} e possui {len(nome)} caracteres')

#upper() - coloca tudo em maiusculo ----------------------------------------------

print(f'O nome em maiusculo {nome.upper()}')

#lower() - coloca tudo em minusculo ----------------------------------------------

print(f'O nome em minusculo {nome.lower()}')

#swapcase() - inverte a string --------------------------------------------------

print(f'O nome invertido é {nome.swapcase()}')

#find() - mostra a posição de uma determinada string ----------------------------

f = 'O dia hoje está muito frio'
print(f'A posição da palavra frio {f.find('frio')}')

#replace() - altera o valor da string sem alterar a variavel principal ----------

n = 'Thereza'
print(f'O novo valor da string é {n.replace('Thereza','Joana')}')

#count() - quantidade de  vezes que uma determinada string repete --------------

z = 'Programação'
print(f'A quantidade de vezes que a string a repete é {z.count('A')}')

#split() - divide a string ------------------------------------------------------

w = 'Bom dia!'
print(w.split())

#join() - escolhe o tipo separador --------------------------------------------------

print(f'O separador {'-'.join(w)}')'''

#strip() - remove o espaço do inicio e do final da string ---------------------------

n1 = '      Bom dia!      '
print(n1)
print(n1.strip())

#lstrip() - remove o espaço da esquerda ----------------------------------------

n2 = '      Bom dia!      '
print(n2)
print(n2.lstrip())

#rstrip() - remove o espaço do direita -------------------------------------------

n3 = '      Bom dia!      '
print(n3)
print(n3.rstrip())


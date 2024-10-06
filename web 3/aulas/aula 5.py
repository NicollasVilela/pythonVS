#reverse() - inverte a lista ----------------------------
'''
a = [1,2,3,4,5,6]
a.reverse()
print(f'A lista é invertida: {a}')

#-------------------------------------------------------
b = []
for n in range(5):
    num = int(input('Digite um valor: '))
    b.append(num)
b.reverse()
print(f'A lista é invertida: {b}')

#sum() - soma todos os valores da lista ---------------

print(f'A soma dos valores = {sum(b)}')

#outra maneira de fazer a mesma coisa -----------------

vet = [0] * 5
for i in range(0,len(vet)):
    vet[i] = int(input('Digite um numero'))
print(vet)
print(f'A soma dos valores = {sum(vet)}')

#pop()- apaga o ultimo elemento da lista -----------------------

num = [10,20,30,40,50]
num.pop()
#num.pop(2)
print(f'A nova lista é {num}')

#del() - deleta elementos da lista -----------------------------

num1 = [10,20,30,40,50]
del(num1[1:4])
print(num1)

#sort() - ordena os elementos da lista ------------------------

lista = ['n','p','a','u','b']
lista1 = [2,8,45,0,23,78]
lista.sort()
print(f'A lista ordenada é {lista}')
lista1.sort()
print(f'A lista ordenada é {lista1}')

#exemplo de numeros randomicos ---------------------------------

import random

num1 = random.randint(1,10)
num2 = random.randint(10,20)
num3 = random.randint(20,30)
num4 = random.randint(30,40)
num5 = random.randint(40,50)

num_aleatorio = [num1,num2,num3,num4,num5]
print(num_aleatorio)

print(f'O menor valor da lista aleatoria é {(min(num_aleatorio))}')

print(f'O maior valor da lista aleatoria é {(max(num_aleatorio))}')

#exemplo mostrando o indice e o valor ------------------------------

lista2 = [10,20,30,40,50,60]
for i,v in enumerate(lista2):
    print(f'Indice: {i}, Valor: {v}')'''

#Dicionário  - {} ou dict() -----------------------------------------
'''
d = {}
d = dict()
print(type(d))

if not d:
    print(f'O dicionario esta vazio')
else:
    print(f'O dicionario não esta vazio')

#criando um dicionário ----------------------------------------------

pessoa = {
    'nome':'Thereza',
    'idade':30,
    'cidade':'Niterói',
    'profissao':'Professora'
}
print('Nome:',pessoa['nome'])
print('Idade:',pessoa['idade'])
print('Cidade:',pessoa['cidade'])
print('Profissão:',pessoa['profissao'])

print('Nome:',pessoa['nome'],'Idade:',pessoa['idade'])

#alterar os dados do dicionario------------------------

pessoa['idade'] = 50
pessoa['cidade'] = 'Rio de Janeiro'
print('Idade:',pessoa['idade'],'Cidade:',pessoa['cidade'])

#adicionar uma nova chave no dicionario ----------------

pessoa['email'] = 'thereza@gmail.com'

print('E_mail:',pessoa['email'])

#del() - apaga uma chave do dicionario -------------------

del(pessoa['idade'])
print('Idade:',pessoa['idade'])'''

'''pode-se fazer a busca no dicionario pela chave ou valor ou os 1 ----

Keys - mostra somente a chave
values - mostra somente os valores
items - mostra a chave e o valor

pessoa1 = {
    'nome':'Thereza',
    'idade':30,
    'cidade':'Niterói',
    'profissao':'Professora'
}
print(pessoa1.values())
print(pessoa1.keys())
print(pessoa1.items())

#---------------------------------------------------------------------

for c in pessoa1.keys():
    print(f'Chave ={c} e Valor: = {pessoa1[c]}')
    
#--------------------------------------------------------------------

notas = {}
notas = {
    'Web3':int(input('Digite a nota de web 3')),
    'Prog3':int(input('Digite a nota de prog 3')),
    'AI3':int(input('Digite a nota de AI 3'))
}

for valor in notas.values():
    print(f'Valor: {valor}')

#--------------------------------------------------------------------

aluno = {}
aluno['nome'] = input('Digite o seu nome: ')
aluno['idade'] = int(input('Digite a sua idade: '))
aluno['cidade'] = input('Digite a sua cidade: ')
aluno['profissao'] = input('Digite a sua profissão: ')

for c,v in aluno.items():
    print(f'{c}:{v}')
    
#update() ------------------------------------------------------

d = {'nome':'Julia'}
print(d)

d.update({'nome':'Julia Silva'})
print(d)

d.update({'idade':19})
d.update({'altura':1.61})
print(d)
#-------------------------------------------------------------------

d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}

d1.update(d2)
print(d1)

#copy() - fazer copia do dicionário-----------------------------------

original = {'a':1,'b':2,'c':3}
copia = original.copy()

copia['d'] = 4
print(copia)

print(original)
#Criando uma lista vazia para armazenar no dicionario ------------------

lista_pessoa = []
quantidade = int(input('Quantas pessoas deseja adicionar a lista?'))
for i in range(quantidade):
    print(f'Informações da pessoa {i + 1}')
    pessoa = {
        'nome' : input('Digite o seu nome: '),
        'idade' : int(input('Digite a sua idade: ')),
        'cidade' : input('Digite a sua cidade: '),
        'profissao' : input('Digite a sua profissão: ')
    }
    lista_pessoa.append(pessoa.copy())
print(lista_pessoa)

#---------------------------------------------------------------------------

estado = dict()
b = list()

for i in range(0,2):
    estado['uf'] = input('Entre com a unidade federativa: ')
    estado['sigla'] = input('Entre com a sigla: ')
    b.append(estado.copy())
print(b)


def mostrar_linha():
    print('-' * 50)
mostrar_linha()

#----------------------------------------------------------------------------

def mostrar_nome():
    print(f'Nome: {nome}')

#nome = input('Digite o seu nome')
#mostrar_nome()
#mostrar_linha()

quantidade_nome = int(input('Quantos nomes deseja inserir?'))

for i in range(quantidade_nome):
    nome = input(f'Digite o seu nome {i + 1}: ')
    mostrar_nome()
mostrar_linha()

#return -------------------------------------------------------------

def soma(n1,n2):
    return n1 + n2
n1 = float(input('Digite o valor de n1'))
n2 = float(input('Digite o valor de n2'))

print(soma(n1,n2))
mostrar_linha()

#---------------------------------------------------------------------

def potencia(n1):
    return n1 ** 2
print(f'O numero {n1} elevado ao quadrado é {potencia(n1)}')
mostrar_linha()

#---------------------------------------------------------------------'''

def calcular_imc(peso,altura):
    print(f'{(peso/altura ** 2) :.2f}')

p = float(input('Digite o seu peso'))
a = float(input('Digite a sua altura'))
calcular_imc(p,a)
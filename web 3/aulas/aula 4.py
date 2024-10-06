#Laço de repetição - while
'''
a = 0
while a < 8:
    print(a)
    a +=1  #a =a + 1
#--------------------------------------------------
b = 1
while b != 0:
    b = int(input('Digite um numero'))
    print('Bom dia!')

#--------------------------------------------------

n = 1
par = impar =0
while n != 0:
    n = int(input('Digite um numero'))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
    #par = par - 1
    print(f'Você digitou {par} numeros pares e {impar} numeros impares')

#break ----------------------------------------------------------------------

num = 0
while num < 5:
    num +=1
    if num == 3:
        break
    print(num)

#continue -----------------------------------------------------------------

num = 0
while num < 10:
    num +=1
    if num == 3:
        continue
    print(num)

#Tupla(),lista[] e Dicionário {}--------------------------------------------------

x = (1,2,3,4,5,6,'Maria')
print(x)
print(x[4])
print(x[-3])
print(x[1:6])
print(x[:6])
print(x[2:])

#concaternar tuplas + -----------------------------------------------------------

b = (1,2,3,4)
c = (5,6,7,8)
#d = b + c
#print(f'A tupla concatenada é {d}')
print(f'A tupla concatenada é {b + c}')

#len() - mostra o tamanho do tupla, quantidade de elementos da tupla -------------

aluno = ('Bia','Ana','Paulo','José')
#tam = len(aluno)
#print(f'A quantidade de elementos da tupla é {tam}')
print(f'A quantidade de elementos da tupla é {len(aluno)}')

#----------------------------------------------------------------------------------

for a in range(0,len(aluno)):
    print(f'Oi!{aluno[a]}')
    print(f'Bom dia!')

#del() - para deletar ----------------------------------------------------------

del(aluno)
print(aluno)

#count() - mostra a quantidade de vezes que um determinado elemento repete

f = (1,3,3,5,8,9,3)
print(f'O numero 3 repete {f.count(3)} vezes')

#index() - mostra a primeira posição da repetição do elemento --------

print(f'O indice da primeira repetição do numero 3 é a posição {f.index(3)} ')'''

#Lista [] -------------------------------------------------------------
'''
x = [1,2,3,4,5,6,'Maria']

print(x)
print(x[4])
print(x[-3])
print(x[1:6])
print(x[:6])
print(x[2:])
x[-1] = 'Bia'
print(x)

#-------------------------------------------------------------------------
y = [1,['Paulo',2,5],7,9,8,[1,2,3],10,25]
print(y)
print(y[5][0])
#------------------------------------------------------------------------
b = [1,2,3,4]
c = [5,6,7,8]
#d = b + c
#print(f'A lista concatenada é {d}')
print(f'A lista concatenada é {b + c}')
#append() - adiciona no final da lista ------------------------------------

w = [10,20,30,40]
j = w.append('Python')
print(w)

#-------------------------------------------------------------------------

numeros = []
n1 = int(input('Digite um numero'))
n2 = int(input('Digite um numero'))
n3 = int(input('Digite um numero'))
n4 = int(input('Digite um numero'))
numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
numeros.append(n4)
print(numeros)

#--------------------------------------------------------------------------
numero = []
for i in range(3,15,2):
    numero.append(i)
    print(i)
    
#insert() - adiciona elementos na posição desejada -------------------------

m = [14,58,96,78]
m.insert(2,'Bia')
print(m)

#remove()- remove um elemento da lista -----------------------------------------

m.remove(58)
print(m)

#min() - busca o menor valor da lista ------------------------------------------

i = [1,2,5,89,0,87,36,95]
print(f'O menor valor da lista é {min(i)}')

#max() - busca o maior valor da lista -----------------------------------------

print(f'O maior valor da lista é {max(i)}')

#-----------------------------------------------------------------------------
prova = [0,0,0]
prova[0] = float(input('Digite a nota da AV1'))
prova[1] = float(input('Digite a nota da AV1'))
prova[2] = float(input('Digite a nota da AV1'))
media = ((prova[0]+prova[1]+prova[2])/3)
print(prova)
print(f'A média do aluno é {media:.2f}')'''
#----------------------------------------------------------------------------
prova = [0]*3
for a in range(0,len(prova)):
    prova[a] = float(input('Digite a nota da prova'))
    media = ((prova[0] + prova[1] + prova[2]) / 3)
    #print(prova)
print(f'A média do aluno é {media:.2f}')



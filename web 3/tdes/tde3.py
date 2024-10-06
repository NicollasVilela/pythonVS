'''1. Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado(entre 0 e 20) e mostrá-la por extenso.


numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 
                   'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 
                   'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Número inválido. Tente novamente.')

print(f'Você digitou o número {numExtenso[numero]}.')'''

'''2. Faça um programa que preencha por leitura uma lista de 10 posições, e conta
quantos valores diferentes existem na lista.


lista = []

for i in range(10):
    valor = int(input(f'Digite o valor para a posição {i + 1}: '))
    lista.append(valor)

dif = set(lista)

print(f'A lista contém {len(dif)} valores diferentes.')'''

'''3.Crie um programa que leia quatro valores pelo teclado e guarde-os em uma lista.
No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares.


valores = []
for i in range(4):
    valor = int(input(f'Digite o valor {i + 1}: '))
    valores.append(valor)

numNoves = valores.count(9)

if 3 in valores:
    posTres = valores.index(3) + 1
else:
    posTres = None

numPares = [num for num in valores if num % 2 == 0]

print(f'O valor 9 apareceu {numNoves} vezes.')
if posTres:
    print(f'O primeiro valor 3 foi digitado na posição {posTres}.')
else:
    print('O valor 3 não foi digitado.')

print(f'Os números pares digitados foram: {numPares}')'''

'''4. Um dado é lançado 50 vezes, e o valor correspondente é armazenado em uma
lista. Faça um programa que determine o percentual de ocorrências de face 6 do
dado dentre esses 50 lançamentos.


import random

lancamentos = [random.randint(1, 6) for _ in range(50)]

qtdSeis= lancamentos.count(6)

percentSeis = (qtdSeis / 50) * 100

print(f'O dado foi lançado 50 vezes.')
print(f'A face 6 apareceu {qtdSeis} vezes.')
print(f'O percentual de ocorrências da face 6 foi de {percentSeis:.2f}%.')'''

'''5. Tradutor Simples:
Desenvolva um programa que atue como um tradutor simples entre duas línguas. O
programa deve usar um dicionário onde as chaves são palavras em uma língua e os
valores são suas traduções em outra língua. O usuário deve poder fornecer uma
palavra como entrada e obter sua tradução como saída.


dicionario = {
    'gato': 'cat',
    'maçã': 'apple',
    'computador': 'computer',
    'sol': 'sun',
}

palavra = input('Digite uma palavra em português para traduzir para o inglês: ').lower()

if palavra in dicionario:
    print(f'A tradução de "{palavra}" para o inglês é: {dicionario[palavra]}')
else:
    print('Tradução não encontrada.')'''

'''6. Estoque de Produtos:
Implemente um sistema simples de controle de estoque de produtos. O programa
deve permitir ao usuário adicionar novos produtos ao estoque, atualizar a
quantidade de produtos existentes e exibir o estoque atualizado. Use um dicionário
onde as chaves são os nomes dos produtos e os valores são as quantidades
disponíveis.


estoque = {}

def addProd(produto, quantidade):
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade
    print(f'Produto "{produto}" adicionado/atualizado com sucesso.')

def atualizarQtd(produto, quantidade):
    if produto in estoque:
        estoque[produto] = quantidade
        print(f'A quantidade do produto "{produto}" foi atualizada para {quantidade}.')
    else:
        print(f'O produto "{produto}" não existe no estoque.')

def exibirEstoque():
    if estoque:
        print("\nEstoque Atual:")
        for produto, quantidade in estoque.items():
            print(f'Produto: {produto}, Quantidade: {quantidade}')
    else:
        print('O estoque está vazio.')

while True:
    print("\n1. Adicionar produto")
    print("2. Atualizar quantidade")
    print("3. Exibir estoque")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        produto = input("Digite o nome do produto: ").lower()
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        addProd(produto, quantidade)

    elif opcao == '2':
        produto = input("Digite o nome do produto que deseja atualizar: ").lower()
        quantidade = int(input(f"Digite a nova quantidade de {produto}: "))
        atualizarQtd(produto, quantidade)

    elif opcao == '3':
        exibirEstoque()

    elif opcao == '4':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")'''

'''7. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
ordem lida.


idades = []
alturas = []

for i in range(5):
    idade = int(input(f'Digite a idade da pessoa {i + 1}: '))
    altura = float(input(f'Digite a altura da pessoa {i + 1} (em metros): '))
    idades.append(idade)
    alturas.append(altura)

print("\nIdades e alturas na ordem inversa:")

for i in range(4, -1, -1):
    print(f'Pessoa {i + 1}: Idade = {idades[i]}, Altura = {alturas[i]:.2f} metros')'''

'''8. Frequência de Letras:
Crie um programa que receba uma string como entrada e conte o número de
ocorrências de cada letra do alfabeto (ignorando maiúsculas/minúsculas). O
programa deve imprimir um dicionário onde as chaves são as letras do alfabeto e os
valores são o número de vezes que cada letra ocorre na string.


def contaLetra(string):
    frequencia = {}

    for letra in string.lower():
        if letra.isalpha():
            if letra in frequencia:
                frequencia[letra] += 1
            else:
                frequencia[letra] = 1

    return frequencia

texto = input("Digite uma string: ")

resultado = contaLetra(texto)

print("\nFrequência de cada letra:")
for letra, freq in sorted(resultado.items()):
    print(f'{letra}: {freq}')'''

'''9. Média de Notas:
Escreva uma função em Python que receba um dicionário contendo nomes de
alunos e suas respectivas notas em uma disciplina. A função deve calcular a média
das notas de todos os alunos e retornar um dicionário onde a chave é "média" e o
valor é a média calculada.


def calcMedia(alunosNotas):
    totalNotas = sum(alunosNotas.values())

    totalAlunos = len(alunosNotas)

    media = totalNotas / totalAlunos

    return {"média": media}

alunosNotas = {
    'Alice': 8.5,
    'Bruno': 7.0,
    'Carlos': 9.2,
    'Diana': 6.8,
    'Eva': 8.0
}

resultado = calcMedia(alunosNotas)

print(resultado)'''

'''10. Contagem de Palavras:
Escreva um programa em Python que receba uma string como entrada e conte o
número de ocorrências de cada palavra na string. O programa deve imprimir um
dicionário onde as chaves são as palavras e os valores são o número de vezes que
cada palavra ocorre na string.'''

'''11. Escreva uma função que recebe um número n como parâmetro e imprime se n é
positivo ou negativo.


def check(n):
    if n > 0:
        print(f'O número {n} é positivo.')
    elif n < 0:
        print(f'O número {n} é negativo.')
    else:
        print(f'O número {n} é zero.')

numero = float(input("Digite um número: "))
check(numero)'''

'''12. Escreva uma função para imprimir o valor absoluto de um número.


def printValAb(n):
    valorA = abs(n)
    print(f'O valor absoluto de {n} é {valorA}.')

numero = float(input("Digite um número: "))
printValAb(numero)'''

'''13. Escreva uma função que recebe dois números (a e b) como parâmetro e retorne
True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.


def somaMaior(a, b, limite):
    return (a + b) > limite

numero1 = float(input("Digite o primeiro número (a): "))
numero2 = float(input("Digite o segundo número (b): "))
limite = float(input("Digite o limite: "))

resultado = somaMaior(numero1, numero2, limite)

print(f'A soma de {numero1} e {numero2} é maior que {limite}? {resultado}')'''

'''14. Faça um programa com uma função chamada somaImposto. A função possui
dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto. A
função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(taxa, custo):
    valor = (taxa / 100) * custo
    custoFinal = custo + valor
    return custoFinal

taxa = float(input("Digite a taxa de imposto sobre vendas (em %): "))
custo = float(input("Digite o custo do item antes do imposto: "))

custoFinal = somaImposto(taxa, custo)

print(f'O custo final do item, incluindo um imposto de {taxa}%, é {custoFinal:.2f}.')'''

'''15. Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.'''


def contDigitos(numero):
    numero = abs(numero)

    qtdDigitos = len(str(numero))

    return qtdDigitos


numero = int(input("Digite um número inteiro: "))

quantidade = contDigitos(numero)

print(f'O número {numero} tem {quantidade} dígitos.')
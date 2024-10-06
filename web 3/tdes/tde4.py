#1-
# try:
# a = int(input('Valor a ser dividido: '))
# b = int(input('Divisor: '))
# r = a/b
# print(r)
# except ZeroDivisionError:
# print('Impossivel dividir por 0.')
# finally:
# print('Fim!')
#2-
# def valor_negativo_error(valor):
# if valor < 0:
# raise ValueError(f"O valor fornecido é negativo: {valor}")
# def verificar_valor(numero):
# valor_negativo_error(numero)
# return "O valor é positivo."
# def obter_valor_externo():
# try:
# valor = float(input("Digite um número: "))
# resultado = verificar_valor(valor)
# print(resultado)
# except ValueError as e:
# print(f"Exceção capturada: {e}")
# obter_valor_externo()
#3-
# def transInt(a):
# try:
# num = int(a)
# print(f'O número convertido é: {num}')
# except ValueError:
# print('Erro. Digite outra coisa')
# except TypeError:
# print('O valor fornecido não é uma string.')
# except:

# print(f'Erro.')
# str = input('Digite a string que vai virar int: ')
# transInt(str)
#4-

#5-
# def eggxecute():
# try:
# res = 0 / 0
# print(f'O resultado é: {res}')
# except:
# print(f'Ocorreu um erro.')
# eggxecute()
#6-
# def launch():
# raise ValueError('Erro.')
# def passa():
# try:
# launch()
# except:
# raise
# try:
# passa()
# except:
# print(f'Erro!!!!!!!!!!!!!')
#7-

#8-Crie uma função que divide dois números. A função deve tratar o caso de
# divisor zero e retornar um valor None quando uma exceção ocorre.

# def div(a, b):
# try:
# r = a / b
# return r
# except ZeroDivisionError:
# print('Erro: Não dá pra dividir por zero.')
# return None
# except ValueError:
# print('Erro')
# return None
# try:
# a = int(input('Digite um numerador: '))
# b = int(input('Digite um denominador: '))
# r = div(a, b)
# if r is not None:
# print(f'O resultado da divisão é: {r}')
# except ValueError:
# print('Erro')
#9-

#10-
# def dividir(lista):
# for num in lista:
# try:
# r = 100 / num
# print(f'100 dividido por {num} é {r}')
# except ZeroDivisionError:
# print(f'Não é possível dividir por zero. ')
# except Exception as e:
# print(f'Erro')
# num = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# dividir(num)
#11-

# def checkPos(n):
# if n < 0:
# raise ValueError('Número negativo não pode')
# print(f'o número {n} é positivo')

# try:
# n = int(input('Digite um número: '))
# checkPos(n)
# except ValueError as e:
# print(f'Erro: {e}')
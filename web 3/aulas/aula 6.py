'''Exception
try:
except:
else:
finally:
https://docs.python.org/3/library/exceptions.html

try:
    numero = int(input('Digite um numero'))
    print(numero)
except:
    print('Digite um valor válido')

#---------------------------------------------
try:
    print(x)
except:
    print('Erro')
#---------------------------------------------
try:
    print(x)
except NameError:
    print('X não definido')
#-------------------------------------------
try:
    a = int(input('Digite um numerador'))
    b = int(input('Digite um denominador'))
    r = a/b
except:
    print('Tivemos um problema no programa')
else:
    print(f'O resultado foi {r}')
#------------------------------------------

try:
    x = int(input('Digite um numero'))
    print(x)
except:
    print('Erro no programa')
else:
    print('Deu tudo certo!')
finally:
    ('Fim do programa')

try:
    numero = int(input('Digite um numerador'))
    numero1 = int(input('Digite um denominador'))
    r = numero / numero1
    print(numero)
except ZeroDivisionError:
    print('Divisão por zero não é possivel')
except ValueError:
    print('Digite um numero válido')
except:
    print('Erro inesperado')
finally:
    print('Termino')
#--------------------------------------
try:
    numero = int(input('Digite um numerador'))
    numero1 = int(input('Digite um denominador'))
    r = numero / numero1
except(ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados')
except ZeroDivisionError:
    print('Divisão por zero não é possivel')
except KeyboardInterrupt:
    print('O usuário preferiu não resposnder')
else:
    print(f'O resultado foi {r}')
finally:
    print('Obrigada por usar o nosso programa')

#--------------------------------------
def leiaInt(msg):
    while True:
        try:
            m = int(input(msg))
        except:
            print('Erro digite um numero')
            continue
        else: return m

m = leiaInt('Digite um valor')
print(f'O valor digitado foi {m}')

#--------------------------------------
def calcular_media(lista):
    try:
        total = sum(lista)
        media = total/len(lista)
    except ZeroDivisionError:
        print('Erro:a lista está vazia.NJão é possivel calcular a media')
    except TypeError:
        print('Erro:a lista contem tipo de dados incompativeis')
    else:
        print(f'A media foi calculada com sucesso')
        return  media
    finally:
        print('Fim do programa')

valores = []
while True:
    valor = input("Digite um valor(ou 'fim' para terminar a lista)")
    if valor.lower() == 'fim':
        break
    try:
        valores.append(float(valor))
    except ValueError:
        print('Valor inválido.Por favor digite um numero')
media = calcular_media(valores)
if media is not None:
    print(f'A media dos valores é: {media}')
#--------------------------------------
def calcular_media(notas):
    try:
        total = sum(notas)
        media = total/len(notas)
        if media >= 6:
            return 'Aprovado'
        else:
            return 'Reprovado'
    except ZeroDivisionError:
        print('Erro:a lista está vazia.NJão é possivel calcular a media')
    except TypeError:
        print('Erro:a lista contem tipo de dados incompativeis')
notas = []
while True:
    nota_str = input("Digite um valor(ou 'fim' para terminar a lista)")
    if nota_str.lower() == 'fim':
        break
    try:
        nota=float(nota_str)
        if nota < 0 or nota >10:
            raise ValueError('A nota deve ser entre 0 e 10')
        notas.append(nota)
    except ValueError:
        print('Valor inválido.Por favor digite um numero')
resultado = calcular_media(notas)
print(f'Resultado: {resultado}')

#-------------------------------------------------------------
def calcular_imc(peso,altura):
    try:
        imc = peso /altura ** 2
        if imc < 18.5:
            return 'Abaixo do peso'
        elif imc >= 18.5 and imc < 25:
            return 'Peso normal'
        elif imc >= 25 and imc < 30:
            return 'Sobrepeso'
        else:
            return 'Obeso'
    except ZeroDivisionError:
        return 'Erro:Altura não pode ser zero'
    except TypeError:
        return 'Erro:Os valores fornecidos devem ser numeros'
try:
    peso = float(input('Digite o seu peso'))
    altura = float(input('Digite a sua altura'))
    if peso <= 0 or altura >10<= 0:
            raise ValueError('Peso e altura devem ser maiores que zero')
except ValueError:
    print('Erro')
else:
        resultado = calcular_imc(peso,altura)
        print(f'Resultado: {resultado}')
# -------------------------------------------------------------------'''

def valor_negativo_error(valor):
    """Levanta uma exceção com uma mensagem personalizada para valores negativos."""
    if valor < 0:
        raise ValueError(f"O valor fornecido é negativo: {valor}")

def verificar_valor(numero):
    """Verifica se o número é negativo e levanta uma exceção se for o caso."""
    valor_negativo_error(numero)
    return "O valor é positivo."

def obter_valor_externo():
    """Obtém um valor externo, por exemplo, do usuário, e verifica se é negativo."""
    try:
        valor = float(input("Digite um número: "))  # Obtém um número do usuário
        resultado = verificar_valor(valor)
        print(resultado)
    except ValueError as e:
        print(f"Exceção capturada: {e}")

# Chamada da função para obter e verificar o valor externo
obter_valor_externo()


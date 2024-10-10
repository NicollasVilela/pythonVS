from tkinter import *
from tkinter import messagebox

'''1. Escreva uma função verificar_numero que recebe um número inserido pelo
usuário como parâmetro e imprime em uma caixa de mensagem do Tkinter
se o número é positivo ou negativo.

def verificar_numero(num):
    if num > 0:
        mensagem = "O número é positivo!"
    else:
        mensagem = "O número é negativo!"
    messagebox.showinfo("Resultado: ", mensagem)
    
def obter_num():
    try:
        num = float(entry.get())
        verificar_numero(num)
    except ValueError:
        messagebox.showerror("Erro. Insira um valor válido.")

t = Tk()
t.geometry('400x300')
t.title('1- ')

entry = Entry(t)
entry.pack(pady = 10)

botao = Button(t, text = 'Verificar', command = obter_num)
botao.pack(pady = 10)

t.mainloop()'''

'''2. Criar uma interface Tkinter que permita ao usuário inserir uma lista ordenada
de números e um limite desejado. Em seguida, ao pressionar um botão, a
função verificará se há algum elemento na lista maior que o limite desejado e
retornará o índice do primeiro elemento que atenda a essa condição, ou
retornará -1 se nenhum elemento for maior que o limite desejado.

def check_len():
    try:
        lista = list(map(float, entry.get().split(', ')))
        limite = float(entry_max.get())
        
        for idx, num in enumerate(lista):
            if num > limite:
                messagebox.showinfo("Resultado", f"O primeiro elemento maior que {limite} está no index {idx}")
                return
        
        messagebox.showinfo("Resultado", "Nenhum elemento ultrapassa o limite!")
    
    except ValueError:
        messagebox.showerror("Erro", "Insira elementos válidos na lista e no limite")
        
t = Tk()
t.geometry('400x300')
t.title('2- ')

lista = []

text = Label(t, text = "Insira os valores separados por vírgula")
text.pack(pady = 2)

entry = Entry(t, width = 30)
entry.pack(pady = 10)

textLIM = Label(t, text = "Insira o limite")
textLIM.pack(pady = 2)

entry_max = Entry(t, width = 30)
entry_max.pack(pady = 10)

botao = Button(t, text = 'Checar', command = check_len)
botao.pack(pady = 10)

t.mainloop()'''

'''3. Criar uma interface Tkinter que permita ao usuário inserir um ano e, ao
pressionar um botão, a função verificará se o ano é bissexto ou não. Em
seguida, exibirá uma mensagem indicando o resultado.

def check_bis():
    ano = int(entry.get())
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        messagebox.showinfo("Resultado", f"{ano} é um ano bissexto!")
    else:
        messagebox.showinfo("Resultado", f"{ano} não é um ano bissexto!") 

t = Tk()
t.geometry('400x300')
t.title('3- ')

text = Label(t, text = 'Insira um ano')
text.pack(pady = 5)

entry = Entry(t, width = 5)
entry.pack(pady = 5)

btn_check = Button(t, text = "CHECK", command = check_bis)
btn_check.pack(pady = 5)

t.mainloop()'''

'''4. Criar uma calculadora básica em Tkinter que permita ao usuário inserir dois
números e, ao pressionar um botão, exibirá o resultado da
adição,subtração,multiplicação e divisão desses dois números.

def calc(op):
    try:
        a = float(num1.get())
        b = float(num2.get())
        if op == '+':
            res.set(a + b)
        elif op == '-':
            res.set(a - b)
        elif op == '*':
            res.set(a * b)
        elif op == '/':
            if b != 0:
                res.set(a / b)
            else:
                res.set("Não pode dividir por 0.")
        else:
            res.set("Operação inválida.")
    except ValueError:
        res.set("Digite um número")

t = Tk()
t.geometry('400x300')
t.title('4- ')

res = StringVar()

num1 = Entry(t)
num1.pack(pady = 5)

num2 = Entry(t)
num2.pack(pady = 5)

Button(t, text = '+', command = lambda: calc('+')).pack(pady = 5)
Button(t, text = '-', command = lambda: calc('-')).pack(pady = 5)
Button(t, text = '*', command = lambda: calc('*')).pack(pady = 5)
Button(t, text = '/', command = lambda: calc('/')).pack(pady = 5)

Label(t, text = "Resultado: ").pack(pady = 5)
Label(t, textvariable = res).pack(pady = 5)

t.mainloop()'''

'''5. Criar uma interface Tkinter que permita ler quatro valores pelo teclado e
guarde-os em uma lista.
No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares. enunciado para tkinter

def process():
    try:
        for i in range(4):
            valor = float(entries[i].get())
            lista.append(valor)
        
        count_nine = lista.count(9)
        
        pos_three = lista.index(3) if 3 in lista else -1
        
        numeros_pares = [num for num in lista if num % 2 == 0]

        resultado = f"Quantidade de 9: {count_nine}\n"
        resultado += f"Posição do primeiro 3: {pos_three}\n"
        resultado += f"Números pares: {numeros_pares}"
        
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

t = Tk()
t.geometry('400x300')
t.title('Leitor de Valores')

lista = []
entries = []

for i in range(4):
    label = Label(t, text=f'Insira o {i + 1}º valor:')
    label.pack(pady=5)
    entry = Entry(t, width=10)
    entry.pack(pady=5)
    entries.append(entry)

btn_process = Button(t, text='Processar', command=process)
btn_process.pack(pady=10)

t.mainloop()'''

#PARTE 2 ==========================

'''
1- C
2- C
3- A
4- A
5- checkbutton
6- C
7- B
8- A
Desenvolva um aplicativo de preço final utilizando Tkinter. A interface
gráfica deve conter um campo de entrada para o valor do produto e outro para a forma de
pagamento. O usuário deve inserir o valor do produto e selecionar a forma de pagamento através de
um campo de entrada. Se a forma de pagamento for à vista (representada pelo número 1), um
desconto de 10% deve ser aplicado sobre o valor do produto antes de exibir o preço final. Caso
contrário, se a forma de pagamento for à prazo (representada pelo número 2), o preço final deve ser
igual ao valor do produto. Ao clicar em um botão "Calcular", o aplicativo deve exibir o preço final em
uma mensagem na tela.
'''

def exibir():
    total = int(val.get())
    selec = pag.get()
    totalAV = total * 0.9
    if selec == '1':
        messagebox.showinfo(f"Total a ser pago", f"Total a ser pago: {totalAV:.2f}")
    elif selec == '2':
        messagebox.showinfo(f"Total a ser pago", f"Total a ser pago: {total:.2f}")
    else:
        messagebox.showerror("ERRO", "OPÇÃO INVÁLIDA")
            
t = Tk()
t.geometry('400x300')
t.title('Leitor de Valores')

sug1 = Label(t, text = "Digite o valor da compra").pack()
val = Entry(t)
val.pack(pady = 5)

sug = Label(t, text = "Digite '1' para pagar a vista(10% OFF) e '2' para pagar a prazo").pack()
pag = Entry(t)
pag.pack(pady = 5)

show = Button(t, text = 'CALCULAR', command = exibir).pack(pady = 5)

t.mainloop()

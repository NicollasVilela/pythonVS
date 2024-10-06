from tkinter import *

'''1. Criação de uma Janela Básica Crie um programa que abra uma janela básica com o título
"Minha Primeira Janela". A janela deve ter as dimensões 300x200 pixels e um botão que, ao
ser clicado, fecha a janela.

t = Tk()

def clicou_fechou():
t.destroy()

t.title('Exemplo de tkinter')
b = Button(t, text = 'Clique aqui para fechar a janela!', command = clicou_fechou)
b.place(x = 10, y = 40)

t.mainloop()'''

'''2. Crie uma interface gráfca que contenha um Label com o texto "Digite seu nome" e um
campo de entrada (Entry). Quando o usuário digitar o nome e pressionar um botão
"Mostrar", o nome deve ser exibido em um novo Label abaixo.

def clica_mostra():
nome = e.get()
r.confg(text = f'Nome digitado: {nome}')

t = Tk()
t.title('2- ')
t.geometry('300x300')

l = Label(t, text = 'Nome: ')
l.pack()

e = Entry(t)
e.pack()

b = Button(t, text = 'Mostrar', command = clica_mostra)
b.pack()

r = Label(t, text = '')
r.pack()

t.mainloop()'''

'''3. Crie um programa com três opções de seleção (RadioButton): "Opção A", "Opção B", e
"Opção C". Quando o usuário selecionar uma das opções e clicar em "Confrmar", a escolha
deve ser exibida em um Label.

def clica_mostra():
selec = x.get()
if selec == 1:

r.confg(text = 'Você selecionou a opção 1')
elif selec == 2:
r.confg(text = 'Você selecionou a opção 2')
elif selec == 3:
r.confg(text = 'Você selecionou a opção 3')
else:
r.confg(text = 'Nenhuma opção selecionada')

t = Tk()
t.title('3-')
t.geometry('300x300')

x = IntVar()

op1 = Radiobutton(t, text = 'Opção 1', variable = x, value = 1)
op1.pack()

op2 = Radiobutton(t, text = 'Opção 2', variable = x, value = 2)
op2.pack()

op3 = Radiobutton(t, text = 'Opção 3', variable = x, value = 3)
op3.pack()

b = Button(t, text = 'Confrmar', command = clica_mostra)
b.pack()

r = Label(t, text = '')
r.pack()

t.mainloop()'''

'''4. Implemente uma interface com três caixas de seleção (CheckButton): "Python", "Java" e
"C++". O usuário pode selecionar mais de uma linguagem. Após clicar no botão "Confrmar",
exiba as linguagens selecionadas em um Label.

def clica_mostra():
selec = []
if py.get() == 1:
selec.append('Python')
if java.get() == 1:
selec.append('Java')
if c.get() == 1:
selec.append('C++')
if selec:
r.confg(text = 'Você selecionou: ' + ', '.join(selec))
else:
r.confg(text = 'Nenhuma opção selecionada')

t = Tk()
t.title('4-')
t.geometry('300x300')

py = IntVar()

java = IntVar()
c = IntVar()

op = Checkbutton(t, text = 'Python', variable = py)
op.pack()

op1 = Checkbutton(t, text = 'Java', variable = java)
op1.pack()

op2 = Checkbutton(t, text = 'C++', variable = c)
op2.pack()

b = Button(t, text = 'Confrmar', command = clica_mostra)
b.pack()

r = Label(t, text = '')
r.pack()

t.mainloop()'''

'''5. Crie um programa que permita alterar a cor de fundo da janela. Adicione botões para três
cores diferentes (por exemplo, vermelho, verde e azul). Quando o usuário clicar em um
botão, a cor de fundo da janela deve mudar para a cor correspondente.

def clicou_mudou():

selec = vm.get()
if selec == 1:
r.confg(text='Você selecionou: Vermelho')
t['bg'] = '#FF0000'
elif selec == 2:
r.confg(text='Você selecionou: Verde')
t['bg'] = '#00FF00'
elif selec == 3:
r.confg(text='Você selecionou: Azul')
t['bg'] = '#0000ff'

t = Tk()
t.title('5-')
t.geometry('300x300')

vm = IntVar()

c = Radiobutton(t, text='Vermelho', variable=vm, value=1, command=clicou_mudou)
c.pack()

c1 = Radiobutton(t, text='Verde', variable=vm, value=2, command=clicou_mudou)
c1.pack()

c2 = Radiobutton(t, text='Azul', variable=vm, value=3, command=clicou_mudou)
c2.pack()

r = Label(t, text='')

r.pack()

t.mainloop()'''

'''6. Implemente uma interface que permita aumentar ou diminuir o tamanho da janela através
de dois botões: "Aumentar" e "Diminuir". Ao clicar nesses botões, a janela deve crescer ou
encolher 50 pixels em cada direção.

def clicou_mudou():
selec = x.get()
if selec == 1:
largura, altura = t.winfo_width(), t.winfo_height()
t.geometry(f"{largura + 50}x{altura + 50}")
elif selec == 2:
largura, altura = t.winfo_width(), t.winfo_height()
if largura > 100 and altura > 100:
t.geometry(f"{largura - 50}x{altura - 50}")

t = Tk()
t.title('6-')
t.geometry('300x300')

x = IntVar()

aum = Button(t, text='Aumentar', command = lambda: (x.set(1), clicou_mudou()))
aum.pack()

dim = Button(t, text='Diminuir', command = lambda: (x.set(2), clicou_mudou()))
dim.pack()

t.mainloop()'''

'''7. Crie uma calculadora simples com dois campos de entrada e botões para as quatro
operações básicas (adição, subtração, multiplicação, divisão). Quando o usuário inserir dois
números e clicar em uma operação, o resultado deve ser mostrado em um Label.

def calc(op):
try:
a = foat(num1.get())
b = foat(num2.get())
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
res.set('Não pode dividir por 0')
else:
res.set('Operação inválida')
except ValueError:
res.set('Erro. Entrada inválida')

t = Tk()
t.title('7-')
t.geometry('300x300')

res = StringVar()

num1 = Entry(t)
num1.pack(pady = 5)

num2 = Entry(t)
num2.pack(pady = 5)

Button(t, text = '+', command = lambda: calc("+")).pack(pady = 5)
Button(t, text = '-', command = lambda: calc("-")).pack(pady = 5)
Button(t, text = '*', command = lambda: calc("*")).pack(pady = 5)
Button(t, text = '/', command = lambda: calc("/")).pack(pady = 5)

Label(t, text = 'Resultado: ').pack(pady = 5)
Label(t, textvariable = res).pack(pady = 5)

t.mainloop()'''

'''8. Crie um programa que contenha uma lista de 10 itens em um Listbox. Adicione uma barra
de rolagem (Scrollbar) para que o usuário possa navegar pela lista. Permita que o usuário

selecione um item e exiba o item selecionado em um Label.

def mostra():
try:
item_selec = Lista.get(Lista.curselection())
res.set(f"Item selecionado: {item_selec}")
except:
res.set("Nenhum item selecionado")

t = Tk()
t.title('8-')
t.geometry('300x300')

scrollbar = Scrollbar(t)
scrollbar.pack(side="right", fll="y")

Lista = Listbox(t, yscrollcommand=scrollbar.set, selectmode=SINGLE)
Lista.pack(pady=15)

itens = ['Pão', 'Açúcar', 'Sal', 'Maionese', 'Carne', 'Queijo', 'Presunto', 'Refrigerante', 'Macarrão', 'Biscoito']
for i in itens:
Lista.insert(END, i)

scrollbar.confg(command=Lista.yview)

res = StringVar()

Label(t, textvariable=res).pack(pady=10)

Button(t, text="Exibir Seleção", command=mostra).pack(pady=10)

t.mainloop()'''
'''from tkinter import *

i = Tk()      #criar a janela

i.title('Primeiro Tkinter')  #titulo da janela

i.wm_iconbitmap('favicon.ico')  #inserir icone na janela

i.geometry('600x400') #tamanho da janela

i['bg'] = '#B0E0E6' #escolher a cor de fundo da janela

#i.resizable(0,0) bloqueia a janela, pode usar (True ou False)

#i.state('zoomed') abre a janela na tela cheia , no zoom,maximizada

#i.state('iconic') abre a janela minimizada

i.minsize(300,200) #define o menor tamanho da janela

i.maxsize(700,500) #define o maior tamanho da janela

#Entry() - criar uma caixa de entrada vazia -----------------------

e = Entry(i).pack()
#e.pack()

#Button() - inserir botão na janela -----------------------------

b = Button(i,text='Cadastrar',font='Gabriola 10').pack()
#b.pack()

#Label() - inserir um rotulo na janela -------------------------

l = Label(i,
          text = 'Nome:',
          bg = 'Khaki',
          fg = '#4B0082',
          font = 'Verdana 10 italic',
          relief = 'raised',
          bd = 10,
          padx = 30,
          pady = 30
          ).pack()
#l.pack()

#sistema grid (linhas e colunas) --------------------------------------------

l1 = Label(i,text='Projeto 1',font='Arial 20',bg='blue')
l2 = Label(i,text='Projeto 2',font='Arial 20',bg='yellow')
l3 = Label(i,text='Projeto 3',font='Arial 20',bg='pink')


l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=0,column=2)

l1.grid(row=0,column=0)
l2.grid(row=1,column=1)
l3.grid(row=2,column=2)

btn1 = Button(i,text='Clique aqui1')
btn2 = Button(i,text='Clique aqui2')
btn3 = Button(i,text='Clique aqui3')

btn1.grid(row=1,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=3,column=2)

l = Label(i,text='Nome: ',bg='#B0E0E6' )
e = Entry(i)
l1 = Label(i,text='Endereço: ',bg='#B0E0E6' )
e1= Entry(i)
l2 = Label(i,text='Email: ',bg='#B0E0E6' )
e2 = Entry(i)
btn = Button(i,text='Incluir')

l.grid(row=0,column=0)
e.grid(row=0, column=1)

l1.grid(row=1,column=0)
e1.grid(row=1, column=1)

l2.grid(row=2,column=0)
e2.grid(row=2, column=1)
btn.grid(row=3,column=0)

#checkbutton() - seleção multipla --------------------------------------

t = Label(i,text='Escolha o seu esporte favorito',bg='#B0E0E6')
c1 = Checkbutton(i,text='Basquete',bg='#B0E0E6')
c2 = Checkbutton(i,text='Futebol',bg='#B0E0E6')
c3 = Checkbutton(i,text='Volei',bg='#B0E0E6')
c4 = Checkbutton(i,text='Tenis',bg='#B0E0E6')
c5 = Checkbutton(i,text='Nataçao',bg='#B0E0E6')

t.grid(row=0,column=0)
c1.grid(row=1,column=0)
c2.grid(row=1,column=1)
c3.grid(row=1,column=2)
c4.grid(row=1,column=3)
c5.grid(row=1,column=4)

#Radiobutton() - seleção simples ---------------------------------

valor = IntVar()

r1 = Radiobutton(i,text='Opção1',bg='#B0E0E6',variable='valor',value=1).pack()
r2 = Radiobutton(i,text='Opção2',bg='#B0E0E6',variable='valor',value=2).pack()
r3 = Radiobutton(i,text='Opção3',bg='#B0E0E6',variable='valor',value=3).pack()

#Listbox() - criar uma lista(posição,valor) ----------------------

lista = Listbox(i)
lista.pack()

lista.insert(0,'AC')
lista.insert(1,'AM')
lista.insert(2,'MG')
lista.insert(3,'RJ')
lista.insert(4,'SP')
lista.insert(END,'RO')
lista.insert(END,'RN')
lista.insert(END,'RS')

estado = ['BA','AM','ES']
for e in estado:
    lista.insert(END,e)

#Scale() - barra de escala(from_,to)---------------------

s = Scale(i,from_=0,to=10).pack() #padrão vertical

s1 = Scale(i,from_=0,to=10,orient=HORIZONTAL).pack()

s2 = Scale(i,from_=0,to=10,orient=HORIZONTAL,resolution=0.5).pack()

#place(x,y) ---------------------------------------------------------

l1 = Label(i,text='Projeto 1',font='Arial 20',bg='blue')
l2 = Label(i,text='Projeto 2',font='Arial 20',bg='yellow')
l3 = Label(i,text='Projeto 3',font='Arial 20',bg='pink')

l1.place(x=10,y=10)
l2.place(x=130,y=60)
l3.place(x=250,y=110)
i.mainloop()'''
#-----------------------------------------------------------------
import tkinter as tk

j = tk.Tk() #instancia da janela principal

def botao_clicado():
    l.config(text='Botão clicado!')

j.title('Exemplo de Tkinter')
l = tk.Label(j,text='Olá Mundo!')
l.place(x=1,y=10)
b = tk.Button(j,text='clique aqui!',command=botao_clicado)
b.place(x=10,y=40)

j.mainloop()
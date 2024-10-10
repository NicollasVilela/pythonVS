from tkinter import *       #import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

'''
root = Tk()
root.geometry('400x300')
root.title('Aplicação Tkinter')

def clique_botao():
    messagebox.showinfo('Informação', "Você clicou no botão!")

btn = Button(root, text='Clique Aqui', command=clique_botao)
btn.pack(pady=10)

#---------------------------------------------------------------



label_lista = Label(root,text='Escolha uma opção: ')
label_lista.pack()

lista_opcoes = Listbox(root)
opcoes = ['Opção 1','Opção 2','Opção 3','Opção 4']
for opcao in opcoes:
    lista_opcoes.insert(END,opcao)
lista_opcoes.pack(pady=10)

def mostrar_opcao():
    selecao = lista_opcoes.curselection()
    if selecao:
        opcao_escolhida = lista_opcoes.get(selecao)
        messagebox.showinfo('Opção',f'Você escolheu :{opcao_escolhida}')
    else:
        messagebox.showinfo('Aviso','Nenhuma opção selecionada')

botao_opcao=Button(root,text='Mostrar opção',command=mostrar_opcao)
botao_opcao.pack(pady=10)

#Radiobutton()------------------------------------------------------------------

opcao_var = StringVar(value='Opção 1') #padrão, para mostrar o radio desabilitado

label_radio = Label(root,text='Escolha uma opção: ')
label_radio.pack()

def exibir_radio():
    messagebox.showinfo('Seleção',f'Você selecionou: {opcao_var.get()}')

Radiobutton(root,text='Opçao A', variable=opcao_var,value='Opção A').pack()
Radiobutton(root,text='Opçao B', variable=opcao_var,value='Opção B').pack()

botao_radio = Button(root,text='Mostrar Escolha',command=exibir_radio)
botao_radio.pack(pady=10)

#Checkbutton() ------------------------------------------------------------------

check_var = BooleanVar()

def exibir_check():
    estado = 'marcado' if check_var.get() else 'desmarcado'
    messagebox.showinfo('Habilitado',f'O botão está {estado}')

ck = Checkbutton(root,text='Marcar', variable= check_var)
ck.pack()

botao_check = Button(root,text='Mostrar Estado',command=exibir_check)
botao_check.pack(pady=10)

#Combobox() --------------------------------------------------------------

label_combo = Label(root,text='Selecione um item: ').pack()

combo_var = StringVar()
cb = Combobox(root,textvariable=combo_var)
cb['values'] = ('Item1','Item2','Item3','Item4')
cb.current(0) #define a seleção padrão
cb.pack(pady=10)

def mostrar_combo():
    messagebox.showinfo('Paradinha2',f'Você escolheu: {combo_var.get()}')

botao_combo = Button(root,text='Mostrar',command=mostrar_combo)
botao_combo.pack()

root.mainloop()'''

#Exemplos práticos ----------------------------------------

j = Tk()
j.title('Calculo')
j.geometry('500x300')

'''def somar():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        resultado = num1 + num2
        messagebox.showinfo('Resultado',f'A soma é {resultado}')
    except ValueError:
        messagebox.showinfo('Erro!', f'Por favor digite um numero válido')

rotulo_num1 = Label(j,text='Numero 1: ')
rotulo_num1.grid(row=0,column=0,padx=10,pady=10)

entrada_num1 = Entry(j)
entrada_num1.grid(row=0,column=1,padx=10,pady=10)

rotulo_num2 = Label(j,text='Numero 2: ')
rotulo_num2.grid(row=1,column=0,padx=10,pady=10)

entrada_num2 = Entry(j)
entrada_num2.grid(row=1,column=1,padx=10,pady=10)

botao_somar = Button(j,text='Somar',command=somar)
botao_somar.grid(row=2,column=0,padx=10,pady=10)

#Converter temperatura --------------------------------------------

def converter():
    try:
        temperatura = float(entrada_temp.get())
        if opcao_var.get() =='Celsius para Fahrenheit':
            resultado = (temperatura * 9/ 5) + 32
            messagebox.showinfo('Resultado',f'{temperatura}°C é igual a {resultado:.2f}°F.')
        elif opcao_var.get() == 'Fahrenheit para Celsius':
            resultado = (temperatura -32) * 5 /9
            messagebox.showinfo('Resultado', f'{temperatura}°F é igual a {resultado:.2f}°C.')
    except ValueError:
        messagebox.showinfo('Erro','Por favor insira uma temperatura válida')

rotulo_temp = Label(j,text='Temperatura: ')
rotulo_temp.place(x=10,y=10)

entrada_temp = Entry(j)
entrada_temp.place(x= 90,y=10)

opcoes = ['Celsius para Fahrenheit','Fahrenheit para Celsius']
opcao_var = StringVar(j)
opcao_var.set(opcoes[0])

menu_opcao = OptionMenu(j,opcao_var,*opcoes)
menu_opcao.place(x=10,y=40)

botao_converter = Button(j,text='Converter',command=converter)
botao_converter.place(x=10, y=80)'''

#exemplo de adicionar/excluir/concluir -----------------------------------
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(END,tarefa)
        entrada_tarefa.delete(0,END)
    else:
        messagebox.showinfo('Aviso','Por favor insira uma tarefa')

def remover_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]
        lista_tarefas.delete(indice)
    except IndexError:
        messagebox.showinfo('Aviso','Por favor selecione uma tarefa para remover')

def marcar_concluida():
    try:
        indice = lista_tarefas.curselection()[0]
        lista_tarefas.itemconfig(indice,fg='red')
    except IndexError:
        messagebox.showinfo('Aviso', 'Por favor selecione uma tarefa para concluir')







entrada_tarefa =Entry(j,width=30)
entrada_tarefa.place(x=10,y=10)

botao_adicionar = Button(j,text='Adicionar',command=adicionar_tarefa)
botao_adicionar.place(x=10,y=40)

lista_tarefas = Listbox(j, width=50)
lista_tarefas.place(x=10,y=80)

botao_remover = Button(j,text='Excluir',command=remover_tarefa)
botao_remover.place(x=10,y=250)

botao_concluir = Button(j,text='Concluir',command=marcar_concluida)
botao_concluir.place(x=60,y=250)

j.mainloop()

'''import tkinter as tk
from tkinter import messagebox

def process():
    # Tenta converter os valores de entrada e armazená-los na lista
    try:
        # Captura os valores digitados e os converte para float
        for i in range(4):
            valor = float(entries[i].get())
            lista.append(valor)
        
        # a) Quantas vezes apareceu o valor 9
        count_nine = lista.count(9)
        
        # b) Em que posição foi digitado o primeiro valor 3
        pos_three = lista.index(3) if 3 in lista else -1
        
        # c) Quais foram os números pares
        numeros_pares = [num for num in lista if num % 2 == 0]

        # Exibe os resultados em uma caixa de mensagem
        resultado = f"Quantidade de 9: {count_nine}\n"
        resultado += f"Posição do primeiro 3: {pos_three}\n"
        resultado += f"Números pares: {numeros_pares}"
        
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Criação da janela principal
t = tk.Tk()
t.geometry('400x300')
t.title('Leitor de Valores')

# Lista para armazenar os valores
lista = []

# Labels e entradas para os quatro valores
for i in range(4):
    label = tk.Label(t, text=f'Insira o {i + 1}º valor:')
    label.pack(pady=5)
    entry = tk.Entry(t, width=10)
    entry.pack(pady=5)
    entries.append(entry)

# Botão para processar os valores
btn_process = tk.Button(t, text='Processar', command=process)
btn_process.pack(pady=10)

# Lista para armazenar as entradas
entries = []

# Inicia o loop principal
t.mainloop()

'''
from tkinter import *
from tkinter.ttk import*
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
#iniciar ventana
window = Tk()
window.title('bienvenido') #titulo de la ventana
window.geometry('500x500') #tamaño de la ventana
lbl =Label(window,text='Hola chicos', font=('Arial bold', 50))
lbl.grid(column=0,row=0)

def clickear():
    lbl.configure(text='no tengo configuracion')
# btn = Button(window, text='click',bg='pink',fg='red',padx=10, pady=10, command=clickear)
btn = Button(window, text='click', command=clickear)
btn.grid(column=1, row=0)
#texto
txt = Entry(window,width=10, state = 'disabled')
txt.grid(column=2,row=0)
txt.focus()
#cajita
combo = Combobox(window)
combo['values']=[1, 2, 3, 4, 5, 'text']
combo.current(1)
combo.grid(column=3 , row=0)
#cuadrito de checkear
chk_state = BooleanVar() #Esto no es una variable python, es una variable Tkinter
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose',var=chk_state)
chk.grid(column=4,row=0)
#crear radio button
def seleccion():
    lbl.configure(text='si tengo configuracion')
rad1 = Radiobutton(window,text='primero',value=1, command=seleccion)
rad1.grid(column=5,row=0)
rad2 = Radiobutton(window,text='segundo',value=2)
rad2.grid(column=5,row=1)
rad3 = Radiobutton(window,text='tercero',value=3)
rad3.grid(column=5,row=2)
#crear ventana emergente
def aqui():
    messagebox.showinfo('HOLA', 'No mires nunca atras')
    messagebox.showwarning('Cuidado', 'Esta es una alerta') #para mensajes de advertencia
    messagebox.showerror('Message title', 'Message content') #para mensajes de error
bot = Button(window, text ='dale aquí', command=aqui)
bot.grid(column=1, row=1)

txt1 = scrolledtext.ScrolledText(window, width = 20, height = 10) #cuadro de texto
txt1.insert(INSERT,'Hola soy un texto')
txt1.grid(column=2,row=4)
var =IntVar()
var.set(36)
spin = Spinbox(window,from_=0,to=100,width=5,textvariable = var) #seleccionar números
spin.grid(column=5,row=3)

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar",background='black')
bar = Progressbar(window, length=200,style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=2,row=5)

window.mainloop()
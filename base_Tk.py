from cProfile import label
from tkinter import *

janela = Tk()

janela.title('Base TK')
janela.geometry('500x300')
janela.configure(background='#dde')

txt1 = Label(
    janela,text=('Seja Bem vindo'),
    font='Arial',
    background='blue',
    foreground='white')
txt1.place(x=10,y=10,width=150,height=20)

vtxt = 'Texto 2'
vgb = 'black'
vfg = 'white'
text2 = Label(janela,text=vtxt,font='Arial',background=vgb,foreground=vfg)
text2.pack(ipadx=20,ipady=20,padx=5,pady=5,side='top',fill=X,expand=True)

janela.mainloop()
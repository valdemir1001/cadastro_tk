from tkinter import *
import os

c = os.path.dirname(__file__)
nomeArquivo = c+ '\\cadastro.txt'

def imprimir_click():
    arquivo = open(nomeArquivo,'a')

    arquivo.write("Nome........: %s " % vnome.get())
    arquivo.write("\nTelefone..: %s " % vfone.get())
    arquivo.write("\nE-mail....: %s " % vemail.get())
    arquivo.write("\nOBS.......: %s " % vobs.get('1.0',END))
    arquivo.write("\n\n")
    arquivo.close()
    


janela = Tk()
janela.title('Base TK')
janela.geometry('500x300')
janela.configure(background='#dde')
janela.iconbitmap('img\python_p.ico')


#ancor=> N=Norte, S=Sul, E=Leste, W=Oeste
#NE=Nordeste, NW=NorOeste, SE=Sudeste, SW=SudOeste

#____________ Início do nome____________

label = Label(janela,text='Nome',
    background='#dde',
    foreground='black',
    anchor=W).place(x=10,y=10,width=100,height=20)

vnome = Entry(janela)
vnome.place(x=10,y=30,width=200,height=20)

#____________ Fim do nome____________

#____________ Início do Telefone____________

label = Label(janela,text='Telefone',
    background='#dde',
    foreground='black',
    anchor=W).place(x=10,y=60,width=100,height=20)

vfone = Entry(janela)
vfone.place(x=10,y=80,width=100,height=20)

#____________ Fim do Telefone____________

#____________ Início do Email____________

label = Label(janela,text='E-Mail',
    background='#dde',
    foreground='black',
    anchor=W).place(x=10,y=110,width=100,height=20)

vemail = Entry(janela)
vemail.place(x=10,y=130,width=200,height=20)

#____________ Fim do email____________

#____________ Início da Observação____________

Label(janela,text='Observação',
    background='#dde',
    foreground='black',
    anchor=W).place(x=10,y=160,width=100,height=20)

vobs = Text(janela)
vobs.place(x=10,y=180,width=200,height=80)

#____________ Fim da Observação____________

bnt = Button(janela,text='Salvar',command=imprimir_click)
bnt.place(x=10,y=270,width=100,height=20)

bnt = Button(janela,text='Gravar',command=imprimir_click)
bnt.place(x=10,y=270,width=100,height=20)

janela.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:12:48 2021

@author: Daniel Esquivias Romo
"""

import tkinter
from tkinter import *
from random import choice

#-----------------------------declaraciones-----------------------------------------------------------------------------------------------
ventana = tkinter.Tk()
ventana.geometry("1400x700")
ventana.title("INVESTIGATOR")
ventana.configure(bg='#6176AB')
ventana.resizable(False,False)


etiqueta = tkinter.Label(ventana, text = "Investigator", font = "Helvetica 80")
etiqueta.pack()
etiqueta.place( x=400, y = 10)
etiqueta.configure(bg='#6176AB')

etiquetan = tkinter.Label(ventana, text = "Por: Daniel Esquivias Romo", font = "Helvetica 10")
etiquetan.pack()
etiquetan.place( x=10, y = 10)
etiquetan.configure(bg='#6176AB')






etiqueta2 = tkinter.Label(ventana, text = "Lugar: (Atico, Jardin, Habitacion, Cocina o Baño)", font = "Arial 15")
etiqueta2.pack()
etiqueta2.place( x=100, y = 200)
etiqueta2.configure(bg='#6176AB')

cajatexto = tkinter.Entry(ventana, font = "Arial 15")
cajatexto.pack()
cajatexto.place( x=100, y = 250)


etiqueta3 = tkinter.Label(ventana, text = "Arma: (Tubo, Pistola, Cuerda, Cuchillo o Veneno)", font = "Arial 15")
etiqueta3.pack()
etiqueta3.place( x=100, y = 300)
etiqueta3.configure(bg='#6176AB')

cajatexto2 = tkinter.Entry(ventana, font = "Arial 15")
cajatexto2.pack()
cajatexto2.place( x=100, y = 350)

etiqueta4 = tkinter.Label(ventana, text = "Persona: (Dimitri, Anna, Kim, Willy o Pema)", font = "Arial 15")
etiqueta4.pack()
etiqueta4.place( x=100, y = 400)
etiqueta4.configure(bg='#6176AB')

cajatexto3 = tkinter.Entry(ventana, font = "Arial 15")
cajatexto3.pack()
cajatexto3.place( x=100, y = 450)

etiqueta4 = tkinter.Label(ventana, font = "Arial 15")
etiqueta4.pack()
etiqueta4.place( x=100, y = 500)
etiqueta4.configure(bg='#6176AB')



canvas2 = Canvas(width = 800, height = 460, bg= '#91D8EA')#lugares
canvas2.pack()
canvas2.place( x=550, y = 200)

canvas3 = Canvas(width = 800, height = 460, bg= '#91D8EA')#armas
canvas3.pack()
canvas3.place( x=550, y = 200)

canvas = Canvas(width = 800, height = 460, bg= '#91D8EA')#personajes
canvas.pack()
canvas.place( x=550, y = 200)



#-------------------------------------------------------------------------------------------------------------------------------------

dimitri = PhotoImage(file = 'dimitri.png')
canvas.create_image(0,0, image = dimitri, anchor=NW)

willy = PhotoImage(file = 'willy.png')
canvas.create_image(160,0, image = willy, anchor=NW)

kim = PhotoImage(file = 'kim.png')
canvas.create_image(320,0, image = kim, anchor=NW)

anna = PhotoImage(file = 'anna.png')
canvas.create_image(480,0, image = anna, anchor=NW)

pema = PhotoImage(file = 'pema.png')
canvas.create_image(640,0, image = pema, anchor=NW)
#-------------------------------------------------------------------------------------------------------------------------------------

tubo = PhotoImage(file = 'tubo.png')
canvas3.create_image(0,0, image = tubo, anchor=NW)

pistola = PhotoImage(file = 'pistola.png')
canvas3.create_image(160,0, image = pistola, anchor=NW)

cuerda = PhotoImage(file = 'cuerda.png')
canvas3.create_image(320,0, image = cuerda, anchor=NW)

veneno = PhotoImage(file = 'veneno.png')
canvas3.create_image(480,0, image = veneno, anchor=NW)

cuchillo = PhotoImage(file = 'cuchillo.png')
canvas3.create_image(640,0, image = cuchillo, anchor=NW)

lugares = PhotoImage(file = 'lugares.png')
canvas2.create_image(0,0, image = lugares, anchor=NW)
#-------------------------------------------------------------------------------------------------------------------------------------

global per
global lug
global arm
global zx

global SC
global SA
global SB
#-----------------------------------------------inicio--------------------------------------------------------------------------------
#-----------------------RANDOMIZED-------------------------------
Weapon = ['tubo', 'pistola', 'cuerda', 'cuchillo', 'veneno']
Room = ['atico', 'jardin', 'habitacion', 'cocina', 'baño']
People = ['dimitri', 'anna', 'kim', 'willy', 'pema']

def restart(Weapon,Room,People):
    global SC
    global SA
    global SB
    #print(Weapon) #Lista antes de eliminar eleccion
    wea_rnd = choice(Weapon) #selecciona arma al azar
    SC = wea_rnd
    #print(SC)
    #Weapon.remove(SC)#elimina de la lista inicial el objeto escogido al azar
    #print(Weapon)
    #----------------------------------------------------
    #print(Room) #Lista antes de eliminar eleccion
    room_rnd = choice(Room) #selecciona room al azar
    SB = room_rnd
    #print(SB)
    #Room.remove(SB)
    #print(Room)
    #---------------------------------------------------
    #print(People) #Lista antes de eliminar eleccion
    ppl_rnd = choice(People) #selecciona room al azar
    SA = ppl_rnd
    #print(SA)
    #People.remove(SA)
    #print(People)
restart(Weapon,Room,People)
#-------------------------------------------------
#-----------------------------------------funciones-----------------------------------------------------------------------------------
def textodeLaCaja():
    global per
    global lug
    global arm
    lug = cajatexto.get()
    lug = lug.lower()
    arm = cajatexto2.get()
    arm = arm.lower()
    per = cajatexto3.get()
    per = per.lower()
    


#----------------------------------------funcion juego-------------------------------------------
def juego(pp,pl,pa,SA,SB,SC):
    #print(lug)
    #print(per)
    #print(arm)
    if pa == SC and pl == SB and pp == SA:
        etiqueta4["text"] = 'Ha descubierto quien es el asesino, Felicidades!'
        #print('Ha descubierto quien es el asesino, Felicidades!')
        final()
    elif pl == SB:
        etiqueta4["text"] = 'Ha encontrado una pista adivinaste algo'
        #print('Ha encontrado una pista adivinaste algo')

    elif pa == SC:
        etiqueta4["text"] = 'Ha encontrado una pista adivinaste algo'
        #print('Ha encontrado una pista adivinaste algo')

    elif pp == SA:
        etiqueta4["text"] = 'Ha encontrado una pista adivinaste algo'
        #print('Ha encontrado una pista adivinaste algo')

    else:
        etiqueta4["text"] = 'No encontraste ninguna pista'
        #print("No encontraste ninguna pista")
        

        
    

#--------------------------------------------------------------------------------------------

def onclick():
    global SC
    global SA
    global SB
    global per
    global lug
    global arm
    textodeLaCaja()
    juego(per,lug,arm,SA,SB,SC)
    
 
def onclick2():
    restart(Weapon,Room,People)
    finala()
    
def onclickp():
    canvas.grid(padx=550, pady = 200)
    canvas2.grid_remove()
    canvas3.grid_remove()


    
def onclicka():
    canvas3.grid(padx=550, pady = 200)
    canvas2.grid_remove()
    canvas.grid_remove()

    
def onclickl():
    canvas2.grid(padx=550, pady = 200)
    canvas.grid_remove()
    canvas3.grid_remove()

 
def onclickt(): 
    canvast.destroy()
    botont.destroy()
    canvas.grid(padx=550, pady = 200)
    canvas2.grid_remove()
    canvas3.grid_remove()

def onclick12(): 
    canvas12.destroy()
    boton12.destroy()

def onclick13(): 
    canvas13.destroy()
    boton13.destroy()

def onclickdimi2(): 
    canvasd.destroy()
    botond.destroy()
    
def onclickwilly2(): 
    canvasw.destroy()
    botonw.destroy()
    
def onclickkim2(): 
    canvask.destroy()
    botonk.destroy()
    
def onclickanna2(): 
    canvasa.destroy()
    botona.destroy()
    
    
def onclickpema2(): 
    canvasp.destroy()
    botonp.destroy()
#---------------------------------------Ventanas files--------------------------------------------------------

def onclickdimi():
      Otraventana.state(newstate = "normal")
      ventana.state(newstate = "withdraw")


def funcion2():
      Otraventana.state(newstate = "withdraw")
      ventana.state(newstate = "normal") 
#----------------------

def onclickwilly():
      Otraventana2.state(newstate = "normal")
      ventana.state(newstate = "withdraw")

def funcion22():
      Otraventana2.state(newstate = "withdraw")
      ventana.state(newstate = "normal") 
#--------------------

def onclickkim():
      Otraventana3.state(newstate = "normal")
      ventana.state(newstate = "withdraw")

def funcion23():
      Otraventana3.state(newstate = "withdraw")
      ventana.state(newstate = "normal")

#------------------
def onclickanna():
      Otraventana4.state(newstate = "normal")
      ventana.state(newstate = "withdraw")

def funcion24():
      Otraventana4.state(newstate = "withdraw")
      ventana.state(newstate = "normal")
#------------------
def onclickpema():
      Otraventana5.state(newstate = "normal")
      ventana.state(newstate = "withdraw")

def funcion25():
      Otraventana5.state(newstate = "withdraw")
      ventana.state(newstate = "normal")

#------------------
def final():
      Otraventanaf.state(newstate = "normal")
      ventana.state(newstate = "withdraw")
      finala()

def funcion2f():
      Otraventanaf.state(newstate = "withdraw")
      ventana.state(newstate = "normal")

#-------------------------------------------------------------------------------------------------------------

botondimitri = tkinter.Button(canvas, text = "Dimitri", padx = 10, pady = 5, command= onclickdimi, font = "Arial 10")
botondimitri.pack()    
botondimitri.place( x=45, y = 160)

botonwilly = tkinter.Button(canvas, text = "Willy", padx = 10, pady = 5, command= onclickwilly, font = "Arial 10")
botonwilly.pack()    
botonwilly.place( x=210, y = 160)

botonkim = tkinter.Button(canvas, text = "Kim", padx = 10, pady = 5, command= onclickkim, font = "Arial 10")
botonkim.pack()    
botonkim.place( x=370, y = 160)

botonanna = tkinter.Button(canvas, text = "Anna", padx = 10, pady = 5, command= onclickanna, font = "Arial 10")
botonanna.pack()    
botonanna.place( x=530, y = 160)

botonpema = tkinter.Button(canvas, text = "Pema", padx = 10, pady = 5, command= onclickpema, font = "Arial 10")
botonpema.pack()    
botonpema.place( x=690, y = 160)

#--------------------------------------------------------------------------------------------------------------
boton = tkinter.Button(ventana, text = "Continuar", padx = 64, pady = 5, command= onclick, font = "Arial 15")
boton.pack()    
boton.place( x=100, y = 550)

botonf = tkinter.Button(ventana, text = "Reiniciar Juego", padx = 50, pady = 5, command= onclick2, font = "Arial 10")
botonf.pack()    
botonf.place( x=2, y = 660)

botonp = tkinter.Button(ventana, text = "Personajes", padx = 50, pady = 5, command= onclickp, font = "Arial 10")
botonp.pack()    
botonp.place( x=650, y = 150)

botona = tkinter.Button(ventana, text = "Armas", padx = 50, pady = 5, command= onclicka, font = "Arial 10")
botona.pack()    
botona.place( x=900, y = 150)

botonl = tkinter.Button(ventana, text = "Lugares", padx = 50, pady = 5, command= onclickl, font = "Arial 10")
botonl.pack()    
botonl.place( x=1100, y = 150)


#--------------------------------------------boton personajes------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------

canvasp = Canvas(width = 1400, height = 700, bg= '#6176AB')#pantalla principal
canvasp.pack()
canvasp.place( x=0, y = 0) 

filep = PhotoImage(file = 'filep.png')
canvasp.create_image(0,0, image = filep, anchor=NW)

botonp = tkinter.Button(ventana, text = "Siguiente", padx = 20, pady = 5, command= onclickpema2, font = "Arial 20")
botonp.pack()    
botonp.place( x=1200, y = 10)

#-----------------------

canvasa = Canvas(width = 1400, height = 700, bg= '#6176AB')#pantalla principal
canvasa.pack()
canvasa.place( x=0, y = 0) 

filea = PhotoImage(file = 'filea.png')
canvasa.create_image(0,0, image = filea, anchor=NW)

botona = tkinter.Button(ventana, text = "Siguiente", padx = 20, pady = 5, command= onclickanna2, font = "Arial 20")
botona.pack()    
botona.place( x=1200, y = 10)

#-----------------------
canvask = Canvas(width = 1400, height = 700, bg= '#6176AB')#pantalla principal
canvask.pack()
canvask.place( x=0, y = 0) 

filek = PhotoImage(file = 'filek.png')
canvask.create_image(0,0, image = filek, anchor=NW)

botonk = tkinter.Button(ventana, text = "Siguiente", padx = 20, pady = 5, command= onclickkim2, font = "Arial 20")
botonk.pack()    
botonk.place( x=1200, y = 10)

#-----------------------

canvasw = Canvas(width = 1400, height = 700, bg= '#6176AB')#pantalla principal
canvasw.pack()
canvasw.place( x=0, y = 0) 

filew = PhotoImage(file = 'filew.png')
canvasw.create_image(0,0, image = filew, anchor=NW)

botonw = tkinter.Button(ventana, text = "Siguiente", padx = 20, pady = 5, command= onclickwilly2, font = "Arial 20")
botonw.pack()    
botonw.place( x=1200, y = 10)

#-----------------------
canvasd = Canvas(width = 1400, height = 700, bg= '#6176AB')#pantalla principal
canvasd.pack()
canvasd.place( x=0, y = 0) 

filed = PhotoImage(file = 'filed.png')
canvasd.create_image(0,0, image = filed, anchor=NW)

botond = tkinter.Button(ventana, text = "Siguiente", padx = 20, pady = 5, command= onclickdimi2, font = "Arial 20")
botond.pack()    
botond.place( x=1200, y = 10)
#------------------

canvas13 = Canvas(width = 1400, height = 700, bg= '#6176AB')#pantalla principal
canvas13.pack()
canvas13.place( x=0, y = 0) 

file13 = PhotoImage(file = 'historia2.png')
canvas13.create_image(0,0, image = file13, anchor=NW)

boton13 = tkinter.Button(ventana, text = "Siguiente", padx = 20, pady = 5, command= onclick13, font = "Arial 20")
boton13.pack()    
boton13.place( x=1200, y = 10)

#----------------------
canvas12 = Canvas(width = 1400, height = 700, bg= '#6176AB')#pantalla principal
canvas12.pack()
canvas12.place( x=0, y = 0) 

file12 = PhotoImage(file = 'historia1.png')
canvas12.create_image(0,0, image = file12, anchor=NW)

boton12 = tkinter.Button(ventana, text = "Siguiente", padx = 20, pady = 5, command= onclick12, font = "Arial 20")
boton12.pack()    
boton12.place( x=1200, y = 10)
    
#------------------------------------------------------------------------------------------------------------------      
canvast = Canvas(width = 1400, height = 700, bg= '#6176AB')#pantalla principal
canvast.pack()
canvast.place( x=0, y = 0) 

cover = PhotoImage(file = 'coverpage.png')
canvast.create_image(0,0, image = cover, anchor=NW)

botont = tkinter.Button(ventana, text = "Comenzar Juego", padx = 20, pady = 5, command= onclickt, font = "Arial 30")
botont.pack()    
botont.place( x=550, y = 300)

#----------------------------------------------------------------------------------------------------------------------------




Otraventana = Toplevel()
Otraventana.state(newstate = "withdraw")
Otraventana.geometry("1400x700")
Otraventana.title("Documentación")


img = PhotoImage(file='filed.PNG')

miEtiqueta = Label(Otraventana, image=img)
miEtiqueta.pack()

abrirVentana1 = Button(Otraventana, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion2)
abrirVentana1.pack()
abrirVentana1.place( x=1200, y = 10)
#------------------------
Otraventana2 = Toplevel()
Otraventana2.state(newstate = "withdraw")
Otraventana2.geometry("1400x700")
Otraventana2.title("Documentación")


img2 = PhotoImage(file='filew.PNG')

miEtiqueta2 = Label(Otraventana2, image=img2)
miEtiqueta2.pack()

abrirVentana12 = Button(Otraventana2, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion22)
abrirVentana12.pack()
abrirVentana12.place( x=1200, y = 10)
#-----------------------

Otraventana3 = Toplevel()
Otraventana3.state(newstate = "withdraw")
Otraventana3.geometry("1400x700")
Otraventana3.title("Documentación")


img3 = PhotoImage(file='filek.PNG')

miEtiqueta3 = Label(Otraventana3, image=img3)
miEtiqueta3.pack()

abrirVentana13 = Button(Otraventana3, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion23)
abrirVentana13.pack()
abrirVentana13.place( x=1200, y = 10)
#-----------------------

Otraventana4 = Toplevel()
Otraventana4.state(newstate = "withdraw")
Otraventana4.geometry("1400x700")
Otraventana4.title("Documentación")


img4 = PhotoImage(file='filea.PNG')

miEtiqueta4 = Label(Otraventana4, image=img4)
miEtiqueta4.pack()

abrirVentana14 = Button(Otraventana4, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion24)
abrirVentana14.pack()
abrirVentana14.place( x=1200, y = 10)
#------------------------

Otraventana5 = Toplevel()
Otraventana5.state(newstate = "withdraw")
Otraventana5.geometry("1400x700")
Otraventana5.title("Documentación")


img5 = PhotoImage(file='filep.PNG')

miEtiqueta5 = Label(Otraventana5, image=img5)
miEtiqueta5.pack()

abrirVentana15 = Button(Otraventana5, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion25)
abrirVentana15.pack()
abrirVentana15.place( x=1200, y = 10)

#------------------------

Otraventanaf = Toplevel()
Otraventanaf.state(newstate = "withdraw")
Otraventanaf.geometry("1400x700")
Otraventanaf.title("Documentación")


imgf = PhotoImage(file='final.PNG')

miEtiquetaf = Label(Otraventanaf, image=imgf)
miEtiquetaf.pack()

canvasf = Canvas(Otraventanaf, width =800, height = 200, bg= 'white')#personajes
canvasf.pack()
canvasf.place( x=60, y = 250)

T = tkinter.Text(canvasf, height=100, width=300)
T.pack()
quote = """a"""
T.insert(tkinter.END, quote)
T.place( x=0, y = 0)
#------------------------------------------------------------------------------------------------------------------------------------

def finala():   
    if SA == 'dimitri':
        T = tkinter.Text(canvasf, height=100, width=300)
        T.pack()
        quote = """Tras la caída de la unión soviética y afectado de por vida con cicatrices
mentales de las atrocidades que Dimitri cometió, fue un gran cambio para un hombre que
fue entrenado como una maquina para matar de la nada cambiar su modo de vida y no volverá 
lastimar a otra persona, Dimitri solo buscó un motivo para poder satisfacer su sed de sangre,
encontrando la situación perfecta estar encerrado en una casa con 5 personas decide planear el 
asesinato, vigilando cada movimiento de la víctima, así logrando estar solo con el donde
utilizo lo primero que encontró en ese lugar para cometer el asesinato creyendo 
haberse salido con la suya pero nadie esperaba que el gran detective llegara y resolviera el caso."""
        T.insert(tkinter.END, quote)
        T.place( x=0, y = 0)
    elif SA == 'willy':
        T = tkinter.Text(canvasf, height=100, width=300)
        T.pack()
        quote = """¿La pregunta es, por que lo hizo William? Cuál sería su razón para cometer tal atrocidad,
nadie nunca pensó que William la persona mas inocente de los sujetos encerrados en esa propiedad 
pudiera llevar la victima a  su muerte. William terminando, siendo el más peligroso de los subjetos."""
        T.insert(tkinter.END, quote)
        T.place( x=0, y = 0)
    elif SA == 'pema':
        T = tkinter.Text(canvasf, height=100, width=300)
        T.pack()
        quote = """Siendo un monje nadie pudo imaginarse que Pema pudiera haber asesinado a alguien. 
El monje tenia que tener una buena razón para hacerlo ya que la práctica de su religión nunca
le permitiría hacer esta atrocidad, nunca sabremos la razón de el Monje para cometer este acto
contra nuestra víctima, las autoridades lo han encerrado en confinamiento hasta nuevo aviso."""
        T.insert(tkinter.END, quote)
        T.place( x=0, y = 0)
    elif SA == 'anna':
        T = tkinter.Text(canvasf, height=100, width=300)
        T.pack()
        quote = """Anna, muchos dirían que es una mujer calmada, una científica formal en su área de trabajo,
pero nadie sospecho que quizás ella estaba trabajando en algo peligroso. Anna al descubrir que alguien
se enteró de lo que estaba planeando no dudo ni un momento en silenciar a esta persona llevando a la 
víctima a un lugar solo donde la agredió hasta su muerte,  creyendo haberse salido con la suya pero 
nadie esperaba que el gran detective llegara y resolviera el caso."""
        T.insert(tkinter.END, quote)
        T.place( x=0, y = 0)
    elif SA == 'kim':
        T = tkinter.Text(canvasf, height=100, width=300)
        T.pack()
        quote = """Nadie nunca supo nada del pasado de Kim, una mujer misteriosa que logró escapar de la nación 
con mas secretos en el mundo no era sorpresa que saliera algo de ella a la luz, para la mala suerte de
nuestra víctima, lo descubrió de la peor manera."""
        T.insert(tkinter.END, quote)
        T.place( x=0, y = 0)
#----------------------------------------------------------------------------------------------------------------------------------
abrirVentana1f = Button(Otraventanaf, text="Abrir ventana principal", bg="white", font= ("Times New Roman", 12), fg="black", command=funcion2f)
abrirVentana1f.pack()
abrirVentana1f.place( x=1200, y = 10)


#------------------------

Otraventana.mainloop()
Otraventana2.mainloop()
Otraventana3.mainloop()
Otraventana4.mainloop()
Otraventana5.mainloop()
ventana.mainloop()
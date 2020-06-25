from tkinter import *
root = Tk()

miFrame = Frame(root)
miFrame.pack()

operacion= ""

resultado = 0


#--------------------------- PANTALLA ---------------------------
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable = numeroPantalla)
pantalla.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

def numeroPulsado(num):
    global operacion
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get()+num)
    
#--------------------------- PANTALLA ---------------------------
def suma(num):
    global operacion
    global resultado
    resultado += float(num)
    operacion = "suma"
    numeroPantalla.set(resultado)

#--------------------------- PANTALLA ---------------------------
def elResultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0


#--------------------------- PANTALLA ---------------------------
#--------------------------- PANTALLA ---------------------------
#--------------------------- PANTALLA ---------------------------



#--------------------------- PANTALLA ---------------------------
boton7 = Button(miFrame, text = "7", width=3, command= lambda:numeroPulsado("7"))
boton7.grid(row=2, column=0)
boton8 = Button(miFrame, text = "8", width=3, command= lambda:numeroPulsado("8"))
boton8.grid(row=2, column=1)
boton9 = Button(miFrame, text = "9", width=3, command= lambda:numeroPulsado("9"))
boton9.grid(row=2, column=2)
botonDiv = Button(miFrame, text = "/", width=3, command= lambda:numeroPulsado("/"))
botonDiv.grid(row=2, column=3)

#--------------------------- PANTALLA ---------------------------
boton4 = Button(miFrame, text = "4", width=3, command= lambda:numeroPulsado("4"))
boton4.grid(row=3, column=0)
boton5 = Button(miFrame, text = "5", width=3, command= lambda:numeroPulsado("5"))
boton5.grid(row=3, column=1)
boton6 = Button(miFrame, text = "6", width=3, command= lambda:numeroPulsado("6"))
boton6.grid(row=3, column=2)
botonMult = Button(miFrame, text = "X", width=3, command= lambda:numeroPulsado("*"))
botonMult.grid(row=3, column=3)

#--------------------------- PANTALLA ---------------------------
boton1 = Button(miFrame, text = "1", width=3, command= lambda:numeroPulsado("1"))
boton1.grid(row=4, column=0)
boton2 = Button(miFrame, text = "2", width=3, command= lambda:numeroPulsado("2"))
boton2.grid(row=4, column=1)
boton3 = Button(miFrame, text = "3", width=3, command= lambda:numeroPulsado("3"))
boton3.grid(row=4, column=2)
botonRest = Button(miFrame, text = "-", width=3, command= lambda:numeroPulsado("-"))
botonRest.grid(row=4, column=3)
#--------------------------- PANTALLA ---------------------------
boton0 = Button(miFrame, text = "0", width=3, command= lambda:numeroPulsado("0"))
boton0.grid(row=5, column=0)
botonComa = Button(miFrame, text = ",", width=3, command= lambda:numeroPulsado(","))
botonComa.grid(row=5, column=1)
botonIgual = Button(miFrame, text = "=", width=3, command= lambda:elResultado())
botonIgual.grid(row=5, column=2)
botonSuma = Button(miFrame, text = "+", width=3, command= lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=3)

#--------------------------- PANTALLA ---------------------------

#--------------------------- PANTALLA ---------------------------

#--------------------------- PANTALLA ---------------------------


root.mainloop()
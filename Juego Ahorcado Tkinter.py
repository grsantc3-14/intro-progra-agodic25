##Juego Ahorcado Tkinter
from tkinter import *
import tkinter as tk
root = Tk()
root.title("Juego del Ahorcado")
C = Canvas(root, bg="white",height=400, width=600)

#Zacate
pisoZacate=C.create_rectangle(0, 200, 600, 600, fill="green", outline="black", width=2)
C.tag_lower(pisoZacate)
#Creando un letrero
label = tk.Label(root, text="Bienvenido")
label.pack()


#Dibujando al mono
poste=C.create_rectangle(100,30,110,340,fill="black")
brazoPoste=C.create_rectangle(80,40,195,50,fill="black")
basePoste=C.create_rectangle(80,340,300,360,fill="black")
cabeza=C.create_oval(170,75,220,125, fill="white", outline="black", width=7)
cuerpo=C.create_rectangle(190,130,200,250,fill="black")
piernaIzq=C.create_polygon(200,250,300,280,280,260,200,230, fill="black", outline="yellow")
#Boton
botonInicio=Button(root, text="Iniciar Juego")
botonInicio.pack()

C.pack()

mainloop()
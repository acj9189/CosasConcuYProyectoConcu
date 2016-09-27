from tkinter import *
import tkinter as tk
from Clases.Automata import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.TipoCreacion = "MG"

        self.AutomataAnalisis = Automata()
        Automata.crearEstado("hola",0,0,True,True)


        self.pack()
        self.create_widgets()
        #menu
        barraMenu = Menu(self)
        mnuArchivo = Menu(barraMenu)
        #subMenu
        mnuCrearAuto = Menu(self)

        #menu
        mnuArchivo.add_cascade(label="Crear Automata",menu=mnuCrearAuto)

        #subMenu
        mnuCrearAuto.add_cascade(label="Por Grafico",command = self.MG)
        mnuCrearAuto.add_cascade(label="Por Tabla",command = self.MT)
        mnuCrearAuto.add_cascade(label="Por Quintupla",command = self.MF)

        #menu

        mnuArchivo.add_command(label="Cargar Automata")
        mnuArchivo.add_command(label="Guardar Automata")
        mnuArchivo.add_command(label="Salir",command=root.destroy)
        barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)

        root.configure(menu=barraMenu)

        #Agregar canvas para dibujar
        self.canvas = Canvas(root, background='white')
        self.canvas.pack(expand = YES, fill = BOTH)
        #self.canvas.bind('<Button-1>', self.on_click)


    def create_widgets(self):
    	pass

    def MG(self):
    	self.TipoCreacion = "MG"
    	print(self.TipoCreacion)

    def MT(self):
    	self.TipoCreacion = "MT"
    	print(self.TipoCreacion)

    def MF(self):
    	self.TipoCreacion = "MF"
    	print(self.TipoCreacion)




root = tk.Tk()
root.geometry("800x600+0+0")
root.title("Ventana Principal")

#mnuCrearAuto = Menu(barraMenu)


app = Application(master=root)

#root.mainloop()
app.mainloop()
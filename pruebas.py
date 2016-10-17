
from Clases.Automata import *
from Interfaces.clsVentanaQuintupla import*

""""class P():
	def __init__(self):
		self.AutomataAnalisis = Automata()

		#Automata.crearEstado(self,"AFD-AFN", "hola", 0, 0, True, True)

	def llamarCrearEstado(self, estadoNombre, posX, posY, esEstadoInicial, esEstadoAceptador):
		self.AutomataAnalisis.crearEstado(estadoNombre, posX , posY, esEstadoInicial, esEstadoAceptador)

	def llamarCrearTransicion(self):
		estadoOrigen = self.AutomataAnalisis.listaEstados[0]
		estadoDestino = self.AutomataAnalisis.listaEstados[0]
		simbolo = "a"
		#return self.AutomataAnalisis.crearTransicion(estadoOrigen, estadoDestino, simbolo)
		self.AutomataAnalisis.crearTransicion(estadoOrigen, estadoDestino, simbolo)







P = P()
P.llamarCrearEstado("q0", 0, 0, False, False)
#P.llamarCrearEstado("q1", 0, 0, False, False)
print(P.llamarCrearTransicion())
#hola

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")), defaultextension=".acj")
print (root.filename)

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
#root.filename = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
arhivo = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("acj files","*.acj"),("all files","*.*")), defaultextension=".acj")
#print (root.filename)
print(arhivo)"""

H = Ventana("quintupla")
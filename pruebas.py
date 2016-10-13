
from Clases.Automata import *

class P():
	def __init__(self):
		self.AutomataAnalisis = Automata()

		#Automata.crearEstado(self,"AFD-AFN", "hola", 0, 0, True, True)

	def llamarCrearEstado(self, estadoNombre, posX, posY, esEstadoInicial, esEstadoAceptador):
		self.AutomataAnalisis.crearEstado(estadoNombre, posX , posY, esEstadoInicial, esEstadoAceptador)







P = P()
P.llamarCrearEstado("q0", 0, 0, False, False)
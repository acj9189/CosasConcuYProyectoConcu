from Estado import *
from Transicion import *

class Automata(object):

	def __init__(self):
		self.listaEstados = []
		self.esDeterminista = False
		self.tieneEstadoInicial = False
		self.tieneEstadoFinal = False
		self.tipodeAutomata = "AFD-AFN"
		print(self.tipodeAutomata)

	def crearEstado(self, estadoNombre, posX, posY, esEstadoInicial, esEstadoAceptador):

		if(self.tipodeAutomata == "AFD-AFN"):
			#print(self.tipodeAutomata)
			#self.listaEstados.append("hola")
			#print(self.listaEstados[0])
			self.listaEstados.append(Estado(estadoNombre, Transicion(), posX, posY, esEstadoInicial, esEstadoAceptador))

		elif(self.tipodeAutomata == "MME"):
			pass
		elif(self.tipodeAutomata == "MMO"):
			pass
		elif(self.tipodeAutomata == "PILA"):
			pass



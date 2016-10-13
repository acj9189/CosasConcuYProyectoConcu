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
			listaTransiciones = []
			self.listaEstados.append(Estado(estadoNombre, listaTransiciones, posX, posY, esEstadoInicial, esEstadoAceptador))
			#self.listaEstados.append(Estado(estadoNombre, [], posX, posY, esEstadoInicial, esEstadoAceptador))

		elif(self.tipodeAutomata == "MME"):
			pass
		elif(self.tipodeAutomata == "MMO"):
			pass
		elif(self.tipodeAutomata == "PILA"):
			pass

	def crearTransicion(self, estadoOrigen, estadoDestino, simbolo):
		numEstados = len(self.listaEstados)
		print(numEstados)
		if(numEstados > 1):

			if(self.tipodeAutomata == "AFD-AFN"):

				nuevaTransicion = Transicion()
				nuevaTransicion.crearTransicion(estadoOrigen, estadoDestino,simbolo)
				estadoOrigen.listaTransiciones.append(nuevaTransicion)
				print("se creo")

			elif(self.tipodeAutomata == "MME"):
				pass
			elif(self.tipodeAutomata == "MMO"):
				pass
			elif(self.tipodeAutomata == "PILA"):
				pass

		else:
			return "No hay suficientes estados para crear una transicion"




#from Estado import Estado
#from Transicion import Transicion

class Automata(object):

	def __init__(self):
		listaEstados = []
		esDeterminista = False
		tieneEstadoInicial = False
		tieneEstadoFinal = False
		tipodeAutomata = "AFD-AFN"

	def crearEstado(self, estadoNombre, posX, PosY, esEstadoInicial, esEstadoAceptador):
		if self.tipodeAutomata == "AFD-AFN":
			self.listaEstados.append(Estado(estadoNombre, Transicion(), posX, PosY, esEstadoInicial, esEstadoAceptador))
		elif(self.tipodeAutomata == "MME"):
			pass
		elif(self.tipodeAutomata == "MMO"):
			pass
		elif(self.tipodeAutomata == "PILA"):
			pass

	def validarSiTieneEstadosFinalesInicial(self):
		if((self.tieneEstadoInicial == False) or (self.tieneEstadoFinal == False)):
			return "NO"
		else:
			return "SI"

	def crearTransicion(self):
		pass

	def realizarReversa(self):
		pass
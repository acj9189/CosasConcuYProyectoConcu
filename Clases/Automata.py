from Estado import Estado
from Transicion import Transicion

class Automata:

	def __init__(self):
		self.listaEstados
		self.esDeterminista = False
		self.tieneEstadoInicial = False
		self.tieneEstadoFinal = False

	def crearEstado(self, estadoNombre, posX, PosY, esEstadoInicial, esEstadoAceptador):
		self.listaEstados.append(Estado(estadoNombre, Transicion(), posX, PosY, esEstadoInicial, esEstadoAceptador))

	def validarSiTieneEstadosFinaleINicial(self):
		if((self.tieneEstadoInicial == False) or (self.tieneEstadoFinal == False)):
			return "NO"
		else:
			return "SI"





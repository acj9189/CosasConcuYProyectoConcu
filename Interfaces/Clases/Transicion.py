
from Estado import *


class Transicion(object):

	def __init__(self):
		self.estadoOrigen = None
		self.estadoDestino = None
		self.simboloT = None
		self.simboloSalida = None


	""""def __init__(self, estadoOrigen, estadoDestino,simboloT):
		self.estadoOrigen = estadoOrigen
		self.estadoDestino = estadoDestino
		self.simboloT = simboloT"""

	def crearTransicion(self, estadoOrigen, estadoDestino, simboloT):
		self.estadoOrigen = estadoOrigen
		self.estadoDestino = estadoDestino
		self.simboloT = simboloT

	def crearTransicionMME(self, estadoOrigen, estadoDestino, simboloT, simboloSalida):
		self.estadoOrigen = estadoOrigen
		self.estadoDestino = estadoDestino
		self.simboloT = simboloT
		self.simboloSalida = simboloSalida

	def getSimboloSalida(self):
		return self.simboloSalida

 	def setSimboloSalida(self, simboloMME):
 		self.simboloSalida = simboloMME

	def getestadoOrigen(self):
		return self.estadoOrigen

	def getestadoDestino(self):
		return self.estadoDestino

	def setestadoOrigen(self, estado):
		self.estadoOrigen = estado

	def setestadoDestino(self, estado):
		self.estadoDestino = estado

	def getSimbolo(self):
		return self.simboloT

	def setSimbolo(self, simbolo):
		self.simboloT = simbolo

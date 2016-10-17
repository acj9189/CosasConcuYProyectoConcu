
from Estado import *


class Transicion(object):

	def __init__(self):
		self.estadoOrigen = None
		self.estadoDestino = None
		self.simboloT = None


	""""def __init__(self, estadoOrigen, estadoDestino,simboloT):
		self.estadoOrigen = estadoOrigen
		self.estadoDestino = estadoDestino
		self.simboloT = simboloT"""

	def crearTransicion(self, estadoOrigen, estadoDestino,simboloT):
		self.estadoOrigen = estadoOrigen
		self.estadoDestino = estadoDestino
		self.simboloT = simboloT

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

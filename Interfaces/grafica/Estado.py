
#from Estado import Estado
#from Transicion import Transicion

class Estado(object):

	"""def __init__(self):
		self.estadoNombre = ""
		self.listaTransiciones = []
		self.posX = 0
		self.PosY = 0
		self.esEstadoInicial = False
		self.esEstadoAceptador = False"""



	def __init__(self, estadoNombre, listaTransiciones, posX, posY, esEstadoInicial, esEstadoAceptador):
		self.estadoNombre = estadoNombre
		self.listaTransiciones = listaTransiciones
		self.posX = posX
		self.posY = posY
		self.esEstadoInicial = esEstadoInicial
		self.esEstadoAceptador = esEstadoAceptador
		self.tam = 30

	def getX(self):
		return self.posX

	def getY(self):
		return self.posY

	def getestadoNombre(self):
		return self.estadoNombre

	def setesEstadoInicial(self, estado):
		self.esEstadoInicial = estado

	def setesEstadoAceptador(self, estado):
		self.esEstadoAceptador = estado

	def contains(self, x, y):
		return self.posX - self.tam <= x and self.posX + self.tam >= x and self.posY - self.tam <= y and self.posY + self.tam >= y

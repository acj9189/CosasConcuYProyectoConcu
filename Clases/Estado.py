
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
		self.PosY = posY
		self.esEstadoInicial = esEstadoInicial
		self.esEstadoAceptador = esEstadoAceptador
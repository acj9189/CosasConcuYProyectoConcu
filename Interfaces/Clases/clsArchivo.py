import pickle
from Automata import *
from Estado import *

class Archivo(object):

	def __init__(self, automata):
		self.automata = automata
		self.archivo = None

	def guardarArchivo(self, ruta, nombreArchivo):
		self.archivo = open(ruta + nombreArchivo, "w")


import pickle
from Automata import *
from Estado import *

class Archivo(object):

	def __init__(self):

		self.automata = None
		self.archivo = None

	def guardarArchivoRutaNombre(self, ruta, nombreArchivo,  automata):

		self.automata = automata
		self.archivo = open(ruta + nombreArchivo, "w")
		pickle.dump(self.automata, self.archivo)
		self.archivo.close()

	def cargarArchivoRutaNombre(self, ruta, nombreArchivo):

		self.automata = None
		self.archivo = open(ruta + nombreArchivo, "r")
		self.automata = pickle.load(self.archivo)
		self.archivo.close()
		return self.automata

	def guardarArchivo(self, ruta,  automata):

		self.automata = automata
		self.archivo = open(ruta, "w")
		pickle.dump(self.automata, self.archivo)
		self.archivo.close()

	def cargarArchivo(self, ruta):

		self.automata = None
		self.archivo = open(ruta, "r")
		self.automata = pickle.load(self.archivo)
		self.archivo.close()
		return self.automata



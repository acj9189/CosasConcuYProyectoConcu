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

	# Desde Aca tengo que revisar que funione correctmante.... todos y cada uno de los metodos que hay de aqui para abajo....
	def encontrarInicial(self):
		estadoInicialEn = None
		self.tieneEstadoInicial = False
		for esini in self.listaEstados:
			if(esini.esEstadoInicial == True):
				estadoInicialEn = esini
				self.tieneEstadoInicial = True
				break
		return estadoInicialEn

	def encontrarFinal(self):

		if((self.tipodeAutomata == "PILA") or (self.tipodeAutomata == "AFD-AFN")):
			ListaFinalesEn = []
			self.tieneEstadoFinal = False
			for esfini in self.listaEstados:
				if(esfini.esEstadoAceptador == True):
					ListaFinalesEn.append(esfini)
					self.tieneEstadoFinal = True
			return ListaFinalesEn

	# Modificar para realizar metodos de Hilos
	def realizarReversa(self):
		self.esDeterminista = False
		self.crearEstadoSiExisteMasdeUnAcept()
		self.cambiarDireccionTran()
		# Organizar para crera una posiocion

	def crearEstadoSiExisteMasdeUnAcept(self):
		ListaFinalesRe = encontrarFinal
		numEstadosFini = len(ListaFinalesRe)
		if(numEstadosFini > 1):
			listaTransiciones = []
			tempEs = Estado("fi", listaTransiciones, 0, 0,False,True)
			for es in self.listaEstados:
				if(es.esEstadoAceptador == True):
					es.esEstadoAceptador = False
					tempTran = Transicion(es, tempEs, "-")
					es.listaTransiciones.append(tempTran)
			self.listaEstados.append(tempEs)

	def cambiarDireccionTran(self):
		tempEs = self.encontrarInicial()
		listaEstadosTemp = []
		for es in self.listaEstados:
			listaEstadosTemp.append(es)
			#if(es.listaTransiciones != None):
			for tran in es.listaTransiciones:
				if((tran.estadoDestino in listaEstadosTemp) == False):
					tranTemp1 = Transicion()
					tranTemp2 = tran
					estadoT = tran.estadoDestino
					tranTemp1.estadoOrigen = estadoT
					tranTemp1.estadoDestino = tran.estadoOrigen
					tranTemp1.simboloT = tran.simboloT
					es.listaTransiciones.remove(tranTemp2)
					estadoT.listaTransiciones.append(tranTemp1)

			if(es.esEstadoInicial == True):
				es.esEstadoInicial = False
				es.esEstadoAceptador = True

			if(es.esEstadoAceptador == True):
				es.esEstadoInicial = True
				es.esEstadoAceptador = False

	# Modificar para realizar metodos de Hilos
	def realizarComplemento(self):
		for es in self.listaEstados:
			if(es.esEstadoAceptador == True):
				es.esEstadoAceptador = False
			else:
				es.esEstadoAceptador = True


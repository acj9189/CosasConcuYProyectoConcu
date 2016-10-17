from Estado import *
from Transicion import *

class Automata(object):

	def __init__(self):
		self.listaEstados = []
		self.esDeterminista = True
		self.tieneEstadoInicial = False
		self.tieneEstadoFinal = False
		self.tipodeAutomata = "AFD-AFN"
		self.tam = 20
		print(self.tipodeAutomata)

	def crearEstado(self, estadoNombre, posX, posY, esEstadoInicial, esEstadoAceptador):

		if(self.tipodeAutomata == "AFD-AFN"):
			#print(self.tipodeAutomata)
			#self.listaEstados.append("hola")
			#print(self.listaEstados[0])
			listaTransiciones = []
			self.listaEstados.append(Estado(estadoNombre, listaTransiciones, posX, posY, esEstadoInicial, esEstadoAceptador))
			#print("Cree estado... Automata y no clsAutomata")
			#self.listaEstados.append(Estado(estadoNombre, [], posX, posY, esEstadoInicial, esEstadoAceptador))

		elif(self.tipodeAutomata == "MME"):
			pass
		elif(self.tipodeAutomata == "MMO"):
			pass
		elif(self.tipodeAutomata == "PILA"):
			pass

	def crearTransicion(self, estadoOrigen, estadoDestino, simbolo):
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

	def buscarEstado(self, x, y):
		for es in self.listaEstados:
			if(es.contains(x, y)):
				print(es.contains(x,y))
				return es
		return None

	def settieneEstadoInicial(self, estado):
		self.tieneEstadoInicial = estado

	def settieneEstadoFinal(self, estado):
		self.tieneEstadoFinal = estado

	def leerCadena(self, cadena):

		if(self.esDeterminista == True):
			self.leerCadenaDet(cadena)
		else:
			self.leerCadenaNODet(cadena)

	def leerCadenaDet(self,cadena):
		pila = []
		EstadoT = self.encontrarInicial()
		#print(len(cadena))
		for caracter in cadena:
			#print(a)
			for t in EstadoT.self.listaTransiciones:
				f = caracter
				if(t.getSimbolo() == f):
					pila.append(t.getestadoDestino())
					EstadoT = t.getestadoDestino()
					break

		tam = len(pila)
		estadoA = pila[tam-1]
		if(estadoA.getesEstadoAceptador() == True):
			return "La cadena fue aceptada"
		else:
			return "La cadena no fue aceptada"

	def leerCadenaNODet(self, cadena):
		pass

	def realizarCierredeClene(self):
		self.esDeterminista = False
		self.crearEstadoSiExisteMasdeUnAcept()
		tam = len(listaEstados)
		EstadoT1 = Estado(tam + 1, None, 0, 0, True, False)
		EstadoT2 = Estado(tam + 2, None, 0, 0, False, False)
		EstadoT3 = Estado(tam + 3, None, 0, 0, False, False)
		EstadoT4 = Estado(tam + 4, None, 0, 0, False, True)

		ListaT1 =[]
		ListaT2 =[]
		ListaT3 =[]

		ListaT1.append(Transicion(EstadoT1, EstadoT2, "-"))
		ListaT1.append(Transicion(EstadoT1, EstadoT4, "-"))
		ListaT2.append(Transicion(EstadoT2, self.encontrarInicial(), "-"))

		EstadoT1.setListaTransiciones(ListaT1)
		EstadoT2.setListaTransiciones(ListaT2)

		EstadoIni = self.encontrarInicial()
		EstadoIni.setesEstadoInicial(False)
		ListaT3.append(Transicion(EstadoT3, EstadoT4, "-"))
		ListaT3.append(Transicion(EstadoT3, EstadoT2, "-"))

		EstadoT3.setListaTransiciones(ListaT3)

		listafi = self.encontrarFinal()
		estadofi = listafi[0]
		estadofi.getlistaTransiciones().append(Transicion(estadofi, EstadoT3, "-"))
		estadofi.setesEstadoAceptador(False)

		self.listaEstados.insert(0, EstadoT1)
		self.listaEstados.append(EstadoT2)
		self.listaEstados.append(EstadoT3)
		self.listaEstados.insert(len(self.listaEstados) - 1, EstadoT1)

	def getesDeterminista(self):
		return self.esDeterminista

	def setesDeterminista(self, estado):
		SELF.esDeterminista = estado

	def getListaEstados(self):
		return self.listaEstados

	def setListaEstados(self, lista):
		self.listaEstados = lista

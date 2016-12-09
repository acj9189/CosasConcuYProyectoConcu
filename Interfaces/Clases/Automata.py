from Estado import *
from Transicion import *

class Automata(object):

	def __init__(self):
		self.listaEstados = []
		self.esDeterminista = True
		self.tieneEstadoInicial = False
		self.tieneEstadoFinal = False
		self.tipodeAutomata = None
		self.tam = 20
		#print(self.tipodeAutomata)

	def crearEstado(self, estadoNombre, posX, posY, esEstadoInicial, esEstadoAceptador,simboloMMO):
		print(self.tipodeAutomata)
		if(self.tipodeAutomata == "AFD-AFN"):
			#print(self.tipodeAutomata)
			#self.listaEstados.append("hola")
			#print(self.listaEstados[0])
			listaTransiciones = []
			self.listaEstados.append(Estado(estadoNombre, listaTransiciones, posX, posY, esEstadoInicial, esEstadoAceptador))
			#print("Cree estado... Automata y no clsAutomata")
			#self.listaEstados.append(Estado(estadoNombre, [], posX, posY, esEstadoInicial, esEstadoAceptador))

		elif(self.tipodeAutomata == "MME"):
			listaTransiciones = []
			self.listaEstados.append(Estado(estadoNombre, listaTransiciones, posX, posY, esEstadoInicial, esEstadoAceptador))
		elif(self.tipodeAutomata == "MM0"):
			listaTransiciones = []
			#print("HOLA")
			e = Estado(estadoNombre, listaTransiciones, posX, posY, esEstadoInicial, esEstadoAceptador)
			self.listaEstados.append(e)
			e.setSimboloMMO(simboloMMO)

		elif(self.tipodeAutomata == "PILA"):
			pass

	def crearTransicion(self, estadoOrigen, estadoDestino, simbolo, simboloMME):
		if(self.tipodeAutomata == "AFD-AFN"):
			nuevaTransicion = Transicion()
			nuevaTransicion.crearTransicion(estadoOrigen, estadoDestino,simbolo)
			estadoOrigen.listaTransiciones.append(nuevaTransicion)
			print("se creo")
		elif(self.tipodeAutomata == "MME"):
			nuevaTransicion = Transicion()
			nuevaTransicion.crearTransicionMME(estadoOrigen, estadoDestino, simbolo, simboloMME)
			estadoOrigen.listaTransiciones.append(nuevaTransicion)
		elif(self.tipodeAutomata == "MMO"):
			nuevaTransicion = Transicion()
			nuevaTransicion.crearTransicion(estadoOrigen, estadoDestino,simbolo)
			estadoOrigen.listaTransiciones.append(nuevaTransicion)
			print("se creo")
		elif(self.tipodeAutomata == "PILA"):
			nuevaTransicion = Transicion()
			nuevaTransicion.crearTransicionPILA(estadoOrigen, estadoDestino, simbolo, simboloMME)
			estadoOrigen.listaTransiciones.append(nuevaTransicion)

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
		ListaFinalesRe = self.encontrarFinal()
		numEstadosFini = len(ListaFinalesRe)
		if(numEstadosFini > 1):
			#listaTransiciones = []
			tempEs = Estado("q" + len(self.listaEstados), [], 0, 0,False,True)
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

			if((es.esEstadoAceptador == True) and ( es != tempEs)):
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
			print("Determinista")
			return self.leerCadenaDet(cadena)
		else:
			print("No Determinista")
			return self.leerCadenaNODet(cadena)

	def leerCadenaDet(self,cadena):
		pila = []
		EstadoT = self.encontrarInicial()
		#print(len(cadena))
		for caracter in cadena:
			print(caracter)
			#print(a)
			for t in EstadoT.getlistaTransiciones():
				f = caracter
				#print(f)
				#print(t.getSimbolo(),f)
				if(t.getSimbolo() == f):
					pila.append(t.getestadoDestino())
					EstadoT = t.getestadoDestino()
					break

		tam = len(pila)
		#print(tam)
		estadoA = pila[tam-1]

		if(estadoA.getesEstadoAceptador() == True):
			print(estadoA)
			print("La cadena fue aceptada")
			return "La cadena fue aceptada"
		else:
			return "La cadena no fue aceptada"

	def leerCadenaNODet(self, cadena):
		pass

	def verificarsiDeterminista(self, simbolo):
		 self.setesDeterminista(True)
		 ListaF = []
		 for es in self.listaEstados:
		 	i = 0
		 	for tran in es.listaTransiciones:
		 		if((tran.getSimbolo() == simbolo) or ((simbolo == "-") and (tran.getSimbolo() == simbolo))):
		 			i = i + 1
		 	ListaF.append(i)

		 	for a in ListaF:
		 		if(a > 1):
		 			self.setesDeterminista(False)
		 			break


	def realizarCierredeKleen(self):
		self.esDeterminista = False
		self.crearEstadoSiExisteMasdeUnAcept()
		tam = len(self.listaEstados)
		EstadoT1 = Estado("q" + str(tam + 1), [], 50, 50, True, False)
		EstadoT2 = Estado("q" + str(tam + 2), [], 50, 50, False, False)
		EstadoT3 = Estado("q" + str(tam + 3), [], 50, 50, False, False)
		EstadoT4 = Estado("q" + str(tam + 4), [], 50, 50, False, True)

		ListaT1 =[]
		ListaT2 =[]
		ListaT3 =[]

		T1 = Transicion()
		T1.crearTransicion(EstadoT1, EstadoT2, "-")
		T2 = Transicion()
		T2.crearTransicion(EstadoT1, EstadoT4, "-")
		T3 = Transicion()
		T3.crearTransicion(EstadoT2, self.encontrarInicial(), "-")

		ListaT1.append(T1)
		ListaT1.append(T2)
		ListaT2.append(T3)

		EstadoT1.setListaTransiciones(ListaT1)
		EstadoT2.setListaTransiciones(ListaT2)

		EstadoIni = self.encontrarInicial()
		EstadoIni.setesEstadoInicial(False)

		T4 = Transicion()
		T4.crearTransicion(EstadoT3, EstadoT4, "-")
		T5 = Transicion()
		T5.crearTransicion(EstadoT3, EstadoT2, "-")

		ListaT3.append(T4)
		ListaT3.append(T5)

		EstadoT3.setListaTransiciones(ListaT3)

		listafi = self.encontrarFinal()
		estadofi = listafi[0]

		T6 = Transicion()
		T6.crearTransicion(estadofi,EstadoT3, "-")

		estadofi.getlistaTransiciones().append(T6)
		estadofi.setesEstadoAceptador(False)

		self.listaEstados.insert(0, EstadoT1)
		self.listaEstados.append(EstadoT2)
		self.listaEstados.append(EstadoT3)
		self.listaEstados.insert(len(self.listaEstados) - 1, EstadoT4)

	def getesDeterminista(self):
		return self.esDeterminista

	def setesDeterminista(self, estado):
		self.esDeterminista = estado

	def getListaEstados(self):
		return self.listaEstados

	def setListaEstados(self, lista):
		self.listaEstados = lista

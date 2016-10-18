from Estado import *
from Transicion import *
from Automata import *

class Automatas(object):

	def __init__(self):
		self.listaAutomatas = []

	def realizarUnionEntreAutomatasNoDeterminista(self, Auto1 , Auto2):

		AutomataRes = Automata()
		AutomataRes.setesDeterminista(False)
		EstadoT = Estado("qi", [], 50, 50, True, False)
		ListaT =[]


		T1 = Transicion()
		T1.crearTransicion(EstadoT, Auto1.encontrarInicial(), "-")
		T2 = Transicion()
		T2.crearTransicion(EstadoT, Auto2.encontrarInicial(), "-")


		ListaT.append(T1)
		ListaT.append(T2)

		Auto1.encontrarInicial().setesEstadoInicial(False)
		Auto2.encontrarInicial().setesEstadoInicial(False)
		EstadoT.setListaTransiciones(ListaT)
		#EstadoT.setListaTransiciones(ListaT)
		#Lista = AutomataRes.getListaEstados()
		#Lista.append()
		AutomataRes.getListaEstados().append(EstadoT)

		for a in Auto1.getListaEstados():
			AutomataRes.getListaEstados().append(a)

		for b in Auto2.getListaEstados():
			AutomataRes.getListaEstados().append(b)

		EstadoTF = Estado("qf", [], 50, 50, False, True)

		for es in AutomataRes.getListaEstados():
			if((es.getesEstadoAceptador() == True) ):

				es.setesEstadoAceptador(False)
				T1 = Transicion()
		        T1.crearTransicion(es, EstadoTF, "-")

		        es.listaTransiciones.append(T1)


		AutomataRes.getListaEstados().append(EstadoTF)
		return AutomataRes

	def realizarConcatenacionEntreAutomatas(self, Auto1, Auto2):

		AutomataRes = Automata()
		AutomataRes.setesDeterminista(False)
		EstadoT1 = Estado("qi", [], 50, 50, True, False)
		EstadoT2 = Estado("qin", [], 50, 50, False, False)
		EstadoT3 = Estado("qf", [], 50, 50, False, True)

		ListaT =[]

		T1 = Transicion()
		T1.crearTransicion(EstadoT1, Auto1.encontrarInicial(), "-")
		ListaT.append(T1)
		EstadoT1.setListaTransiciones(ListaT)
		Auto1.encontrarInicial().setesEstadoInicial(False)
		AutomataRes.getListaEstados().append(EstadoT1)

		for a in Auto1.getListaEstados():
			AutomataRes.getListaEstados().append(a)



		#AutomataRes.crearEstadoSiExisteMasdeUnAcept()
		#tam = AutomataRes.getListaEstados

		AutoFin = self.encontrarFinal(AutomataRes)
		T2 = Transicion()
		T2.crearTransicion(AutoFin, EstadoT2, "-")
		#AutoFin = AutomataRes.getListaEstados[tam -1]#.getlistaTransiciones().append()
		AutoFin.getlistaTransiciones().append(T2)

		T3 = Transicion()
		T3.crearTransicion(EstadoT2, Auto2.encontrarInicial(), "-")
		EstadoT2.getlistaTransiciones().append(T3)
		AutomataRes.getListaEstados.append(EstadoT2)

		AutoFin2 = encontrarFinal(AutomataRes)
		AutoFin2.setesEstadoAceptador(False)

		T4 = Transicion()
		T4.crearTransicion(Auto2.encontrarInicial(), EstadoT3, "-")

		AutoFin3 = encontrarFinal(Auto2)
		AutoFin3.getlistaTransiciones.append(T4)
		AutoFin3.setesEstadoAceptador(False)

		for b in Auto2.getListaEstados():
			AutomataRes.getListaEstados().append(b)

		AutomataRes.append(EstadoT3)
		return AutomataRes

	def encontrarFinal(self, Auto):
		tam = len(Auto.getListaEstados())
		if(tam > 1):
			Auto1.crearEstadoSiExisteMasdeUnAcept()

		for e in Auto.getListaEstados:
			if(e.getesEstadoAceptador() == True):
				return e

	def realizarInterseccionEntreAutomatas(self, Auto1, Auto2):
		pass
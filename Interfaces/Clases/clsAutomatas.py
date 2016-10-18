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

	def realizarConcatenacionEntreAutomatas(self):
		pass
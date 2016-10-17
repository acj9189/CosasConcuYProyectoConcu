from Estado import *
from Transicion import *
from Automata import *

class Automatas(object):

	def __init__(self):
		self.listaAutomatas = []

	def realizarUnionEntreAutomatasNoDeterminista(self, Auto1 , Auto2):

		AutomataRes = Automata()
		AutomataRes.setesDeterminista(False)
		EstadoT = Estado("qi", [], 0, 0, True, False)
		ListaT =[]
		ListaT.append(Transicion(EstadoT, Auto1.encontrarInicial(), "-"))
		ListaT.append(Transicion(EstadoT, Auto2.encontrarInicial(), "-"))

		Auto1.encontrarInicial().setesEstadoInicial(False)
		Auto2.encontrarInicial().setesEstadoInicial(False)
		EstadoT.setListaTransiciones(ListaT)
		#Lista = AutomataRes.getListaEstados()
		#Lista.append()
		AutomataRes.getListaEstados().append(EstadoT)

		#for a in Auto.getListaEstados(), Auto2.getListaEstados():



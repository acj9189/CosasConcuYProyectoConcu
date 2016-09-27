
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class ventana(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("CrearAuto.ui",self)


app = QApplication(sys.argv)
_ventana = ventana()
_ventana.show()
app.exec_()


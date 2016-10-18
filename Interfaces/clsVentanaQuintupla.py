from Tkinter import*
import tkSimpleDialog
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
from ttk import *

from Clases.Automata import *
from Clases.Estado import *
from Clases.clsArchivo import*
import clsVentana


class Ventana(object):

    def __init__(self):
        self.automata = Automata()
        self.archivo = None
        self.inicialseleccionado = None
        self.posX = 0
        self.posY = 0
        self.ventanaQuintupla = Tk()
        self.frame = Frame(self.ventanaQuintupla)
        self.canvas = Canvas(self.frame, bd=6, bg='white', width=300, height=300)
        self.ventanaQuintupla.title("Modo Quintupla")
        self.ventanaQuintupla.geometry("400x400+0+0")
        self.canvas.place(x=0, y=0)
        self.frame.grid(column=0, row=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        Button(self.ventanaQuintupla, text='colocar')
        self.ventanaQuintupla.mainloop()


    def retornarAutomata(self):
        return self.automata

    def crearEstado(self):
        self.automata.crearEstado(self)

if __name__ == '__main__':
    H = Ventana()
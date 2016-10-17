from Tkinter import*
import tkSimpleDialog
import Tkinter, Tkconstants, tkFileDialog
from ttk import *
from Clases.clsAutomata import *
from Clases.clsEstado import *

from Clases.Automata import *
from Clases.Estado import *
from Clases.clsArchivo import*
from clsVentanaQuintupla import *


class Ventana(object):

    def __init__(self):
        #self.automata = clsAutomata(['0', '1'])
        self.automata = Automata()
        
        self.archivo = None
        self.inicialseleccionado = None
        self.posX = 0
        self.posY = 0
        #self.op = ''
        self.ventanaPrincipal = Tk()
        self.frame = Frame(self.ventanaPrincipal)
        self.canvas = Canvas(self.frame, bd=6, bg='white', width=1200, height=800)
        self.ventanaPrincipal.title("Realizar Automata")
        self.ventanaPrincipal.geometry("1140x700+0+0")
        self.canvas.place(x=0, y=0)
        self.frame.grid(column=0, row=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.txtCadena = StringVar()
        self.modoOperacion = 0
        Button(self.frame, text='Colocar Estado', command=lambda: self.crearEstado()).grid(column=5, row=1)
        #Button(self.frame, text='Minimizar Automata', command=lambda: self.minimizar()).grid(column=2, row=1)
        #Button(self.frame, text='Guardar Automata', command=lambda: self.guardarArchivo()).grid(column=3, row=1)
        #Button(self.frame, text='Cargar Automata', command=lambda: self.cargarArchivo()).grid(column=3, row=1)
        #Button(self.frame, text='Leer Cadena', command=lambda: self.verificarCadena()).grid(column=4, row=1)
        #Button(self.frame, text='Quintupla', command=lambda: self.minimizar()).grid(column=2, row=1)
        #Button(self.frame, text='Cargar Automata', command=lambda: self.minimizar()).grid(column=4, row=1)
        #Button(self.frame, text='Determinista', command=lambda: self.pasarADeterminista()).grid(column=5, row=1)
        OptionMenu(self.frame, self.txtCadena, 'Funciones Automata', 'Minimizar Automata', 'Union', 'Complemento', 'Reverso', 'Concatenacion', 'Cierre de Kleene').grid(column=3, row =1)
        OptionMenu(self.frame, self.txtCadena, 'Archivo',  'Guardar Automata', 'Cargar Automata').grid(column=1, row =1)
        Button(self.frame, text='Realizar Quintupla', command=lambda : self.pasarAQuintupla()).grid(column=4, row=1)
        Entry(self.frame, textvariable=self.txtCadena).grid(column=1, row=51, sticky=(W, E))
        #Button(self.frame, text='Verificar', command=lambda: self.verificarCadena()).grid(column=2, row=51, sticky=(W, E))
        Label(self.frame, text='Zoom').grid(column=3, row=51)
        self.canvas.grid(column=1, row=2, columnspan=50, rowspan=50, sticky=E + W)
        self.canvas.bind('<Button-1>', self.onClickCanvas)
        self.canvas.bind('<Double-1>', self.doubleClickCanvas)
        self.canvas.bind('<Button-3>', self.mostrarMenu)
        self.canvas.bind('<Motion>', self.moviendo)
        self.canvas.bind('<B1-Motion>', self.moverEstado)
        self.ventanaPrincipal.mainloop()

    def pasarAQuintupla(self):
        ventanita = Tk()

        ventanita.mainloop()


    def onClickCanvas(self, event):
        if self.modoOperacion == 1:
            #estado = clsEstado(event.x, event.y, 'q' + str(len(self.automata.diccionarioEstados.keys())))
            #self.automata.nuevoEstado(estado)
            self.automata.crearEstado('q' + str(len(self.automata.listaEstados)), event.x, event.y, False, False)

        elif self.modoOperacion == 2:
            finalseleccionado = self.automata.buscarEstado(event.x, event.y)

            if finalseleccionado is not None:
                #var = tkMessageBox.askyesno("Title", "Your question goes here?")
                simbolo = tkSimpleDialog.askstring("Ingresar","Ingrece el simbolo de la transicion")
                print(simbolo)
                self.crearTransicion(self.inicialseleccionado, finalseleccionado, simbolo)

        self.modoOperacion = 0
        self.actualizarScreen()

    def doubleClickCanvas(self, event):

        if self.automata.buscarEstado(event.x, event.y) is None:
            self.modoOperacion = 0
            return
        self.modoOperacion = 2
        self.inicialseleccionado = self.automata.buscarEstado(event.x, event.y)
        self.actualizarScreen()

    def crearEstado(self):
        self.modoOperacion = 1

    def crearTransicion(self, origen, destino, simbolo):
        self.automata.crearTransicion(origen, destino, simbolo)
        self.actualizarScreen()

    def mostrarMenu(self, event):
        estado = self.automata.buscarEstado(event.x, event.y)
        if estado is not None:
            self.menuEstado = Menu(self.ventanaPrincipal, tearoff=0)
            label = ''
            if estado.esEstadoAceptador == True:
                label = 'No Aceptador'
            else:
                label = 'Aceptador'
            self.menuEstado.add_command(label=label, command=lambda: self.cambiarAceptador(estado))
            label = ''

            # Tengo que corregir qwu no deje pintar mas inicla si ya existe uno...
            if estado.esEstadoInicial == True:
                label = 'No Inicial'
            else:
                label = 'Inicial'
            self.menuEstado.add_command(label=label, command=lambda: self.cambiarInicial(estado))
            #self.menuEstado.add_separator()
            #self.menuEstado.add_command(label='Cancelar', command=lambda: self.cancelar())
            try:
                self.menuEstado.tk_popup(event.x_root + 20, event.y_root + 20, 0)
            finally:
                self.menuEstado.grab_release()

    def guardarArchivo(self):
        #nombreArchivo = tkSimpleDialog.askstring("Ingresar","Ingrece el nombre del archivo que desea almacenar")
        #nombreArchivo = nombreArchivo + ".acj"
        #file_path_string = tkFileDialog.asksaveasfile(mode='w',defaultextension=".acj")
        file_path_string = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("acj files","*.acj"),("all files","*.*")), defaultextension=".acj")
        #print(file_path_string, nombreArchivo)
        print(file_path_string)
        self.archivo = Archivo()
        self.archivo.guardarArchivo(file_path_string, self.automata)
        #self.automata.exportarJSON()

    def cargarArchivo(self):

        file_path_string = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("acj files","*.acj"),("all files","*.*")), defaultextension=".acj")
        print(file_path_string)
        self.archivo = Archivo()
        self.automata = self.archivo.cargarArchivo(file_path_string)
        self.actualizarScreen()

    def cambiarAceptador(self, estado):
        if(estado.esEstadoAceptador == True):
            estado.setesEstadoAceptador(False)
            self.automata.settieneEstadoFinal(False)
        else:
            estado.setesEstadoAceptador(True)
            self.automata.settieneEstadoFinal(True)
        self.actualizarScreen()

    def cambiarInicial(self, estado):
        if (estado.esEstadoInicial == True):
            estado.setesEstadoInicial(False)
            self.automata.settieneEstadoInicial(False)
        else:
            estado.setesEstadoInicial(True)
            self.automata.settieneEstadoInicial(True)
        self.actualizarScreen()

    def moviendo(self, event):
        self.posX, self.posY = event.x, event.y
        if self.modoOperacion == 2:
            self.actualizarScreen()

    def cancelar(self):
        pass

    def moverEstado(self, event):
        sel = self.automata.buscarEstado(event.x, event.y)
        if sel is None:
            return
        sel.x, sel.y = event.x, event.y
        self.actualizarScreen()

    def minimizar(self):
        self.automata = self.automata.minimizar()
        self.actualizarScreen()

    def pasarADeterminista(self):
        self.automata = self.automata.convertirADeterminista()
        self.actualizarScreen()

    def verificarCadena(self):
        cadena = tkSimpleDialog.askstring("Cadenas","Ingrece la cadena que quiere analizar")
        self.automata.leerCadena(cadena)



    def actualizarScreen(self):
        self.canvas.delete('all');
        tam = self.automata.tam

        if self.modoOperacion == 2:
            self.canvas.create_line(self.inicialseleccionado.getX(), self.inicialseleccionado.getY(), self.posX, self.posY)
        for a in self.automata.listaEstados:

            # pintar transiciones

            for d in a.listaTransiciones:
                if(d.getestadoOrigen() == d.getestadoDestino()):
                     # lazo
                        self.canvas.create_text(d.getestadoOrigen().getX(), d.getestadoOrigen().getY() - 70, text = d.getSimbolo())
                        self.canvas.create_line(a.getX() + tam, a.getY() + tam / 4, d.getestadoOrigen().getX(), d.getestadoOrigen().getY() - (tam * 5),
                                                d.getestadoOrigen().getX() - tam, d.getestadoOrigen().getY() - tam / 2, arrow=LAST, smooth=True)
                else:
                    # Destino mayor que origen
                    if (d.getestadoDestino().getX() > a.getX()):
                         print("entro origen mayor que destino")
                         if (a.getY() <= d.getestadoDestino().getY()):
                             pm = (d.getestadoDestino().getX() - (d.getestadoDestino().getX() - a.getX()) / 2, a.getY())
                             pt = (pm[0] + 30, pm[1] + 30)
                         else:
                             pm = (d.getestadoDestino().getX() - (d.getestadoDestino().getX() - a.getX()) / 2,d.getestadoDestino().getY())
                             pt = (pm[0] + 30, pm[1] - 30)
                         self.canvas.create_text(pt, text = d.getSimbolo())
                         self.canvas.create_line(a.getX(), a.getY(), pm, d.getestadoDestino().getX(), d.getestadoDestino().getY() - tam, arrow=LAST,
                                                    smooth=True)
                    else:
                        # Origen mayor que Destino
                         if (a.getY() <= d.getestadoDestino().getY()):
                             print("entro origen menor o igual q destino")
                             pm = (d.getestadoDestino().getX() - (d.getestadoDestino().getX() - a.getX()) / 2, d.getestadoDestino().getY())
                             pt = (pm[0] + 10, pm[1] + 50)
                         else:
                             pm = (d.getestadoDestino().getX() - (d.getestadoDestino().getX() - a.getX()) / 2, a.getY())
                             pt = (pm[0] + 10, pm[1] - 50)
                         self.canvas.create_text(pt, text = d.getSimbolo())
                         self.canvas.create_line(a.getX(), a.getY(), pm, d.getestadoDestino().getX(), d.getestadoDestino().getY() + tam, arrow=LAST,
                                                    smooth=True)

            # pintar estados """

            self.canvas.create_oval(a.getX() - tam, a.getY() - tam, a.getX() + tam, a.getY() + tam, fill='red',
                                    activeoutline='blue', outline='white', width=2)
            if a.esEstadoAceptador == True:
                self.canvas.create_oval(a.getX() - 12, a.getY() - 12, a.getX() + 12, a.getY() + 12)

            if a.esEstadoInicial == True:
                self.canvas.create_line(a.getX() - tam * 2, a.getY(), a.getX() - tam, a.getY(), arrow=LAST)
            self.canvas.create_text(a.getX(), a.getY(), fill = 'white', text = a.getestadoNombre())


if __name__ == '__main__':
    V = Ventana()
    #V.verificarCadena()
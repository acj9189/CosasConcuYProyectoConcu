import tkMessageBox
from Tkinter import*
import tkSimpleDialog
import Tkinter, Tkconstants, tkFileDialog
import tkSimpleDialog
import Tkinter, Tkconstants, tkFileDialog
from ttk import *
from Clases.clsAutomata import *
from Clases.clsEstado import *
from Clases.Automata import *
from Clases.Estado import *
from Clases.clsArchivo import*
import clsVentanaQuintupla
from Clases.clsAutomatas import *
from Tkinter import *
from ttk import *



class Ventana(object):

    def __init__(self):
        self.automata = Automata()
        self.archivo = None
        self.inicialseleccionado = None
        self.posX = 0
        self.posY = 0
        self.ventanaPrincipal = Tk()
        self.frame = Frame(self.ventanaPrincipal)
        self.canvas = Canvas(self.frame, bd=6, bg='white', width=1200, height=800)
        self.ventanaPrincipal.title("Realizar Automata")
        self.ventanaPrincipal.geometry("1140x700+0+0")
        self.canvas.place(x=0, y=0)
        self.frame.grid(column=0, row=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        #self.txtCadena = StringVar()
        self.canvas2 = Canvas(self.frame, bg = 'gray', width=350, height=250)
        self.canvas2.place(x=850, y=0)


        #Agregamos un menu
        self.menu = Menu(self.ventanaPrincipal)
        self.ventanaPrincipal.config(menu=self.menu)
        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label='Archivo', menu=self.subMenu)
        self.subMenu.add_command(label='Modo Quintupla', command=lambda: self.pasarAQuintupla())
        self.subMenu.add_command(label='Modo Tabla', command=lambda: self.pasarAQuintupla())
        self.subMenu.add_command(label='Cargar Archivo', command=lambda: self.cargarArchivo())
        self.subMenu.add_command(label='Guardar Archivo', command=lambda: self.guardarArchivo())
        self.subMenu.add_separator()
        self.subMenu.add_command(label='Salir', command=lambda: self.ventanaPrincipal.quit())

        #Agregamos un menu para las funciones
        self.menuFunciones = Menu(self.menu)
        self.menu.add_cascade(label="Funciones", menu= self.menuFunciones)
        #self.menuFunciones.add_command(label='Minimizacion', command=lambda: self.minimizar())
        self.menuFunciones.add_command(label='Complemento', command=lambda: self.complemento())
        self.menuFunciones.add_command(label='Union', command=lambda: self.union())
        self.menuFunciones.add_command(label='Interseccion', command=lambda: self.interseccion())
        self.menuFunciones.add_command(label='Reverso', command=lambda: self.reverso())
        self.menuFunciones.add_command(label='Concatenacion', command=lambda: self.concatenacion())
        self.menuFunciones.add_command(label='Cierre de Kleen', command=lambda: self.cierreKleen())
        self.menuFunciones.add_command(label='Pasar a Determinista', command=lambda: self.pasarADeterminista())
        self.menuFunciones.add_command(label='Crear a partir de Expresion Regular', command=lambda: self.nada())
        self.menuFunciones.add_command(label='Crear a partir de Automata', command=lambda: self.nada())

        #Agregamos un modo de operacion para los eventos
        self.modoOperacion = 0
        Button(self.frame, text='Colocar Estado', command=lambda: self.crearEstado()).grid(column=10, row=1)
        Button(self.frame, text='Pruebas', command=lambda: self.verificarCadena()).grid(column=14, row=1)
        Button(self.frame, text='Borrar Todo', command=lambda : self.clearCanvas()).grid(column=13, row=1)
        #Entry(self.frame, textvariable=self.txtCadena).grid(column=1, row=51, sticky=(W, E))
        Label(self.frame, text='Zoom').grid(column=3, row=51)
        self.canvas.grid(column=1, row=2, columnspan=50, rowspan=50, sticky=E + W)
        self.canvas.bind('<Button-1>', self.onClickCanvas)
        self.canvas.bind('<Double-1>', self.doubleClickCanvas)
        self.canvas.bind('<Button-3>', self.mostrarMenu)
        self.canvas.bind('<Motion>', self.moviendo)
        self.canvas.bind('<B1-Motion>', self.moverEstado)
        self.ventanaPrincipal.mainloop()



    def pasarAQuintupla(self):
        self.aceptadores = []
        self.iniciales = []
        self.estados = []
        self.lista = StringVar()
        for es in self.automata.listaEstados:
            if (es.esEstadoAceptador == True):
                self.aceptadores.append(es.getestadoNombre())
            self.estados.append(es.getestadoNombre())
        for ini in self.automata.listaEstados:
            if (ini.esEstadoInicial == True):
                self.iniciales.append(ini.getestadoNombre())

        '''for esini in self.automata.listaEstados:
            if (esini.esEstadoInicial == True):
                self.iniciales.append(esini.getEstadoNombre())'''



                

        #self.canvas2.create_text(20, 30, anchor=W, font="Purisa", text="Aceptadores:")
        self.canvas2.create_text(20, 60, anchor=W, font="Purisa",
                                 text= 'F: ' + str(self.aceptadores) + '  (Aceptadores)')

        self.canvas2.create_text(20, 30, anchor=W, font="Purisa",
                                 text='Q: ' + str(self.estados) + '  (Estados)')

        self.canvas2.create_text(20, 90, anchor=W, font="Purisa",
                                 text='S: ' + str(self.iniciales) + '  (Inicial)')


    def clearCanvas(self):
        self.canvas.delete("all")
        self.automata.listaEstados = []

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
                #print(simbolo)
                if(simbolo == "-"):
                    self.automata.setesDeterminista(False)

                self.crearTransicion(self.inicialseleccionado, finalseleccionado, simbolo)

                i = 1
                for e in self.inicialseleccionado.getlistaTransiciones():
                    if(e.getSimbolo() == simbolo):
                        i = i + 1

                if(i > 1):
                    self.automata.setesDeterminista(False)

                #self.crearTransicion(self.inicialseleccionado, finalseleccionado, simbolo)

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
        #print(sel)
        if sel is None:
            return
        sel.setX(event.x)
        sel.setY(event.y)
        #sel.x, sel.y = event.x, event.y
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

    def verificarCadena(self):
        cadena = tkSimpleDialog.askstring("Cadenas","Ingrece la cadena que quiere analizar")
        print(self.automata.leerCadena(cadena))

    def complemento(self):
        self.automata.realizarComplemento()
        self.actualizarScreen()

    def reverso(self):
        self.automata.realizarReversa()
        self.actualizarScreen()

    def cierreKleen(self):
        self.automata.realizarCierredeKleen()
        self.actualizarScreen()

    def union(self):
        numes = len(self.automata.getListaEstados())
        if(numes > 0):
            Auto1 = self.automata
            Auto2 = self.cargaMasUnautomata()
            AutomatasPP = Automatas()
            self.automata = AutomatasPP.realizarUnionEntreAutomatasNoDeterminista(Auto1, Auto2)
        else:
            result = tkMessageBox.askquestion("Union", "Desea Cargar los dos Automatas o prefiere realizar uno", icon='warning')
            if result == 'yes':
                Auto1 = self.cargaMasUnautomata()
                Auto2 = self.cargaMasUnautomata()
                AutomatasPP = Automatas()
                self.automata = AutomatasPP.realizarUnionEntreAutomatasNoDeterminista(Auto1, Auto2)

        self.actualizarScreen()

    def cargaMasUnautomata(self):

        file_path_string = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("acj files","*.acj"),("all files","*.*")), defaultextension=".acj")
        #print(file_path_string)
        self.archivo = Archivo()
        return self.archivo.cargarArchivo(file_path_string)

    def concatenacion(self):
        numes = len(self.automata.getListaEstados())
        if(numes > 0):
            Auto1 = self.automata
            Auto2 = self.cargaMasUnautomata()
            AutomatasPP = Automatas()
            self.automata = AutomatasPP.realizarConcatenacionEntreAutomatas(Auto1, Auto2)
        else:
            result = tkMessageBox.askquestion("Union", "Desea Cargar los dos Automatas o prefiere realizar uno", icon='warning')
            if result == 'yes':
                Auto1 = self.cargaMasUnautomata()
                Auto2 = self.cargaMasUnautomata()
                AutomatasPP = Automatas()
                self.automata = AutomatasPP.realizarConcatenacionEntreAutomatas(Auto1, Auto2)

        self.actualizarScreen()

    def interseccion(self):
        numes = len(self.automata.getListaEstados())
        if(numes > 0):
            Auto1 = self.automata
            Auto2 = self.cargaMasUnautomata()
            AutomatasPP = Automatas()
            self.automata = AutomatasPP.realizarInterseccionEntreAutomatas(Auto1, Auto2)
        else:
            result = tkMessageBox.askquestion("Union", "Desea Cargar los dos Automatas o prefiere realizar uno", icon='warning')
            if result == 'yes':
                Auto1 = self.cargaMasUnautomata()
                Auto2 = self.cargaMasUnautomata()
                AutomatasPP = Automatas()
                self.automata = AutomatasPP.realizarInterseccionEntreAutomatas(Auto1, Auto2)

        self.actualizarScreen()

if __name__ == '__main__':
    V = Ventana()


    #V.verificarCadena()
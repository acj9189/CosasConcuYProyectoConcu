from Tkinter import*
from ttk import *
from clsAutomata import *
from clsEstado import *


class Ventana(object):
    def __init__(self):
        self.automata = clsAutomata(['0', '1'])
        self.seleccionar = None
        self.posX = 0
        self.posY = 0
        #self.op = ''
        self.ventanaPrincipal = Tk()
        self.frame = Frame(self.ventanaPrincipal)
        self.canvas = Canvas(self.frame, bd=6, bg='white', width=1200, height=800)
        self.ventanaPrincipal.title("Prueba Automata")
        self.ventanaPrincipal.geometry("1300x900")
        self.canvas.place(x=0, y=0)
        self.frame.grid(column=0, row=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.txtCadena = StringVar()
        self.modoOperacion = 0
        Button(self.frame, text='Colocar Estado', command=lambda: self.crearEstado()).grid(column=1, row=1)
        Button(self.frame, text='Minimizar Automata', command=lambda: self.minimizar()).grid(column=2, row=1)
        Button(self.frame, text='Guardar Automata', command=lambda: self.guardarJson()).grid(column=3, row=1)
        Button(self.frame, text='Cargar Automata', command=lambda: self.minimizar()).grid(column=4, row=1)
        Button(self.frame, text='Determinista', command=lambda: self.pasarADeterminista()).grid(column=5, row=1)
        Entry(self.frame, textvariable=self.txtCadena).grid(column=1, row=51, sticky=(W, E))
        Button(self.frame, text='Verificar', command=lambda: self.verificarCadena()).grid(column=2, row=51,
                                                                                          sticky=(W, E))
        Label(self.frame, text='Zoom').grid(column=3, row=51)
        self.canvas.grid(column=1, row=2, columnspan=50, rowspan=50, sticky=E + W)
        self.canvas.bind('<Button-1>', self.onClickCanvas)
        self.canvas.bind('<Double-1>', self.doubleClickCanvas)
        self.canvas.bind('<Button-3>', self.mostrarMenu)
        self.canvas.bind('<Motion>', self.moviendo)
        self.canvas.bind('<B1-Motion>', self.moverEstado)
        self.ventanaPrincipal.mainloop()


    def onClickCanvas(self, event):
        if self.modoOperacion == 1:
            estado = clsEstado(event.x, event.y, 'q' + str(len(self.automata.diccionarioEstados.keys())))
            self.automata.nuevoEstado(estado)
        elif self.modoOperacion == 2:
            anterior = self.automata.buscar(event.x, event.y)
            if anterior is not None:
                self.menuTransicion = Menu(self.ventanaPrincipal, tearoff=0)
                for e in self.automata.alfabeto:
                    if e == 'E':
                        continue
                    self.menuTransicion.add_command(label=e,
                                                    command=lambda c=e, ant=anterior, sel=self.seleccionar: self.crearTransicion(sel,
                                                                                                                                 ant,
                                                                                                                                 c))
                self.menuTransicion.add_separator()
                self.menuTransicion.add_command(label='E',
                                                command=lambda c='E', ant=anterior, sel=self.seleccionar: self.crearTransicion(sel,
                                                                                                                               ant,
                                                                                                                               c))
                self.menuTransicion.add_separator
                self.menuTransicion.add_command(label='Cancelar', command=lambda: self.cancelar())
                try:
                    self.menuTransicion.tk_popup(event.x_root + 20, event.y_root + 20, 0)
                    self.menuTransicion.grab_set()
                finally:
                    self.menuTransicion.grab_release()
        else:
            pass
        self.modoOperacion = 0
        self.actualizarScreen()

    def doubleClickCanvas(self, event):

        if self.automata.buscar(event.x, event.y) is None:
            self.modoOperacion = 0
            return
        self.modoOperacion = 2
        self.seleccionar = self.automata.buscar(event.x, event.y)
        self.actualizarScreen()

    def crearEstado(self):
        self.modoOperacion = 1

    def crearTransicion(self, sel, ant, caracter):
        self.automata.diccionarioEstados[sel][caracter].append(ant)
        self.actualizarScreen()

    def mostrarMenu(self, event):
        estado = self.automata.buscar(event.x, event.y)
        if estado is not None:
            self.menuEstado = Menu(self.ventanaPrincipal, tearoff=0)
            label = ''
            if estado.esAceptador():
                label = 'No Aceptador'
            else:
                label = 'Aceptador'
            self.menuEstado.add_command(label=label, command=lambda: self.cambiarAceptador(estado))
            label = ''
            if estado is self.automata.inicial:
                label = 'No Inicial'
            else:
                label = 'Inicial'
            self.menuEstado.add_command(label=label, command=lambda: self.cambiarInicial(estado))
            self.menuEstado.add_separator()
            self.menuEstado.add_command(label='Cancelar', command=lambda: self.cancelar())
            try:
                self.menuEstado.tk_popup(event.x_root + 20, event.y_root + 20, 0)
            finally:
                self.menuEstado.grab_release()

    def guardarJson(self):
        self.automata.exportarJSON()

    def cambiarAceptador(self, estado):
        estado.setAcept(not estado.esAceptador())
        self.actualizarScreen()

    def cambiarInicial(self, estado):
        if self.automata.inicial is estado:
            self.automata.inicial = None
        else:
            self.automata.inicial = estado
        self.actualizarScreen()

    def moviendo(self, event):
        self.posX, self.posY = event.x, event.y
        if self.modoOperacion == 2:
            self.actualizarScreen()

    def cancelar(self):
        pass

    def moverEstado(self, event):
        sel = self.automata.buscar(event.x, event.y)
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

        cadena = self.txtCadena.get()
        actual = self.automata.inicial
        for c in cadena:
            if c not in self.automata.alfabeto:
                print 'El caracter ' + c + ' no esta dentro del alfabeto'
                return
            actual = self.automata.diccionarioEstados[actual][c][0]
        if actual.esAceptador():
            print 'La cadena ' + cadena + ' es aceptada'
        else:
            print 'La cadena ' + cadena + ' no es aceptada'

    def actualizarScreen(self):
        self.canvas.delete('all');
        tam = self.automata.tam
        if self.modoOperacion == 2:
            self.canvas.create_line(self.seleccionar.getX(), self.seleccionar.getY(), self.posX, self.posY)
        for a in self.automata.diccionarioEstados.keys():
            # pintar transiciones
            for c in self.automata.alfabeto:
                for d in self.automata.diccionarioEstados[a][c]:
                    if d is a:
                        # lazo
                        self.canvas.create_text(d.getX(), d.getY() - 70, text=c)
                        self.canvas.create_line(a.getX() + tam, a.getY() + tam / 4, d.getX(), d.getY() - (tam * 5),
                                                d.getX() - tam, d.getY() - tam / 2, arrow=LAST, smooth=True)
                    else:
                        if d.getX() > a.getX():
                            if a.getY() <= d.getY():
                                pm = (d.getX() - (d.getX() - a.getX()) / 2, a.getY())
                                pt = (pm[0] + 30, pm[1] + 50)
                            else:
                                pm = (d.getX() - (d.getX() - a.getX()) / 2, d.getY())
                                pt = (pm[0] + 30, pm[1] - 50)
                            self.canvas.create_text(pt, text=c)
                            self.canvas.create_line(a.getX(), a.getY(), pm, d.getX(), d.getY() - tam, arrow=LAST,
                                                    smooth=True)
                        else:
                            if a.getY() <= d.getY():
                                pm = (d.getX() - (d.getX() - a.getX()) / 2, d.getY())
                                pt = (pm[0] + 30, pm[1] + 50)
                            else:
                                pm = (d.getX() - (d.getX() - a.getX()) / 2, a.getY())
                                pt = (pm[0] + 30, pm[1] - 50)
                            self.canvas.create_text(pt, text=c)
                            self.canvas.create_line(a.getX(), a.getY(), pm, d.getX(), d.getY() + tam, arrow=LAST,
                                                    smooth=True)
            # pintar estados
            self.canvas.create_oval(a.getX() - tam, a.getY() - tam, a.getX() + tam, a.getY() + tam, fill='red',
                                    activeoutline='blue', outline='black', width=2)
            if a.esAceptador() == 1:
                self.canvas.create_oval(a.getX() - 12, a.getY() - 12, a.getX() + 12, a.getY() + 12)
            if self.automata.inicial is a:
                self.canvas.create_line(a.getX() - tam * 2, a.getY(), a.getX() - tam, a.getY(), arrow=LAST)
            self.canvas.create_text(a.getX(), a.getY(), fill='black', text=a.getLabel())


if __name__ == '__main__':
    Ventana()
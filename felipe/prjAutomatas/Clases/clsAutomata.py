import clsEstado

class clsAutomata:
    def __init__(self, alfabeto):
        self.diccionarioEstados = {}
        if 'E' not in alfabeto:
            self.alfabeto = alfabeto + ['E']
        else:
            self.alfabeto = alfabeto
        self.inicial = None
        self.determinista = False
        self.tam = 30

    def nuevoEstado(self, estado):
        self.diccionarioEstados[estado] = {}
        for i in self.alfabeto:
            self.diccionarioEstados[estado][i] = []

    def nuevaTransicion(self, origen, destino, simbolo):
        if simbolo not in self.alfabeto:
            return
        self.diccionarioEstados[origen][simbolo].append(destino)

    def buscar(self, x, y):
        for e in self.diccionarioEstados.keys():
            if e.contains(x, y):
                return e
        return None

    def ordenar(self, lista):
        ordenada = []
        i = 0
        while len(ordenada) != len(lista):
            for j in lista:
                if int(j.getLabel()[1]) == i:
                    ordenada.append(j)
                    continue
            i += 1
        return ordenada

    def elimNoAcces(self):
        accesibles = []
        for i in self.diccionarioEstados.keys():
            for c in self.alfabeto:
                accesibles.extend(self.diccionarioEstados[i][c])
        listaElim = []
        for i in self.diccionarioEstados.keys():
            if i not in accesibles:
                listaElim.append(i)
        for i in listaElim:
            del self.diccionarioEstados[i]

    def marcarDist(self):
        mm = {}
        lista = self.ordenar(self.diccionarioEstados.keys())
        print lista
        length = len(self.diccionarioEstados.keys())
        for i in range(length - 1):
            mm[i] = {}
            for j in range(i + 1, length):
                print i, ' - ', j
                if lista[i].esAceptador() and (not lista[j].esAceptador()) or lista[j].esAceptador() and (not lista[i].esAceptador()):
                    mm[i][j] = 1
                else:
                    mm[i][j] = 0
        return mm

    def minimizar(self):
        self.elimNoAcces()
        mm = self.marcarDist()
        length = len(self.diccionarioEstados.keys())
        ordenados = self.ordenar(self.diccionarioEstados.keys())
        cambio = True
        while cambio:
            cambio = False
            for i in range(length - 1):
                for j in range(i + 1, length):
                    if mm[i][j] == 1:
                        continue
                    for c in self.alfabeto:
                        k = self.diccionarioEstados[ordenados[i]][c][0]
                        l = self.diccionarioEstados[ordenados[j]][c][0]
                        if k is not l:
                            if ordenados.index(k) > ordenados.index(l):
                                tmp = k
                                k = l
                                l = tmp
                            if mm[ordenados.index(k)][ordenados.index(l)] == 1:
                                mm[i][j] = 1
                                cambio = True
                                continue
        ne = []
        agrego = False
        elim = []
        print 'Imprimiendo matriz'
        for i in range(length - 1):
            for j in range(i + 1, length):
                print mm[i][j],
            print '-----------'
        for i in self.diccionarioEstados.keys():
            ne.append([i])
        for i in range(length - 1):
            for j in range(i + 1, length):
                if mm[i][j] == 0:
                    for n in ne:
                        if ordenados[i] in n:
                            for n2 in ne:
                                if ordenados[j] in n2:
                                    if n is n2:
                                        break
                                    n.extend(n2)
                                    elim = n2
                                    agrego = True
                            if agrego:
                                ne.remove(elim)
                                agrego = False
        # Crear nuevo automata
        automata2 = clsAutomata(self.alfabeto)
        for n in ne:
            acept = False
            ini = False
            for i in n:
                if i.isAcept():
                    acept = True
                if i is self.inicial:
                    ini = True
            e = clsEstado(n[0].getX(), n[0].getY(), 'q' + str(len(automata2.matriz.keys())), acept)
            automata2.nuevoEstado(e)
            if ini:
                automata2.inicial = e
                ini = False
        ordenados = self.ordenar(automata2.matriz.keys())
        for i in self.diccionarioEstados.keys():
            for c in self.alfabeto:
                if len(self.diccionarioEstados[i][c]) <= 0:
                    continue
                orig = ordenados[self.buscarIndiceContenedor(i, ne)]
                dest = ordenados[self.buscarIndiceContenedor(self.diccionarioEstados[i][c][0], ne)]
                if len(automata2.matriz[orig][c]) == 0:
                    automata2.nuevaTransicion(orig, dest, c)
                elif automata2.matriz[orig][c][0] != dest:
                    print 'Algoritmo Malo', automata2.matriz[orig][c][0]
        return automata2

    def convertirADeterminista(self):
        nuevoAutom = clsAutomata(self.alfabeto)
        nuevaMatriz = {}
        nuevoEst = EstadoEsp()
        for c in self.alfabeto:
            if c == 'E':
                continue
            if len(self.diccionarioEstados[self.inicial][c]) > 0:
                nuevoEst.add(self.inicial)
                break
        for n in self.obtenerSgtes(self.inicial, 'E'):
            if not nuevoEst.containsE(n):
                nuevoEst.add(n)
        nuevaMatriz[nuevoEst] = {}
        for c in self.alfabeto:
            nuevaMatriz[nuevoEst][c] = []
        nuevoAutom.inicial = nuevoEst
        it = nuevaMatriz.keys().__iter__()
        while True:
            try:
                actual = it.next()
                for c in self.alfabeto:
                    if c == 'E':
                        continue
                    ee = EstadoEsp()
                    for e in actual.estados:
                        for ne in self.obtenerSgtes(e, c):
                            if not ee.containsE(ne):
                                ee.add(ne)
                    esta = False
                    nuevaMatriz[actual][c] = [ee]
                    for k in nuevaMatriz.keys():
                        if k.equals(ee):
                            esta = True
                            break
                    if not esta:
                        nuevaMatriz[ee] = {}
                        for c2 in self.alfabeto:
                            nuevaMatriz[ee][c2] = []
            except StopIteration:
                break
        cont = 0
        x = 40
        y = 40
        for e in nuevaMatriz.keys():
            e.label = 'q' + str(cont)
            e.x = x
            e.y = y
            x += 100
            cont += 1
            if cont == 6:
                x = 30
                y += 100
        nuevoAutom.matriz = nuevaMatriz
        for x in nuevaMatriz.keys():
            for c in nuevoAutom.alfabeto:
                print x, c, nuevaMatriz[x][c]
        return nuevoAutom

    def obtenerSgtes(self, e, c):
        lista = []
        for d in self.diccionarioEstados[e][c]:
            for c2 in self.alfabeto:
                if c2 == 'E':
                    continue
                if len(self.diccionarioEstados[d][c2]) > 0:
                    if d not in lista:
                        lista.append(d)
            for d2 in self.diccionarioEstados[d]['E']:
                for nuevo in self.obtenerSgtes(d2, 'E'):
                    if nuevo not in lista:
                        lista.append(nuevo)
        for d in self.obtenerSgtes(e, 'E'):
            for c2 in self.alfabeto:
                if c2 == 'E':
                    continue
                if self.diccionarioEstados[d][c] > 0:
                    if d not in lista:
                        lista.append(d)
        return lista

    def aceptadores(self):
        lista = []
        for e in self.diccionarioEstados.keys():
            if e.isAcept():
                lista.append(e)
        return lista

    def buscarIndiceContenedor(self, e, lista):
        for i in lista:
            if e in i:
                return lista.index(i)
        return -1

    def buscarPorLabel(self, label):
        for i in self.diccionarioEstados.keys():
            if i.getLabel() == label:
                return i
        return None

    def esDeterm(self):
        for e in self.diccionarioEstados.keys():
            if (len(self.diccionarioEstados[e][chr(222)]) > 0):
                return False
            for c in self.alfabeto:
                if (len(self.diccionarioEstados[e][c]) > 1):
                    return False
        return True

    def exportarJSON(self):
        archivo = open('archivo', 'wb')
        archivo.write('{"automata":\n    [\n        {"estados":\n            [\n')
        listaEstados = self.ordenar(self.diccionarioEstados.keys())
        for i in listaEstados:
            archivo.write('                ' + i.aJson())
            if listaEstados[len(listaEstados) - 1] != i:
                archivo.write(',')
            archivo.write('\n')
        archivo.write('            ]\n        },')
        archivo.write('        {"matriz":\n            [\n')
        cadena = ''
        for i in listaEstados:
            for c in self.alfabeto:
                for j in self.diccionarioEstados[i][c]:
                    cadena += '                {"origen":"' + str(i) + '","destino":"' + str(
                        j) + '","caracter":"' + c + '"},\n'
        cadena = cadena[:len(cadena) - 2]
        archivo.write(cadena)
        archivo.write('            ]\n        },\n')
        archivo.write('        "inicial":"' + str(self.inicial) + '"')
        archivo.write('    ]\n}')
        archivo.close()

    def cambiarTam(self, tam):
        self.tam = tam
        for i in self.diccionarioEstados.keys():
            i.setTam(self.tam)

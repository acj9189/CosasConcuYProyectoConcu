

class clsEstado:
    def __init__(self, x, y, etiqueta, aceptador=None):
        self.posX = x
        self.posY = y
        self.etiqueta = etiqueta
        self.tam = 30
        if aceptador != None:
            self.aceptador = aceptador
        else:
            self.aceptador = False

    def __str__(self):
        return self.etiqueta

    def __repr__(self):
        return self.__str__()

    def setTam(self, nuevoTam):
        self.tam = nuevoTam

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY

    def esAceptador(self):
        return self.aceptador

    def setAcept(self, acept):
        self.aceptador = acept

    def getLabel(self):
        return self.etiqueta

    def contains(self, x, y):
        return self.posX - self.tam <= x and self.posX + self.tam >= x and self.posY - self.tam <= y and self.posY + self.tam >= y

    def aJson(self):
        return '{"label":"' + str(self.etiqueta) + '", "posX":' + str(self.posX) + ', "posY":' + str(self.posY) + ', "aceptador": ' + str(
            self.aceptador) + '}'


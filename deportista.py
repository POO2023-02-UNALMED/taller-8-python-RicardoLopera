class Deportista(object):
    def __init__(self, anosPracticando):
        self._deporte = "Futbol"
        self._anosPracticando = anosPracticando
    
    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, deporte):
        self._deporte = deporte

    def getAñosPracticando(self):
        return self._anosPracticando
    
    def setAñosPracticando(self, anosPracticando):
        self._anosPracticando = anosPracticando


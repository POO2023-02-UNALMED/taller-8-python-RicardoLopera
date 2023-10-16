class Deportista(object):
    def __init__(self, anosPracticando):
        self._deporte = "Futbol"
        self._anosPracticando = anosPracticando
    
    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, deporte):
        self._deporte = deporte

    def getAnosPracticando(self):
        return self._anosPracticando
    
    def setAnorPracticando(self, anosPracticando):
        self._anosPracticando = anosPracticando


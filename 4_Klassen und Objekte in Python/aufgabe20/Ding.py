class Ding:
    _dichte = {
        'Au': ('Gold', 19.32),
        'Ag': ('Silber', 10.5),
        'Fe': ('Eisen', 7.87)
    }

    def __init__(self, volumen, symbol):
        self.__volumen = volumen
        self._symbol = symbol

    def getMasse(self):
        masse = self.__volumen * self._dichte[self._symbol][1]
        return masse

    def getVolumen(self):
        volumen = self.__volumen
        return volumen

    def __str__(self):
        return f"Symbol: {self._symbol} - Dichte {self._dichte[self._symbol][1]} - Volumen: {self.__volumen}cm³"

class Data():
    def __init__(self, dia = 1, mes = 1, ano = 1980):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def setDia(self, dia):
        self.__dia = dia

    def getDia(self):
        return self.__dia
    
    def getMes(self):
        return self.__mes

    def setMes(self, mes):
        self.__mes = mes

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def __str__(self):
        return f'{self.getDia()}/{self.getMes()}/{self.getAno()}'
    
    def _valida(self,dia=0, mes=0, ano=0):
        if dia < 1 or dia > 31:
            return True
        elif mes < 1 or mes > 12:
            return True
        elif ano < 1:
            return True
        return False
    
    def _bisexto(self,ano):
        if ano % 400 == 0:
            return True
        elif ano % 4 == 0 and ano % 100 != 0:
            return True
        else:
            return False


        

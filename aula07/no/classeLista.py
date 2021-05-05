from classeNo import No

class Lista():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.size = 0
   
    def estaVazia(self):
        return self.size
        
    def getPrimeiro(self):
        return self.primeiro.info
        
    def getUltimo(self):
        return self.ultimo.info
    
    def addInicio(self, valor):
        if self.size == 0:
            self.primeiro = self.ultimo = No(None, valor, None)
        else:
            self.primeiro = No(None, valor, self.primeiro)
            self.primeiro.proximo.anterior = self.primeiro
        self.size += 1

    def addFim(self, valor):
        if self.size == 0:
            self.primeiro = self.ultimo = No(None, valor, None)
        else:
            self.ultimo = No(self.ultimo, valor, None)
            self.ultimo.anterior.proximo = self.ultimo
        self.size += 1

    def imprimir(self):
        aux = self.primeiro
        while aux != None:
            print(aux.info)
            aux = aux.proximo

    def delInicio(self):
        if self.size == 1:
            self.primeiro = self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
        self.size -= 1

    def delFim(self):
        if self.size == 1:
            self.primeiro = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
        self.size -= 1

    



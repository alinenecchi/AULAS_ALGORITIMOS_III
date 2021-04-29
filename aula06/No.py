class Node:
    def __init__(self, label):
        self.label = label  #nome do nodo
        self.next = None    #Ponteiro para o proximo/ ao inicializar o proximo vai comecar zerado
    
    def getLabel(self):
        return self.label
    
    def set_label(self, label):
        self.label = label
    
    def getNext(self):
            return self.label
    
    def set_next(self, next):
        self.next = next
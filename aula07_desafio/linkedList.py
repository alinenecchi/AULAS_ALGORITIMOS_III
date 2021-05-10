from node import Node 

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def appendList(self, element):
        if self.head:
            # inserção quando a lista já possui elements
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)  # Primeira inserção
        self._size = self._size + 1


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _getNode(self, index):
        pointer = self.head
        for index in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Índex Desconhecido")
        return pointer

    def set(self, index, element):
        pass
    def __getItem__(self, index):

        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("Índex Desconhecido")

    def __setItem__(self, index, element):
        pointer = self._getNode(index)
        if pointer:
            pointer.data = element
        else:
            raise IndexError("Índex Desconhecido")

    def searchList(self, element):
        """Retorna o indice elem se ele estiver na lista ou none, caso contrário"""
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == element:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} - Esse element não está na lista".format(element))

    def insertList(self, index, element):  # inserção de element em qualquer posição
        node = Node(element)
        if index == 0:   # O[1]
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index - 1)
            node = Node(element)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1


    def removeList(self, element):
        if self.head is None:
            raise ValueError("{} - Esse element não está na lista".format(element))
        elif self.head.next == element:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            antecessor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == element:
                    antecessor.next = pointer.next
                    pointer.next = None
                antecessor = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + " -> "
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


from node import Node


# inserir
# remover
# observar o top da Stack

class Stacks:
    def __init__(self):
        self.top = None
        self._size = 0

    # Enquadra nos casos especiais, 4 op elementares, complexidade de O[1]
    def pushStaks(self, element):  # Insere um element na Stack
        node = Node(element)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    # Operações constantes, complexidade de O[1]
    def popStacks(self):  # remove o element do top da Stack
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("A Stack está vazia")

    # Operações constantes, complexidade de O[1]
    def peekStacks(self):  # retorna o top sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("A Stack está vazia")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


'''
    COMANDOS PARA EXECUTAR EM TESTES

Stack = Stack()  # Cria uma Stack

Stack.pushStaks(23)
Stack.pushStaks('python')
Stack.pushStaks(5)
Stack.pushStaks('Sucesso')
Stack.pushStaks(10)
Stack.pushStaks(24.5)    # Adiciona elements na Stack ( Do top pra baixo )

Stack  
print(Stack)   # Comandos para ver a Stack listada


Stack.peekStacks()   # Ver o top da Stack

Stack.popStacks()   # Retira elements da Stack ( Do top pra baixo )

len(Stack)   # Ve a quantidade de elements que há na Stack
'''
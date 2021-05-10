from stacks import Stacks
stack = Stacks()  # Cria uma Stack

stack.pushStaks(23)
print(stack)
stack.pushStaks('python')
print(stack)
stack.pushStaks(5)
print(stack)
stack.pushStaks('Sucesso')
print(stack)
stack.pushStaks(10)
print(stack)
stack.pushStaks(24.5)    # Adiciona elements na Stack ( Do top pra baixo )

print(stack)   # Comandos para ver a Stack listada


stack.peekStacks()   # Ver o top da Stack

stack.popStacks()   # Retira elements da Stack ( Do top pra baixo )

len(stack)   # Ve a quantidade de elements que há na Stack

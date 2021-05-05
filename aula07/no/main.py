from classeLista import Lista

lista = Lista()
lista.imprimir()
lista.addInicio( 3 )
lista.addInicio( 10 )
lista.addFim(11)
lista.addInicio(50)
print( "Tamanho da Lista: " ,str(lista.size))
lista.imprimir()
lista.delInicio()
print( "Tamanho da Lista: " ,str(lista.size))
lista.imprimir()

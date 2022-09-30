from lista import Lista
lista = Lista()


lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
lista.adicionar(4)
lista.adicionar(5)
lista.adicionar(6)
lista.adicionar(6)
lista.adicionar(6)


print("lista inicial: ")
lista.show()
lista.remover_um(4)
print("lista retirando 1 numero (4): ")
lista.show()
lista.adicionar("casa")
print("lista depois de adicionar 'casa': ")
lista.show()